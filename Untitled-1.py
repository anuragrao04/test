def gotomainpage():
    print("You are now on the mainpage")
while True:
    print('''               ***SWEEP***         
    1. Create Account
    2. Login
    3. Exit''')
    choice = input()


    if choice == '1':
        username = input("Enter Username/Email: ")
        password = input("Enter password: ")
        otp = input("Enter OTP: ")
        print("Thank you")
        gotomainpage()

    elif choice == '2':
        username = input("Enter Username/Email: ")
        password = input("Enter password: ")
        print("Thank you")
        gotomainpage()

    elif choice == '3' or choice.lower() == 'exit':
        break




