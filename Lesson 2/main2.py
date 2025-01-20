# Count the occurrence of each alphabhet in the string entered by the user
input_str = input ("Enter the string : ").lower ()
count = {}

for x in input_str :
    if x in count :
        count [x] += 1
    else :
        count [x] = 1

print (count)