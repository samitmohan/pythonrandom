# usernamelogin

def admin():
    username = raw_input("Enter Admin Name : ")
    usernames_acceptable = ('samit', 'mihica')             # convert all to lower char
    if username in usernames_acceptable:
        print("Welcome")
        def password_login():
            if username == 'samit':
                password = raw_input("Enter Password : ")
                passwords = {"samit" : "samitmohan123", "mihica" : "mmihica08"}
                for key, value in passwords.items(): 
                    if password == value: 
                        print("You're logged in")
                        break
                else:
                    print("Wrong password")
                    hint = "name+number"
                    print("Hint : ", hint)
                    password_login()
                                                                 
            else:
                password2 = raw_input("Enter Password : ")
                passwords = {"samit" : "samitmohan123", "mihica" : "mmihica08"}
                for key, value in passwords.items(): 
                    if password2 == value: 
                        print("You're logged in")
                        break
                else:
                    print("Wrong password")
                    hint = "name+number"
                    print("Hint : ", hint) 
                    password_login() 

        password_login()
    else:
        print("Can't recognise admin, try again.")
        admin()
    

admin()
