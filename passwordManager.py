from dataclasses import dataclass
# from saveFile import save, load
from pickle import loads, dumps
from requests import get
from random import randint, choice
from Encryption import Encrypt


@dataclass
class Account():
    Tag: str
    Username: str
    Password: list[str]
    Url: str

@dataclass
class Category():
    Title: str
    Accounts: list[Account]

class Password_Manager():
    def __init__(self):
        self.categories = []
        General = Category("General", [])
        Recently_Deleted = Category("Recently Deleted", [])
        self.categories.append(General)
        self.categories.append(Recently_Deleted)
        self.duplicates = 0 

    def add_category(self, title):
        new_category = Category(title, [])
        self.categories.append(new_category)
        print(self.categories)

    def edit_category(self, title, index):           
        self.categories[index].Title = title  
        print(self.categories) 
                

    def del_category(self, index):
        for account in self.categories[index].Accounts:
            self.categories[1].Accounts.append(account)
            self.categories[index].Accounts.remove(account)
        self.categories.pop(index)
        print(self.categories)

    def relocate(self, category_index, tag):
        account_index = self.get_account_index(1, tag)
        temp = self.categories[1].Accounts[account_index]
        self.categories[1].Accounts.pop(account_index)
        self.categories[category_index].Accounts.append(temp)


    def add_account(self, category_index, tag, username, password, url):
        new_account = Account(tag, username, [], url)
        try:
            self.check_duplicate_tags(tag)
            self.categories[category_index].Accounts.append(new_account)
            account_index = self.get_account_index(category_index, tag)
            self.categories[category_index].Accounts[account_index].Password.append(password)
        except:
            raise Exception()

    def check_duplicate_tags(self, tag, category_index=-1, acc_index=-1):
        for i in range(len(self.categories)):
            for j in range(len(self.categories[i].Accounts)):
                if category_index == i and acc_index == j:
                    continue
                elif self.categories[i].Accounts[j].Tag == tag:
                    raise Exception()

    def get_account_index(self, category_index, tag):
        for i in range(len(self.categories[category_index].Accounts)):
            if self.categories[category_index].Accounts[i].Tag == tag:
                return i

    def del_account(self, category_index, tag):
        account_index = self.get_account_index(category_index, tag)
        account = self.categories[category_index].Accounts[account_index]

        if category_index == 1:
            pass
        else:
            self.categories[1].Accounts.append(account)
        self.categories[category_index].Accounts.remove(account) 
        
    
    def edit_account(self, category_index, old_tag, new_tag, username, password, url): 
        account_index = self.get_account_index(category_index, old_tag)
        try:
            self.check_duplicate_tags(new_tag, category_index, account_index)
            self.categories[category_index].Accounts[account_index].Tag = new_tag
            self.categories[category_index].Accounts[account_index].Username = username
            self.append_to_passwords(password, category_index, account_index)
            self.categories[category_index].Accounts[account_index].Url = url
            print(self.categories)
        except:
            raise Exception()


    def append_to_passwords(self, new_password, category_index, acc_index):
        for password in self.categories[category_index].Accounts[acc_index].Password:
            if password == new_password:
                self.categories[category_index].Accounts[acc_index].Password.remove(password)
        self.categories[category_index].Accounts[acc_index].Password.append(new_password)

            
    def generate(self, include, length, symbols):
        password = ""
        letters= 'abcdefghijklmnopqrstuvwxyz'
        upperletters = letters.upper()

        for i in range(int(length)):
            type = choice(include)
            if type == 0:
                charecter = choice(symbols)
                password += charecter
            if type == 1:
                charecter = choice(upperletters)
                password += charecter
            if type == 2:
                charecter = str(randint(0,9))
                password += charecter 
            if type == 3:
                charecter = choice(letters)
                password += charecter
        return password

    def save_as(self, path, masterpassword):
        buffer = dumps(self)
        key = Encrypt(masterpassword)
        encypted_data = key.encrypt(buffer)

        f = open(path, 'wb')
        f.write(encypted_data)
        f.close()

    def Open(self, path, masterpassword):
        file = open(path, 'rb')
        buffer = file.read()
        file.close()

        key = Encrypt(masterpassword)

        try:
            decrypted_file = key.decrypt(buffer)

            openedobj = loads(decrypted_file)
            return openedobj
        except:
            raise Exception

    def import_Url_file(self, Url, masterpassword):
        encrypted_link = get(Url)
        buffer = encrypted_link.content

        key = Encrypt(masterpassword)
        try:
            decrypted_file = key.decrypt(buffer)

            if decrypted_file == False:
                return False

            open_object = loads(decrypted_file)
            return open_object
        except:
            raise Exception
        

    def save(self, path, masterpassword):
        buffer = dumps(self)

        key = Encrypt(masterpassword)
        encypted_data = key.encrypt(buffer)

        f = open(path, 'wb')
        f.write(encypted_data)
        f.close()

    def __del__ (self):
        print(self.categories)

    def theme_prefrences(self, mode):
        f = open("Theme","w")
        f.write(mode)
        f.close()

    def check_theme_prefrences(self):
        theme = open("Theme","r")
        Theme_mode = theme.read()
        theme.close()
        if Theme_mode == "DarkMode":
            return 1
        elif Theme_mode == "DefultMode":
            return 0




