# Count the occurrence of vowels in the string entered by the user
vowel_dict = {
    "a" : 0,
    "e" : 0,
    "i" : 0,
    "o" : 0,
    "u" : 0,
}
input_str = input ("Enter the string : ").lower ()
for x in input_str :
    if x in vowel_dict :
        vowel_dict [x] += 1

print (vowel_dict)
