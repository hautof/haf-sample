#encoding='utf-8'

import os, sys


class TestCheck(object):
    def test_check_1(self, r, t):
        print("test here of TestCheck")
        print(r)
        print(t)
        assert r==t