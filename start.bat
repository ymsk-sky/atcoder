@echo off
IF Exist %1 EXIT /B
mkdir %1
cd %1
type nul > a.py
type nul > b.py
type nul > c.py
type nul > d.py
type nul > e.py
