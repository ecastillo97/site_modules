found = {'u' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'a' : 0}
word = input("Provide a word to search for vowels: ").lower()
for letter in word:
    if letter in found:
       found[letter] += 1
for vowel,count in sorted(found.items()):
    print(vowel, 'was found', count, 'time(s).')
