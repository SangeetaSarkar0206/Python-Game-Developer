name = []
print ("Welcome to Name Database")
print ("You can now create your own database. Select from the options below.")

while True :
    
    print ("1. Add a name to the list")
    print ("2. Change a name in the list")
    print ("3. Delete a name from the list")
    print ("4. View all the names in the list")
    print ("5. End the program")
    print ("")
    user = int (input ("Please select the option : "))

    if user == 1 :
        n = input ("Enter a name you want to add : ")
        print (n, "has been added to the list.")
        name.append (n)
    elif user == 2 :
        n = input ("Enter the name you want to change : ")
        if n in name :
            pos = name.index(n)
            x = input ("Please enter the changed name : ")
            name[pos] = x
        else :
            print ("Name is not in the list.")
    elif user == 3 :
        n = input ("Enter the name you want to delete : ")
        if n in name :
            name.remove(n)
            print (n, "is removed from the list.")
        else :
            print ("Name is not in the list.")
    elif user == 4:
        print ("Here, is the list: ")
        print (name)
    elif user == 5 :
        break
    else :
        print ("Enter a valid option number.")
    print ("-"*40)       
    

