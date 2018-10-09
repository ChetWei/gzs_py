# -*- coding: utf-8 -*-

def lines(file):
    for line in file:
        yield '\n'
        
        

def bllocks(file):
    block = []
    for line in file:
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()   #空行
            block = []
