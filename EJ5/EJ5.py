#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def trueFibo(n):
    if n <= 2:
        if n == 2: return True
        if n < 2: return False
    return (trueFibo(n-1) ^ trueFibo(n-2))
