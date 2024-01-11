#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def count_vowels(input_string):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    vowel_count = input_string.intersection(vowels)

    return vowel_count


if __name__ == "__main__":
    user_input = input("Введите строку: ")
    input_set = set(user_input)
    result = count_vowels(input_set)
    print("Количество гласных в строке:", len(result))
    print(result)
