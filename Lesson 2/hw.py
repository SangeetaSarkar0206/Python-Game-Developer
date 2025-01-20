"""
The new academic year is starting and you as the store manager are told to take care of accounts of 
textbook purchases. As a python programmer, you decide to maintain a dictionary of textbooks and its 
cost. Create the dictionary.
a) Later you found that the cost of the physics book was entered wrong. Correct price is 200. 
Make this change.
b) Add the cost of 2 more books to the dictionary.
c) Print cost of the book entered by the user.
d) Print all the books and their cost.
"""

book_dict = {
    "English" : 180,
    "Mathematics" : 250,
    "Chemistry" : 190,
    "Biology" : 170,
    "Physics" : 180,
    "Economics" : 90
}
while True : 
    print ("1. To adjust price of book.")
    print ("2. Add price of book.")
    print ("3. Print cost of a book.")
    print ("4. Print price of all books.")

    user = int (input ("Enter your choice (1-4): "))

    # To adjust price of book.
    if user == 1 :
        b_name = input ("Enter the name of the book :")
        if b_name in book_dict :
            b_price = int (input ("Enter the price of book : "))
            book_dict [b_name] = b_price
        else :
            print ("Book not found.")

    #Add price of book.
    elif user == 2 :
        b_name = input ("Enter name of book : ")
        b_price = input ("Enter the price : ")
        book_dict [b_name] = b_price

    # Print cost of a book.
    elif user == 3 :
        b_name = input ("Enter book name to know it's price : ")
        if b_name in book_dict :
            print ("Price = ", book_dict [b_name])
        else :
            print ("Book not found.")

    # Print price of all books.
    elif user == 4 :
        print (book_dict)

    else : 
        break

    print ()




