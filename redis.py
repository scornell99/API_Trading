# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:05:44 2016

@author: scornell
"""

import redis

r = redis.StrictRedis(host='localhost', port=6379,db=0)
r.set('foo', 'bar')
