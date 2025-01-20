"""
Write a program that uses a dictionary that contains ten usernames and passwords. 
The program should ask the user to enter their username and password. 
If the username is not in the dictionary, the program should indicate that the person is not a valid user of the system. 
If the username is in the dictionary, but the user does not enter the right password, the program should say that the password is invalid. 
If the password is correct, then the program should tell the user that they are now logged in to the system.
"""

user_dict = {
    "username1" : "abcd@123",
    "username2" : "efgh@123",
    "username3" : "ijkl@123",
    "username4" : "mnop@123",
    "username5" : "qrst@123",
    "username6" : "uvwx@123",
    "username7" : "yz12@123",
    "username8" : "ab34@123",
    "username9" : "cd56@123",
    "username10" : "ef78@123"
}
username = input ("Please enter your username : ")
password = input ("Please enter your password : ")
if username not in user_dict :
    print ("Invalid username")
else :
    if user_dict [username] == password :
        print ("You are now logged into the system.")
    else :
        print ("Invalid password.")