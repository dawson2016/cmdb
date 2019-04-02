#!/usr/bin/env python
#coding:utf-8
from __future__ import absolute_import
from celery import task
from celery import platforms
import time
platforms.C_FORCE_ROOT = True
#app = Celery('tasks',backend="redis", broker='redis://127.0.0.1:6379/0')
#@app.task
@task
def add(x, y):
    print 'hello celery'
    time.sleep(10)
    return x + y
