"""AHC040
Packing Uncertain Rectangles

30 <= N <= 100
N/2 <= T <= 4*N
1000 <= sigma <= 10000: 標準偏差σ
1 <= w,h <= 10**9

Time Limit: 3s (3000ms)

同じ面積でも正方形に近いほど(横幅+縦幅)の値は小さくなる = 正方形を目指す
"""

import random
import sys
from enum import IntEnum
from math import ceil, log2
from time import time
from typing import List, Optional, Tuple

program_start_ts = time()
random.seed(40)

INF = 10**12
X = 1.2  # 外箱の横幅を補正する定数(最小/最大の幅*Xの範囲にする)
C = 1.2  # ループ時間を補正する定数(測定時間*Cの値を参考にする)
LIMIT_TIME = 2.6  # この時間経過すると最後の処理へ移る(途中打ち切り)

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

class Rect:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

class NFP:
    """No Fit Polygon
    配置済み矩形に新しく矩形を配置すると重なってしまう領域
    -> NFPに被ると配置不可. NFPの外は配置可能
    """
    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class VEdgeType(IntEnum):
    RIGHT = 0
    LEFT = 1

class HEdgeType(IntEnum):
    TOP = 0
    BOTTOM = 1

class VEdge:
    def __init__(self, x: int, y: int, type_: VEdgeType, placement_index: int) -> None:
        self.x = x
        self.y = y
        self.type_ = type_
        self.placement_index = placement_index

class HEdge:
    def __init__(self, x: int, y: int, type_: HEdgeType, placement_index: int) -> None:
        self.x = x
        self.y = y
        self.type_ = type_
        self.placement_index = placement_index

class Node:
    def __init__(self, p_self: int, p_min: int, p_max: int, parent: Optional["Node"], left: Optional["Node"], right: Optional["Node"]) -> None:
        self.p_self = p_self
        self.p_min = p_min
        self.p_max = p_max
        self.parent = parent
        self.left = left
        self.right = right

    def add(self, lambda_: int) -> None:
        self.p_self += lambda_
        self.p_min += lambda_

    def update_min(self) -> None:
        self.p_min = self.p_self + min(self.left.p_min, self.right.p_min)

class Tree:
    def __init__(self, num_intervals: int) -> None:
        depth = int(ceil(log2(num_intervals - 1)))
        num_leaves = 2**depth
        num_nodes = 2**(depth + 1) - 1
        num_internal_nodes = num_nodes - num_leaves
        num_dummy_leaves = num_leaves - num_intervals + 1
        nodes = [Node(0, 0, 0, None, None, None) for _ in range(num_nodes)]
        for i in range(num_internal_nodes):
            left = nodes[2*i + 1]
            right = nodes[2*i + 2]
            nodes[i].left = left
            nodes[i].right = right
            left.parent = nodes[i]
            right.parent = nodes[i]
        for i in range(num_nodes - num_dummy_leaves, num_nodes):
            nodes[i].p_self = 1
            nodes[i].p_min = 1
            nodes[i].p_max = 1
        for i in reversed(range(num_internal_nodes)):
            nodes[i].update_min()
        self.root = nodes[0]
        self.leaves = nodes[num_internal_nodes:]

    def update_values(self, sweep_line_type: HEdgeType, left_index: int, right_index: int) -> None:
        """新しいNFPに応じて葉ごとのNFPの重複数を更新"""
        lambda_ = -1 if sweep_line_type == HEdgeType.TOP else 1
        left = self.leaves[left_index]
        right = self.leaves[right_index]
        left.add(lambda_)
        right.add(lambda_)
        while left.parent is not right.parent:
            if left is not left.parent.right:
                left.parent.right.add(lambda_)
            if right is not right.parent.left:
                right.parent.left.add(lambda_)
            left.parent.update_min()
            right.parent.update_min()
            left = left.parent
            right = right.parent
        node = left.parent
        while node is not None:
            node.update_min()
            node = node.parent

    def find_no_overwrap(self, alpha: int) -> Optional[int]:
        """左の葉から探索してNFPが存在しない(被らない)最初の葉を返す"""
        def _find(node: Node, offset: int, num_leaves: int) -> Optional[int]:
            if alpha >= offset + num_leaves:
                return None
            if node.p_min > 0:
                return None
            if node.left is None:
                return offset
            else:
                k = num_leaves // 2
                result = _find(node.left, offset, k)
                if result is None:
                    result = _find(node.right, offset + k, k)
                return result
        return _find(self.root, 0, len(self.leaves))

def _NFPs_to_edges(nfps: list[NFP]) -> Tuple[List[VEdge], List[HEdge]]:
    """NFPを辺に分解する"""
    left_right_edges = []
    top_bottom_edges = []
    for i, nfp in enumerate(nfps):
        left = VEdge(nfp.x1, nfp.y2, VEdgeType.LEFT, i)
        right = VEdge(nfp.x2, nfp.y2, VEdgeType.RIGHT, i)
        top = HEdge(nfp.x2, nfp.y2, HEdgeType.TOP, i)
        bottom = HEdge(nfp.x2, nfp.y1, HEdgeType.BOTTOM, i)
        left_right_edges.extend([left, right])
        top_bottom_edges.extend([top, bottom])
    return left_right_edges, top_bottom_edges

def _get_interval_indices(intervals: List[VEdge]) -> Tuple[List[int], List[int]]:
    """左辺/右辺の集合からインターバルを取得する
    i番目の配置済み矩形に対して
    - 左辺のx座標: left_right_edges[interval_indices[i][0]]
    - 右辺のx座標: left_right_edges[interval_indices[i][1]]
    になるようにinterval_indicesを作成
    """
    num_placements = len(intervals) // 2
    placement_to_left_indices = [-1 for _ in range(num_placements)]
    placement_to_right_indices = [-1 for _ in range(num_placements)]
    for j, e in enumerate(intervals):
        if e.type_ == VEdgeType.LEFT:
            placement_to_left_indices[e.placement_index] = j
        else:
            placement_to_right_indices[e.placement_index] = j
    return placement_to_left_indices, placement_to_right_indices

def find_bl(nfps: List[NFP], new_rect: Rect, box_height: int) -> Optional[Point]:
    """探索処理"""
    y_limit = box_height - new_rect.height
    # NFPから辺に分解
    left_right_edges, top_bottom_edges = _NFPs_to_edges(nfps)
    # 辺をソート
    intervals = sorted(left_right_edges, key=lambda e: (e.x, e.type_, e.y))
    sweep_lines = sorted(top_bottom_edges, key=lambda e: (e.y, e.type_, e.x))
    placement_to_left_indices, placement_to_right_indices = _get_interval_indices(intervals)
    tree = Tree(len(intervals))
    for sweep_line in sweep_lines:
        i = sweep_line.placement_index
        left_leaf = placement_to_left_indices[i]
        right_leaf = placement_to_right_indices[i] - 1
        # NFPの重複を更新
        tree.update_values(sweep_line.type_, left_leaf, right_leaf)
        if sweep_line.y > y_limit:
            break
        if sweep_line.y < 0:
            continue
        if sweep_line.type_ == HEdgeType.TOP:
            found_leaf = tree.find_no_overwrap(left_leaf)
            if found_leaf is not None:
                y = sweep_line.y
                x = intervals[found_leaf].x
                return Point(x, y)
    return None

def create_placements_of_box(box: Rect) -> List[Tuple[Point, Rect]]:
    c = 1
    return [
        (Point(0, -c), Rect(box.width, c)),
        (Point(-c, 0), Rect(c, box.height)),
        (Point(box.width, 0), Rect(c, box.height)),
    ]

def create_NFP(point: Point, rect: Rect, new_rect: Rect) -> NFP:
    x1 = point.x - new_rect.width
    y1 = point.y - new_rect.height
    x2 = point.x + rect.width
    y2 = point.y + rect.height
    return NFP(x1, y1, x2, y2)

def find_BL_point(placements: List[Tuple[Point, Rect]], new_rect: Rect, box: Rect) -> Optional[Point]:
    placements = create_placements_of_box(box) + placements
    nfps = [create_NFP(point, rect, new_rect) for point, rect in placements]
    return find_bl(nfps, new_rect, box.height)

def input():
    return sys.stdin.readline().strip()

def check_stopping(crt_time: float, fin_time: float) -> bool:
    if fin_time == 0.0:
        return False
    loop_time = crt_time - fin_time  # 1つ解答する時間
    # 残り時間が今回のループ時間(*補正値)分余っているならTrue
    return LIMIT_TIME - (crt_time - program_start_ts) <= loop_time*C

def query(res: list, is_last: bool = False) -> Tuple[int, int]:
    """結果を出力しそれに対応した横/縦幅を返す"""
    print(len(res), flush=True)
    for p, r, d, b in res:
        print(p, r, d, b, flush=True)
    if is_last:
        return -1, -1
    w, h = map(int, input().split())
    return w, h

def solve() -> None:
    """解答
    横幅は最低/最高幅を決めて, その範囲でランダムに(T - 1)個生成する
    """
    fin_time = 0.0
    cnt = 0

    N, T, sigma = map(int, input().split())
    whl = [tuple(map(int, input().split())) for _ in range(N)]

    ROOT_N = N**0.5
    width_min = int(-(-sum([min(w, h) for w, h in whl]) // ROOT_N) * X)
    width_max = int(-(-sum([max(w, h) for w, h in whl]) // ROOT_N) * X)

    # TODO: 局所探索により少しずつ改善箇所を見つけて更新していく
    rl = [random.randint(0, 1) for _ in range(N)]
    for _ in range(T - 1):
        # TLE対策: 残り時間が足りそうにない場合は途中打ち切り
        crt_time = time()
        if check_stopping(crt_time, fin_time):
            break

        query([])
        cnt += 1

    # 途中で打ち切った場合に残り回数を消費
    for _ in range(T - 1 - cnt):
        query([])
    # T回目=最終結果を出力
    query([], is_last=True)


if __name__ == "__main__":
    solve()
