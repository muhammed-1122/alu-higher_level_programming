#!/usr/bin/python3
"""
Module that indents text.
"""

def text_indentation(text):
    """Prints text with two new lines after '.', '?', and ':'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    split_text = ""
    for char in text:
        split_text += char
        if char in ".?:":
            print(split_text.strip(), end="\n\n")
            split_text = ""
    if split_text.strip():
        print(split_text.strip(), end="")
