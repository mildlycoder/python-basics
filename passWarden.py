from cryptography.fernet import Fernet

master_pwd = input("enter the master password ")

def view():
    with open("storage.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            accnt, pwd = data.split(" | ")
            print(f"{accnt} {pwd}")


def add():
    name = input("enter the the acconut ")
    pwd = input("enter the password ")

    with open("storage.txt", 'a') as f:
        f.write(f"{name} | {pwd}\n")

while True:
    choice = input("enter the choice(enter q to quit) \n a.view b.add ").lower()
    
    if choice == "q":
        break
    
    if choice == "a":
        view()
        break
    elif choice == "b":
        add()
        break
    else:
        print("enter a valid choice")