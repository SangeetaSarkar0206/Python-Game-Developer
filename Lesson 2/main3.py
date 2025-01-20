#Find if a given number entered by the user is a pangram or not ? 

num_dict = {
    "0" : 0,
    "1" : 0,
    "2" : 0,
    "3" : 0,
    "4" : 0,
    "5" : 0,
    "6" : 0,
    "7" : 0,
    "8" : 0,
    "9" : 0
}
user = input("Enter the number to check if it's pangram : ")
for x in user :
    if x in num_dict :
        num_dict [x] += 1

yes_no = True
for every_value in num_dict.values () :
    if every_value == 0 :
        yes_no = False

if yes_no == True : 
    print("Entered number is a Panagram")
else:
    print("Entered number is not a Panagram")
