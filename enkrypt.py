import mysql.connector
from email_validator import validate_email, EmailNotValidError
import phonenumbers
from cryptography.fernet import Fernet
import base64



#Function to encrypt data
def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

# Function to decrypt data
def decrypt_data(data, key):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(data)
    decryption_balance = int(decrypted_data.decode()) 
    return decryption_balance


def decryption():
    print("==================YOUR-BALANCE====================\n")
    name = input("ENTER YOUR NAME: ")
  
    
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="Ramdevi#2", port=3306, database="testdb")
        mycursor = mydb.cursor()
        query = "SELECT Balance FROM `user_info` WHERE Name = %s"
        mycursor.execute(query, (name,))
        encrypted_balance = mycursor.fetchone()[0]
        pin = input("ENTER YOUR KEY: ")

        if len(pin) != 4 or not pin.isdigit():
            print("Invalid PIN format. Please enter a 4-digit PIN.")
            return
        
        encryption_key = base64.urlsafe_b64encode(pin.zfill(32).encode())
        decrypted_balance = decrypt_data(encrypted_balance, encryption_key)
        
        print("YOUR CURRENT BALANCE : ", decrypted_balance)
        print("======================================\n")
    except Exception as e:
        print(encrypted_balance,"(ENCRIPTED...)")
        print("\n===================================")
    function()
        
    
     

def deposit():
    print("==================DEPOSIT====================\n")
    name = input("ENTER YOUR NAME: ")
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="Ramdevi#2", port=3306, database="testdb")
        mycursor = mydb.cursor()
        query = "SELECT Balance FROM `user_info` WHERE Name = %s"
        mycursor.execute(query, (name,))
        encrypted_balance = mycursor.fetchone()[0]
        pin = input("ENTER YOUR KEY: ")

        if len(pin) != 4 or not pin.isdigit():
            print("Invalid PIN format. Please enter a 4-digit PIN.")
            return
        
        encryption_key = base64.urlsafe_b64encode(pin.zfill(32).encode())
        decrypted_balance = decrypt_data(encrypted_balance, encryption_key)
        
        amount = int(input("ENTER THE AMOUNT DO YOU WANT TO DEPOSIT: "))
        ac_num = int(input("ENTER YOUR ACCOUNT NUMBER: "))
        
        current_balance = decrypted_balance
        updated_balance = current_balance + amount

        encryption_key_input = input("Enter a 4-digit PIN for encryption: ")
        
        if len(encryption_key_input) != 4 or not encryption_key_input.isdigit():
            print("Invalid PIN format. Please enter a 4-digit PIN.")
            return
        
        # Pad the PIN and convert to a valid Fernet key
        encryption_key = base64.urlsafe_b64encode(encryption_key_input.zfill(32).encode())
        encrypted_updated_balance = encrypt_data(str(updated_balance), encryption_key)
        
        mycursor.execute("use testdb")
        
        update_query = "UPDATE user_info SET Balance = %s WHERE Account_number = %s"
        mycursor.execute(update_query, (encrypted_updated_balance, ac_num))
        
        mydb.commit()
        
        print("__________________________________________\n")
        print("DEAR USER, YOU CREDITED BY RS.", amount)
        print("__________________________________________")
        
        mycursor.close()
        mydb.close()
    except Exception as e:
        print("ENTER VALID KEY..YOU CAN'T DEPOSIT NOW..")
        print("\n===================================")
    function()


def withdraw():
    print("==================WITHDRAW====================\n")
    name = input("ENTER YOUR NAME: ")
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="Ramdevi#2", port=3306, database="testdb")
        mycursor = mydb.cursor()
        query = "SELECT Balance FROM `user_info` WHERE Name = %s"
        mycursor.execute(query, (name,))
        encrypted_balance = mycursor.fetchone()[0]
        pin = input("ENTER YOUR KEY: ")
        if len(pin) != 4 or not pin.isdigit():
            print("Invalid PIN format. Please enter a 4-digit PIN.")
            return
        
        encryption_key = base64.urlsafe_b64encode(pin.zfill(32).encode())
        decrypted_balance = decrypt_data(encrypted_balance, encryption_key)

        amount = int(input("ENTER THE AMOUNT DO YOU WANT TO WITHDRAW: "))
        ac_num = int(input("ENTER YOUR ACCOUNT NUMBER: "))
        
        current_balance = decrypted_balance
        updated_balance = current_balance - amount

        encryption_key_input = input("Enter a 4-digit PIN for encryption: ")
        
        if len(encryption_key_input) != 4 or not encryption_key_input.isdigit():
            print("Invalid PIN format. Please enter a 4-digit PIN.")
            return
        
        # Pad the PIN and convert to a valid Fernet key
        encryption_key = base64.urlsafe_b64encode(encryption_key_input.zfill(32).encode())
        encrypted_updated_balance = encrypt_data(str(updated_balance), encryption_key)
        
        mycursor.execute("use testdb")
        
        update_query = "UPDATE user_info SET Balance = %s WHERE Account_number = %s"
        mycursor.execute(update_query, (encrypted_updated_balance, ac_num))
        
        mydb.commit()
        
        print("__________________________________________\n")
        print("DEAR USER, YOU DEBITED BY RS.", amount)
        print("__________________________________________")
    except Exception as e:
        print("ENTER VALID KEY...YOU CAN'T WITHDRAW NOW..")
        print("\n===================================")
    function()
        



def function():
    choice=int(input("ENTER THE OPERATION DO YOU WANT TO PERFORM...\n 1.DEPOSIT \n 2.WITHDRAWL\n 3.CHECK BALANCE \nENTER YOUR CHOICE.... :)"))
    if choice==1:
        deposit()
    elif choice==2:
        withdraw()
    elif choice==3:
        decryption()
    else:
        print("PLEASE ENTER VALID CHOICE : ")
        function()





def signup():
    while(True):
        print("==================LET'S START====================\n")
        name = input("ENTER YOUR NAME: ")
        try:
            email = input("ENTER YOUR E MAIL: ")
            valid = validate_email(email)
            if valid:
                print(" ✔️ VALID EMAIL ✔️ ")
            
            try:
                ph_num = input("ENTER YOUR PHONE NUMBER: ")
                parsed_number = phonenumbers.parse(ph_num, None)
                if phonenumbers.is_valid_number(parsed_number):
                    print(f"{ph_num} IS A VALID MOBILE NUMBER ✔️")
                # else:
                #     print(f"{ph_num} IS NOT A VALID MOBILE NUMBER ❌")
                #     break
                
                ac_num = int(input("ENTER YOUR ACCOUNT NUMBER: "))
                encryption_key_input = input("Enter a 4-digit PIN for encryption: ")
                balance = int(input("ENTER YOUR ACCOUNT BALANCE: "))
                password = input("ENTER YOUR PASSWORD: ")
                concat = name + password
                
                if len(encryption_key_input) != 4 or not encryption_key_input.isdigit():
                    print("Invalid PIN format. Please enter a 4-digit PIN.")
                    signup()
                    return
                    
                
                
                # Pad the PIN and convert to a valid Fernet key
                encryption_key = base64.urlsafe_b64encode(encryption_key_input.zfill(32).encode())

                encrypted_balance = encrypt_data(str(balance), encryption_key)

                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Ramdevi#2",
                    port=3306,
                    database="testdb"
                )

                cursorsign = mydb.cursor()
                cursorsign.execute("use testdb")
                
                try:
                    cursorsign.execute("insert into user_info(name_password, Account_number,Balance, Name, Email, Ph_num) values (%s, %s, %s, %s, %s, %s)", (concat, ac_num, encrypted_balance, name, email, ph_num))
                    mydb.commit()
                    print("YOU REGISTERED SUCCESSFULLY")
                    function()
                except Exception as e:
                    if "Duplicate entry" in str(e):
                        print("ERROR: Duplicate entry. User already exists.")
                    else:
                        print("An error occurred:", e)

                cursorsign.close()
                mydb.close()
                break
            except phonenumbers.NumberParseException:
                print(f"{ph_num} IS NOT A VALID MOBILE NUMBER ❌")
        except Exception as e:
            print(f"{email} is not Valid ❌")
            print("PLEASE ENTER A VALID EMAIL ADDRESS")
def login():
    
    name = input("ENTER YOUR NAME: ")
    password = input("ENTER YOUR PASSWORD: ")
    concat = (name + password)
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ramdevi#2",
        port=3306,
        database="testdb"
    )

    cursorsign = mydb.cursor()
    cursorsign.execute("use testdb")
    
    try:
        cursorsign.execute("select * from user_info where name_password = %s", ((concat),))
        user_data = cursorsign.fetchone()
        if user_data:
            print("LOGIN SUCCESSFUL")
            function()
        else:
            print("LOGIN FAILED")
            
            print("SIGN UP TO CONTINUE.. :)")
            print("===================================")
            signup()
    except Exception as e:
        print("An error occurred:", e)

    cursorsign.close()
    mydb.close()


def main():
    print("HEY THERE WELCOME BACK....")
    choice = int(input(" 1.SIGN UP\n 2.LOGIN\nENTER YOUR CHOICE: "))

    if choice == 1:
        signup()
    elif choice==2:
        login()
    else:
        print("PLEASE ENTER VALID CHOICE :( ")

main()

