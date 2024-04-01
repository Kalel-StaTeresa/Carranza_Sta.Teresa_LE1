import os

game_library ={
    "Donkey Kong": 3, "Super Mario Bros" : 5, "Tetris" : 2
}



game_lib = {}
acc_lib = {}


def Avail_games():
    pass


def register():
    while True:
        try:
            print("REGISTER PAGE")
            print("Please input information")
            username = str(input("Please input username: "))
            password = str(input("Password (must be 8 characters long): "))
            if len(password) >= 8:
                print("Account registered succesfully")
                userbalance = 0
                userpoints = 0
                
                acc_lib[username] = {
                    "username": username,
                    "password": password,
                    "Balance": userbalance,
                    "Points": userpoints
                    } 
                return menu() 
            else:
                print("Password must be atleast 8 characters long")
                break   
        except ValueError:
            print("Wrong input")
            input()
            return
        
def userlogin():
    while True:
        try:
            print("LOGIN PAGE")
            username = str(input("Username: "))
            password = str(input("Password: "))
            if username and password not in acc_lib:
                print("User does not exist.")
                break
            else:
                print("Login Successful")
                user_menu()
        except ValueError:
            print("Wrong input")
            input()
            return
        
def adminlogin():
    while True:
        try:
            print("ADMIN LOGIN PAGE")
            admin = str(input("Username: "))
            if admin == "admin":
                print("Incorrect Username")
                break
            else:
                adminpass = str(input("Password: "))
                if adminpass == "adminpass":
                    print("Incorrect password")
                else:
                    print("Login Successful")
                    admin_menu()
        except ValueError:
            print("Wrong input")
            input()
            return

def user_menu(username):
    pass

def admin_menu():
    
        
        
        
def menu():
    while True:
        try:
            print("Welcome to the Game Rental System")
            print("1. Display Available Games")
            print("2. Register User")
            print("3. Log in")
            print("4. Admin Log in")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                Avail_games()
            if choice == "2":
                register()
            if choice == "3":
                userlogin()
            if choice == "4":
                adminlogin()
            if choice == "5":
                print("Closing app...Goodbye!")
                return
            else:
                print("Please input an option")
                break
        except ValueError:
            print("Wrong input")
            return
menu()
            