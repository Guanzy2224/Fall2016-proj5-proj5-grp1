# -*- coding: utf-8 -*-

from sample import themain

def generate1():
    start = request.vars.start_with1
    pred = themain(start,1)
    pred=pred.replace("\n","<br/>")
    return pred

def generate2():
    start = request.vars.start_with2
    pred = themain(start,2)
    pred=pred.replace("\n","<br/>")
    return pred

def generate3():
    start = request.vars.start_with3
    pred = themain(start,3)
    pred=pred.replace("\n","<br/>")
    return pred

def generate4():
    start = request.vars.start_with4
    pred = themain(start,4)
    pred=pred.replace("\n","<br/>")
    return pred

def test():
    return locals()

def music_start_form():
    return locals()
