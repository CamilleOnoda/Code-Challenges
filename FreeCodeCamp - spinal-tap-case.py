"""Spinal Tap Case
Convert a string to spinal case.
Spinal case is all-lowercase-words-joined-by-dashes.
spinalCase("This Is Spinal Tap") should return the string this-is-spinal-tap.
spinalCase("thisIsSpinalTap") should return the string this-is-spinal-tap.
spinalCase("The_Andy_Griffith_Show") should return the string the-andy-griffith-show.
spinalCase("Teletubbies say Eh-oh") should return the string teletubbies-say-eh-oh.
spinalCase("AllThe-small Things") should return the string all-the-small-things."""

import re


def spinalCase(str):
  str = re.sub(r'[\s_]', '-', str)
  str = re.sub(r'([a-z])([A-Z])', r'\1-\2', str).lower()
  print(f"{str}\n")


spinalCase('This Is Spinal Tap')
spinalCase('thisIsSpinalTap')
spinalCase('The_Andy_Griffith_Show')
spinalCase('Teletubbies say Eh-oh')
spinalCase('AllThe-small Things')
