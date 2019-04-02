#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年4月14日
 
@author: Administrator
'''
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.context_processors import request
def require_login(func):
    def _deco(request):
        if request.session.get('IS_LOGIN')!=True:
            return HttpResponseRedirect(reverse('login'))
        else:
            return func(request)
    return _deco
