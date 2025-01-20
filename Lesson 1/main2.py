# World Countries capitals database

#create empty dictionary
country_dict = {}

# forever loop
while True :
    # printing menu
    print ("1. Add country and capital name")
    print ("2. Display all countries name")
    print ("3. Display all capitals name")
    print ("4. Display capital of a specific country")
    print ("5. Delete an entry")

    # get user choice
    choice = int (input ("Enter your choice (1-5) : "))

    # choice 1 - add country and capitals
    if choice == 1 :
        country = input ("Enter country's name : ").upper ()
        capital = input ("It's capital name : ").upper ()
        country_dict [country] = capital
        

    # choice 2 - display all countries
    elif choice == 2 :
        print (list (country_dict.keys ()))

    # choice 3 - display all capitals
    elif choice == 3 :
        print (list (country_dict.values ()))

    #choice 4 - Display capital of a specific country
    elif choice == 4 :
        choice2 = input ("Enter the country to know it's capital : ").upper ()
        if choice2 in country_dict :
            print (country_dict [choice2])
        else :
            print ("Info isn't present in the directory")
    
    # choice 5 - Delete an entry
    elif choice == 5 :
        choice2 = input ("Enter the country you want to delete : ").upper ()
        del (country_dict [choice2])
    
    else :
        break

    print (country_dict)
    print ()
