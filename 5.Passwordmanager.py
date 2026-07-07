from cryptography.fernet import Fernet
pwd=input("What is the master password? ")

# def write_key():
#     key=Fernet.generate_key()
#     with open("5.key.key", "wb") as f:
#         f.write(key)
# write_key()

# def load_key():
#     file=open("5.key.key", "rb")
#     key=file.read()
#     file.close()
#     return key
# key=load_key()+pwd.encode()
# fer=Fernet(key)

def view():
    with open("5.passwords.txt", "r") as f:
        for line in f.readlines():
            data=line.rstrip()
            user, passw=data.split("|")
            print("Account:", user, "| Password:", passw)

def add():
    name=input("Account Name: ")
    pwd=input("Password: ")
    with open("5.passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")

def delete():
    name=input("Account Name: ")
    with open("5.passwords.txt", "r") as f:
        lines=f.readlines()
    with open("5.passwords.txt", "w") as f:
        for line in lines:
            data=line.rstrip()
            user, passw=data.split("|")
            if user != name:
                f.write(line)

while True:
    mode=input("Would you like to view, add,delete the passwords or quit? ").lower()
    if mode=="q":
        break

    if mode=="view":
        view()
    elif mode=="delete":
        delete()
    elif mode=="add":
        add()
    else:
        print("Invalid mode.")