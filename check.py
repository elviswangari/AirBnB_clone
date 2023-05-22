#!/usr/bin/python3
""" A script to test pycodestyle"""


class Check:
    def check(name, key="works"):
        print(f"its {name} and it {key}")


Check.check('elvis')
