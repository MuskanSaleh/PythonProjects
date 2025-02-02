#allow to encrypt text
from cryptography.fernet import Fernet

'''
def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key","rb")
    key1 = file.read()
    file.close()
    return key1

key1 = load_key()
fer = Fernet(key1)      

def view():
     with open('passwords.txt','r') as f:
         for line in f.readlines():
             data = line.rstrip()
             user,passw = data.split("|")
             print("User : ",user," | Password : ",fer.decrypt(passw.encode()).decode())
             
    
def add():
    name=input("account name:")
    pwd = input("Password : ")
    # it open the file and automatically close
    with open('passwords.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        
while True:
    mode = input("Would you like to add a new password or view or q for quite : ").lower()
    if mode == "q":
        break
    
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalide mode")
        continue
        
    
    