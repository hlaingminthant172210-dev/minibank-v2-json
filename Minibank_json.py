import sys
import json
class MiniBank:

    def firstOption(self):
        choose_input = int(input("Press 1 to register\nPress 2 to login\nPress 3 to exit\n"))
        if choose_input == 1:
            self.register()
        elif choose_input == 2:
            self.login()
        elif choose_input == 3:
            self.exit()
        else:
            print("<< Invalid option. Please choose again. >>")
            self.firstOption()

    def register(self):
        while True:
            print("\n___________Welcome to MiniBank_________\n")
            r_username:str =input("Enter your r_username: ")
            exist=self.exist_rUser(r_username)
            if exist:
                print("<< Username already exists. Please choose another. >>")
                continue
            if not r_username.isalpha() or len(r_username)>10: 
                print("<< Please enter only letters (A-Z). Maximum 10 characters allowed. >>")
                continue #re-enter username 
            
            break

        while True:
            r_password1=input("Enter your r_password1: ")
            r_password2=input("Enter your r_password2: ")
            if (r_password1 != r_password2):
                print("Incorrect Password")
                continue #re-enter password

            else:
                break #password correct ->go to amount
        while True:
            r_amount = input("Enter your r_amount: ")

            if not r_amount.isdigit():
                print("<< Please enter numbers only >>")
                continue

            r_amount = int(r_amount)

            if r_amount < 1000:
                print("<< Minimum registration amount is 1000 >>")
                continue            
            break
        try:
            with open("all_user_info.json",'r') as jfile:
                all_user_info=json.load(jfile)
        except:
            all_user_info={}

        id=str(len(all_user_info)+1)
        all_user_info[id]={"name":r_username,"password":r_password1,"amount":r_amount}

        with open("all_user_info.json",'w') as file:
            json.dump(all_user_info,file)



    def login(self):
        print("\n___________This is Login_________\n")
        l_username=input("Please login your name : ")
        l_password=input("Please enter your login password : ")
        exist_User=self.existUser(l_username,l_password)
        if exist_User:
            print("Login Successful")
            current_user=self.userID(l_username)
            print("Login User",current_user)
            self.menu(current_user)
        else:
            print("User Not Found")

    
    def menu(self,current_user):
        while True:
            choose_menu = int(input("Press 1 to Transfer\nPress 2 to Withdraw\nPress 3 to Update\nPress 4 to exit\n"))
            if choose_menu == 1:
                self.transferMoney(current_user)

            if choose_menu == 2:

                self.withdrawMoney(current_user)
                
            if choose_menu == 3:
                self.updateInfo(current_user)

            if choose_menu == 4:
                self.exit()

            else:
                print("<< Invalid option. Please choose again. >>")
                continue
                


    def userID(self,l_username):
        with open("all_user_info.json",'r') as file:
            data=json.load(file)
            for id in data:
                if (data[id]["name"]==l_username):
                    return id
            return None

    def current_userID(self,transfer_username,current_user):
        with open("all_user_info.json",'r') as file:
            data=json.load(file)
            if(data[current_user]["name"]==transfer_username):
                return None
            return True

    def existUser(self,l_username,l_passwrod):
        with open("all_user_info.json",'r') as file:
            data=json.load(file)

            for id in data:
                if(data[id]["name"]==l_username and data[id]["password"]==l_passwrod):
                    return True
            return False
    
    def exist_rUser(self, r_username):
        try:
            with open("all_user_info.json", "r") as file:
                data = json.load(file)
        except:
            # If file does not exist, is empty, or contains invalid JSON
            data = {}

        for user_id in data:
            if data[user_id]["name"] == r_username:
                return True

        return False

    def transferMoney(self,current_user):
        with open("all_user_info.json",'r') as file:
            data=json.load(file)
            while True:
                    transfer_userName=input("Please enter transfer username : ")
                    transferUser=self.userID(transfer_userName)
                    currentUser=self.current_userID(transfer_userName,current_user)

                    if transferUser is None or currentUser is None:
                        print("<< Invalid user or self-transfer is not allowed. >>")
                        continue

                    else:
                        print("Transfer to ", transferUser)
                        break
            while True:
                transfer_amount = input("Please enter transfer amount :")
                if not transfer_amount.isdigit():
                    print("<< Enter digit number >>")
                    continue
                transfer_amount=int(transfer_amount)
                if(data[current_user]["amount"]>=transfer_amount):
                    data[current_user]["amount"]-=transfer_amount
                    data[transferUser]["amount"]+=transfer_amount
                    with open("all_user_info.json",'w') as file:
                        json.dump(data,file)

                    print("Transfer amount :",transfer_amount)
                    print("Remaining amount :",data[current_user]["amount"])
                    break
            
                else:
                    print("<< Not enough money >>")
    
    

    def withdrawMoney(self,current_user):
        with open("all_user_info.json",'r') as file:
            data=json.load(file)

        while True:
            withdraw_amount=input("Enter your withdraw amount : ")
            if not withdraw_amount.isdigit():
                print("<<Enter digit >>")
                continue
            withdraw_amount=int(withdraw_amount)
            if(data[current_user]["amount"])>=withdraw_amount:
                data[current_user]["amount"]-=withdraw_amount
                with open("all_user_info.json",'w') as file:
                    json.dump(data,file)
                
                print("Withdraw Successfully!")
                print("Remaining amount : ",data[current_user]["amount"])
                break
                
            else:
                print("<< Not enough money >>")
                break

    def updateInfo(self,current_user):
        with open("all_user_info.json",'r') as file:
            data=json.load(file)

        choose_update=int(input("Press 1 to update username\nPress 2 to update password\nPress 3 to add amount\n"))
        if(choose_update == 1):
            while True:
                update_username=input("Enter your update username : ")
                if not update_username.isalpha():
                    print("<< Enter only letters(A-Z) >>")
                    continue
                else:
                    data[current_user]["name"]=update_username
                    print("<< Updated Successfully! >>")
                    break


        if(choose_update == 2):
            while True:
                update_password=input("Enter your update password : ")
                if not update_password.isdigit():
                    print("<<Enter digit numbers >>")
                    continue
                else:
                    data[current_user]["password"]=update_password
                    print("<< Updated Successfully! >>")
                    break

        if(choose_update == 3):
            while True:
                update_amount = input("Enter your update amount : ")
                if not update_amount.isdigit():
                    print("<< Enter digit numbers >>")
                    continue
                update_amount=int(update_amount)
                data[current_user]["amount"]+=update_amount
                print("<< Updated Successfully! >>")
                break
        
        with open("all_user_info.json",'w') as file:
            json.dump(data,file)
    
    def exit(self):
        print("<< Exiting the program. Goodbye! >>")
        sys.exit()

if __name__ == '__main__':
    minibank:MiniBank = MiniBank()
    while True:
        minibank.firstOption()