import os

game_library ={
    "Donkey Kong": 3, "Super Mario Bros" : 5, "Tetris" : 2
}

game_lib = {}
acc_lib = {}


def Avail_games():
    pass


def register():
    try:
        print("REGISTER PAGE")
        print("Please input information")
        username = str(input("Please input username"))
        if username in acc_lib:
            print("Username already existing")
            return
        else:
            continue
        password = str(input("Password (must be 8 characters long)"))
        if len(password) >= 8:
            print("Account registered succesfully")
        else:
            print("Password must be atleast 8 characters long")
            return
        
        userbalance = 0
        userpoints = 0
        
        acc_lib[username] = {
            "username": username,
            "password": password,
            "Balance": userbalance,
            "Points": userpoints
        }
    except ValueError:
        print("Wrong input")
        input()
        
def userlogin():
    pass
      
    
def adminlogin():
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
                break
            else:
                print("Please input an option")
                return
        except ValueError:
            print("Wrong input")
            return
            