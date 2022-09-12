import json
import os


def count_lines(name):
    with open (name) as text_file:
        text = [string.rstrip() for string in text_file.readlines()]

        return len(text)


def count_chars(name):
    with open (name) as text_file:
        text = [word for word in text_file.read()]

        return len(text)


def test(*func, name):
    
    return count_lines(name), count_chars(name)

print(test(name='text.txt'))
