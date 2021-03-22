dictionary_username_password = {}
while True:
    print('''                   ***SWEEP***         
    1. Create Account
    2. Login
    3. Exit''')
    choice = input()


    if choice == '1':
        username = input("Enter Username/Email: ")
        password = input("Enter password: ")
        otp = input("Enter OTP: ")
        dictionary_username_password.update({username:password})
        print("You're registered! please select login on the next screen and enter your credentials")

    elif choice == '2':
        username = input("Enter Username/Email: ")
        
        if username in dictionary_username_password.keys():
            password = input("Enter password: ")
            if password == dictionary_username_password[username]:
                print("Welcome!")
                break 

            else: 
                print("Wrong password!")
                break 
        else:
            print("Please create an account")
            break         
    elif choice == '3' or choice.lower() == "exit":
        break
        






