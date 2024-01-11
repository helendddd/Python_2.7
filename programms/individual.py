#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")
    a = {"c", "e", "h", "n"}
    b = {"e", "f", "k", "n", "x"}
    c = {"b", "c", "h", "p", "r", "s"}
    d = {"b", "e", "g"}

    x = (a - b) & (c | d)
    print(f"x = {x}")

    not_b = u - b

    y = (a & not_b) | (c - d)
    print(f"y = {y}")
