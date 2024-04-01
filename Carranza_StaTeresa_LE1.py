import os

game_library ={
    1:{"Donkey Kong": 3}, 
    2:{"Super Mario Bros" : 5}, 
    3:{"Tetris" : 2}
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
                menu() 
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
    while True:
        try:
            print(f"Logged in as "[username])
            print("1. Rent a game")
            print("2. Return a game")
            print("3. Top-up Account")
            print("4. Display inventory")
            print("5. Redeem free game rental")
            print("6. Check Points")
            print("7. Log out")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                rent_game(username)
            if choice == "2":
                return_game(username)
            if choice == "3":
                top_up(username)
            if choice == "4":
                inventory(username)
            if choice == "5":
                redeem(username)
            if choice == "6":
                check_point(username)
            if choice == "7":
                print("Logging out...Goodbye!")
                menu()
            else:
                print("Please input an option")
                break
        except ValueError:
            print("Wrong input")
            return
    
def rent_game(username):
    print(game_library.keys)
def return_game(username):
    pass
def top_up(username):
    pass
def inventory(username):
    pass
def redeem(username):
    pass
def check_point(username):
    pass

def admin_menu():
    while True:
        try:
            print("Admin Menu") 
            print("1. Update Game Details")
            print("2. Log out")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                update_menu()
            if choice == "2":
                print("Logging out...Goodbye!")
                menu()
            else:
                print("Please input an option")
                break
        except ValueError:
            print("Wrong input")
            return
        
def update_menu():
    pass
        
        
        
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
            