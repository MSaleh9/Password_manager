from cryptography.fernet import Fernet

'''
def write_key() : 
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file : 
        key_file.write(key)
'''

def load_key():
    with open("key.key","rb") as f_key:
        return f_key.read()
        
def show():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            acc_domain, acc_id, acc_pw = line.rstrip().split("|")
            print(f"domain: {acc_domain}, ID: {acc_id}, PW: {Fernet(load_key()).decrypt(acc_pw.encode()).decode()} .")

def add():
    domain = input("domain: ")
    id = input("Account id: ")
    pwd = input("Password: ")
    pwd = Fernet(load_key()).encrypt(pwd.encode()).decode()
    with open('passwords.txt', 'a') as f:
        f.write(domain + "|" + id + "|" + pwd + "\n")

def main():
    # creating a key : run this once : write_key()
    while True :
        mode = input("would you add or show passwords ?(add or show) or (q) to quit: ").lower()
        if mode == "q" :
            break
        if mode == "add":
            add() 
        elif mode == "show":
            show() 
        else :
            print("ivalid input")
            continue


if __name__ == "__main__":
    main()