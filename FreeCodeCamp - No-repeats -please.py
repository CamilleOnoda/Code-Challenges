#eturn the number of total permutations of the provided string that don't have 
#repeated consecutive letters. Assume that all characters in the provided string are each unique.
#For example, aab should return 2 because it has 6 total permutations 
#(aab, aab, aba, aba, baa, baa), but only 2 of them (aba and aba) 
#don't have the same letter (in this case a) repeating.

from itertools import permutations

def permAlone(string):
    def repeat_letters(s):
      for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
          return True
      return False

    count = 0
    for perm in permutations(string):
        if not repeat_letters(perm):
            count += 1
    return count

print(permAlone("abcdefa"))