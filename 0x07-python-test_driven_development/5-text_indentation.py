#!/usr/bin/python3
"""Defines a function that prints a text with 2 new lines after each,
of these characters: . ? and :
Attributes:
    text_indentation: function that prints a text with specific conditions
"""


def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    string = text.replace('.', '.\n\n').replace(':', ':\n\n')\
        .replace('?', '?\n\n')
    for i in range(len(text)):
        string = string.replace('\n ', '\n')

    print(string, end='')
