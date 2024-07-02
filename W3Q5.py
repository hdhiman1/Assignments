def is_vowel(letter):
    vowels = "AEIOUaeiou"
    return letter in vowels

# Assuming Table1 is a list of words
Table1 = ["example", "word", "set", "up", "beautiful"]  # Replace with actual data
Table2 = []

count = 0

while len(Table1) > 0:
    # Read the first row X in Table 1
    X = Table1.pop(0)
    # Move X to Table 2
    Table2.append(X)
    i = len(X)
    C = 0
    A = False
    B = False
    
    while i > 0:
        i -= 1
        letter = X[i]
        if is_vowel(letter):
            if A and not B:
                C = 1
            A = True
            B = False
        else:
            if not A and B:
                C = 1
            A = False
            B = True
    
    if C == 0:
        count += 1

print("Count of words with no vowel-consonant or consonant-vowel transitions:", count)
print("Table2:", Table2)
