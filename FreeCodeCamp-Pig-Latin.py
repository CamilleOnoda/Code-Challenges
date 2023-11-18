def translatePigLatin(word):
    vowels = "aeiou"

    if word[0] in vowels:
        # If the word starts with a vowel, add "way" at the end
        pig_latin = word + "way"
    else:
        # If a word begins with a consonant, take the first consonant or 
        # consonant cluster, move it to the end of the word, and add "ay" to it.
        index = 0
        while index < len(word) and word[index] not in vowels:
            index += 1
        pig_latin = word[index:] + word[:index] + "ay"

    return pig_latin

print(translatePigLatin("california"))
print(translatePigLatin("glove"))
print(translatePigLatin("algorithm"))
print(translatePigLatin("eight"))  
print(translatePigLatin("schwartz"))
print(translatePigLatin("rhythm"))
