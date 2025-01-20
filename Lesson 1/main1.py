# create a dictionary key:value pair
sample_dict = {
    "name" :"Sangeeta",
    "age" : 29,
    "country" : "India"
}

# access values in dictionary
print (sample_dict)
print (sample_dict["country"])

# difference between list and Dictionary
sample_list = ["Sangeeta", 29, "India"]
print (sample_list[2])   # index-position starts with "0"

# get list of keys and values
print (sample_dict.keys ())
print (sample_dict.values ())

# keys one after the another
for x in sample_dict.keys () :
    print (x)

# keys one after the another along with their values
for x in sample_dict.keys () :
    print (x, sample_dict[x])

# check if a key exists in the dictionary or not
if "country" in sample_dict :
    print ("key exists")
else :
    print ("key doesn't exist")

# add key-value pair in dictionary
sample_dict ["city"] = "Guwahati"
print (sample_dict)

# changing key-value pair
sample_dict ["city"] = "Nongstoin"
print (sample_dict)

# delete key-value pair
del (sample_dict["city"])
print (sample_dict)

# storing a list in the dictionary
sample_dict ["hobbies"] = ["waching web seires", "coding", "playing with pets"]
print (sample_dict)

# access a value in list stored in dictionary
print (sample_dict ["hobbies"] [1])

# creating a nested dictionary
classroom_dict = {
    "Student1" : {
        "age" : 10,
        "marks" : [89,92,78,84,90]
    },
    "Student2" :{
        "age" : 9,
        "marks" : [67,69,78,74,80]
    }
}

# getting the keys and values of nested dictionary
print (classroom_dict.keys ())
print (classroom_dict.values ())

# getting key's values one after the another
for i in classroom_dict.keys () :
    print (classroom_dict[i])

# change the value of nested dictionary
classroom_dict ["Student1"] ["age"] = 9
print (classroom_dict)