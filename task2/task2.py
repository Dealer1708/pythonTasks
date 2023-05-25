import json
import re


num_pattern = re.compile(r'(\+374|0).*?(\d{2,3}).*?(\d{2,3}).*?(\d{2}).*?(\d{2})')
mail_patten = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def data_file_r():
    with open("files/data.json", "r") as file:
        data_file = json.load(file) # dict
        return data_file

def dump(data):
    with open("files/data.json", "w") as f:
        json.dump(data, f, indent= 3)

def start():
    action = input(" 1 - add contact \n 2 - change contact \n 3 - delete contact \n >>> ")
    if int(action) == 1:
        add_contact()
    elif int(action) == 2:
        change_contact()

    elif int(action) == 3:
        delete_contact()

    else: start()
    
def add_contact():
    data_file = data_file_r()
    items = {}
    str_data = """{"data": {"count": 0, "items": {}}}"""
    dict_data = json.loads(str_data)
    number = input(" Phone number >>> ")


    if re.match(num_pattern, number):

        phone_number = fit_number(number)

        if phone_number in list(data_file["data"]["items"]):
            print("\n <<<Phone number already exists>>> \n")
            start()

        

        contact_name = input(" Name >>> ")
        email = None

        while True:        
            ask_email = input("\n Add email? y/n>>> \n\n >>>")
            if ask_email == "y":
                email = add_email()
                break
            elif ask_email == "n":
                break


        items.update({phone_number: {"contact_name": contact_name, "phone_number": phone_number, "email": email}})
        dict_data["data"]["items"].update(items)
        
        data_file["data"]["items"].update(items)
        count_key = {"count": len(list(data_file["data"]["items"]))}
        data_file["data"].update(count_key)
        dump(data_file)
        start()
    else:
        print("Invalid phone number")
        start()
        
def change_contact():
    contact_number = input(" Type 'Exit' or 'e' to go back \n Phone number of the contact >>> ")

    data_file = data_file_r()

    phone_number = fit_number(contact_number)


    if phone_number in ["exit","Exit","e","E"]:
        start()
    elif phone_number in list(data_file["data"]["items"]):
        action = input(" 1 - change phone number \n 2 - change name \n 3 - change email \n>>> ")

        if int(action) == 1:
            change_num(phone_number)
        elif int(action) == 2:
            change_name(phone_number) 
        elif int(action) == 3:
            change_email(phone_number)

    else: 
        print("\n <<<Not Found>>> \n")
        change_contact()

def delete_contact():
    contact_number = input(" Type 'Exit' or 'e' to go back \n Phone number of the contact >>> ")
    data_file = data_file_r()

    if contact_number in ["exit","Exit","e","E"]:
        start()

    phone_number = fit_number(contact_number)



    if phone_number in list(data_file["data"]["items"]):
        del data_file["data"]["items"][phone_number]
        count_key = {"count": len(list(data_file["data"]["items"]))}
        data_file["data"].update(count_key)
        dump(data_file)
        start()

        
    else: 
        print("\n <<<Not Found>>> \n")
        delete_contact()


def change_num(number):
    data_file = data_file_r()

    new_number = input(" New number >>> ")
    
    if re.match(num_pattern, new_number):

        phone_number = fit_number(new_number)


        data_file["data"]["items"][number]["phone_number"] = phone_number
        data_file["data"]["items"][phone_number] = data_file["data"]["items"].pop(number)
        dump(data_file)
        start()
    else:
        print("Invalid phone number")
        change_num(number)

    
def change_name(number):
    data_file = data_file_r()
    new_name = input("New name >>> ")
    data_file["data"]["items"][number]["contact_name"] = new_name
    dump(data_file)
    start()

def add_email():
    while True:
        email = input(" Email >>> ")
        if re.fullmatch(mail_patten, email):
            break
        else:
            print("Invalid email")
    return str(email)
    
def change_email(number):
    data_file = data_file_r()
    new_email = add_email()
    data_file["data"]["items"][number]["email"] = new_email
    dump(data_file)
    start()

def fit_number(number):
    if number[0:4] == "+374":
        phone_number = "0" + number[4::]
        return phone_number
    elif number[0] == "0":
        return number



start()


