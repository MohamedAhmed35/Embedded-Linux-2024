def isVowel(char):
    if(char == "a" or char == "e" or char == "i" \
       or char == "o" or char == "u"):
        print("Vowel")
    else:
        print("Not a Vowel")

letter = input("Enter a letter: ")
letter = letter.lower()
isVowel(letter)
