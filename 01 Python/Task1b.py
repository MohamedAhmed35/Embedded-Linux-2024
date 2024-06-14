def isVowel(char):
    char = char.lower()
    vowels = "aeiou"
    print("vowel") if char in vowels else print("Not a Vowel")

letter = input("Enter a letter: ")
isVowel(letter)