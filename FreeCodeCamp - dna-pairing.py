"""DNA Pairing
Pairs of DNA strands consist of nucleobase pairs. Base pairs are represented by 
the characters AT and CG, which form building blocks of the DNA double helix.
The DNA strand is missing the pairing element. Write a function to match the 
missing base pairs for the provided DNA strand. For each character in the provided string, find the base pair character. Return the results as a 2d array.
For example, for the input GCG, return [["G", "C"], ["C","G"], ["G", "C"]]
The character and its pair are paired up in an array, and all the arrays are 
grouped into one encapsulating array."""

pairs = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G",
}

def pairElement(str) -> None:
    new_list = []
    for char in str:
        if char in pairs:
            value = pairs[char]
            new_item = [char, value]
            new_list.append(new_item)
    print(new_list)


pairElement("GCG")
pairElement("ATCGA")
pairElement("TTGAG")
pairElement("CTCTA")

