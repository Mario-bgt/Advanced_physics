"""Implement a function is_perfect_pangram, which takes a string sentence and an optional string alphabet as arguments.
A "pangram" is a word or sentence that uses all letters in an alphabet at least once. A "perfect pangram" uses each
 letter exactly once.
The function is_perfect_pangram should check if sentence is a perfect pangram for the given alphabet. If no alphabet
 is given, the 26 letters of the English alphabet should be assumed. Character casing and any characters that are not
  part of the alphabet should be ignored.
You may assume that is_perfect_pangram will only be constructed with parameters that match the description. Make sure
 you correctly formulate the function signature.
Use the following template:"""


def is_perfect_pangram(str, alphabet = "abcdefghijklmnopqrstuvwxyz"):
    str = "".join([c if c in alphabet else "" for c in str ])
    for char in alphabet:
        if char not in str.lower():
            return False
    if len(str) != len(alphabet):
        return False
    return True




print( is_perfect_pangram("Mr Jock, TV quiz PhD, bags few lynx") )
print( is_perfect_pangram("a b c", "abc") )
print( is_perfect_pangram("azbzc", "abc") )
print( is_perfect_pangram("abc", "abcd") )
print( is_perfect_pangram("abb", "abc") )
