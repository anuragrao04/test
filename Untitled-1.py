dictionary_username_password = {}  #dictionary definition 
def go_to_mainpage():
    print('''                   ***SWEEP***                 
                        ***SELECT SERVICE***
    1. hair dressing
    2. bathroom cleaning 
    3. house cleaning 
    4. fan cleaning 
    5. idk whatever \U0001F602''')   
    choice = input()
while True: #infinite loop 
    print('''                   ***SWEEP***                     
    1. Create Account
    2. Login
    3. Exit''')
    choice = input()                #just the menu


    if choice == '1':                   #for creating an account 
        username = input("Enter Username/Email: ")
        password = input("Enter password: ")
        otp = input("Enter OTP: ")
        dictionary_username_password.update({username:password})     #to add username and password to the dictionary, add a print statement if you want to verify
        print("Welcome! login using the login option on the next page")


    elif choice == '2':                 #login 
        username = input("Enter Username/Email: ")
        
        if username in dictionary_username_password.keys():      #checking if username is in the dictionary. the .keys() function returns all the key values
            password = input("Enter password: ")
            if password == dictionary_username_password[username]:     #checking if the password matches the username 
                print("Welcome!")
                go_to_mainpage()
                break 

            else: 
                print("Wrong password!")
                break 
        else:
            print("Please create an account")                   #if username is not in the dictionary 
            break          
    elif choice == '3' or choice.lower() == "exit":             #exit 
        break
        






