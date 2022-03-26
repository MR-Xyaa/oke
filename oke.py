#!/usr/bin/python
# encoding: utf-8
"""
Author : MR-Xyaa
Github : https://github.com/MR-Xyaa
Facebook : Xyaa Xyaa
Date : 26-03-2022
"""
import os, sys, time, urllib
R = '\x1b[1;31m'
N = '\x1b[0m'
Y = '\x1b[1;33m'
G = '\x1b[1;37m'

def restart_program():
	python = sys.executable
	os.execl(python, python, *sys.argv)
	curdir = os.getcwd()
	
	
def banner():
    print '%s   {●]▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪[● ]%s' % (R, Y, R, N)
    print '%s                   [•]Author____: MR-Xyaa%s' % (R, N)
    print '%s                   [•]Github____: https://github.com/MR-Xyaa%s' % (R, N)
    print '%s                   [•]Facebook__: Xyaa Xyaa%s' % (R, N)
    print '%s   {●]▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪[●] %s' % (R, Y, R, N)
    
    
   
