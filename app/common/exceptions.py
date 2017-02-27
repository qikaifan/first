#!/usr/bin/env python
# -*- coding: utf-8 -*-


class IllegalArgumentException(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class UnauthorizedException(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
