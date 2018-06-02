#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
import datetime
from memobird.libs.pymobird import SimplePymobird


_bird = SimplePymobird(ak=os.getenv("AK"),
                      device_id=os.getenv("DEVICE_ID"))

def print_text(txt):
    _bird.print_text(txt)


def print_notice(title, body):
    d = {'title': title, 
         'body': body, 
         'today': str(datetime.datetime.now().date())}
    _bird.print_text("================================\n"
                     "{title:^32}\n"
                     "--------------------------------\n"
                     "{body}\n"
                     "================================"
                     "{today:>32}\n".format(**d))
