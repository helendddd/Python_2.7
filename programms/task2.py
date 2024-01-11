#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def common_characters(string1, string2):
    set1 = set(string1)
    set2 = set(string2)
    common_chars = set1 & set2
    return common_chars


if __name__ == "__main__":
    input_str1 = input("Введите первую строку: ")
    input_str2 = input("Введите вторую строку: ")

    common_chars_set = common_characters(input_str1, input_str2)

    if common_chars_set:
        print("Общие символы в двух строках:", ', '.join(common_chars_set))
    else:
        print("Нет общих символов в двух строках.")
