import contact_utils
import sys

contact = {}

def add_contact(name, age= 20, phone= "000-000-0000"):
    contact[name]= {"age":age, "phone" : phone}
    print (contact)
    return (contact)

def dispay_contact(contact):
    print(contact)

action = input("enter the action you want to perform: for eg. Add, View, Average or Exit :")

while (True):
    if action == "Add":
        contact_name = input("add contacts where key is name(str)")
        contact_age  = input("Add contact age(int)")
        contact_phone = input("Add contact phone(str)")
        if contact_age =="" and contact_phone =="":
            add_contact(contact_name)
        elif contact_age !="" and contact_phone =="":
            add_contact(contact_name, contact_age)
        elif contact_age =="" and contact_phone !="":
            add_contact(contact_name, contact_phone)
        else:
            add_contact(contact_name, contact_age, contact_phone)
        action = input("enter the action you want to perform: for eg. Add, View, Average or Exit :")
    elif action == "View":
        dispay_contact(contact)
        action = input("enter the action you want to perform: for eg. Add, View, Average or Exit :")
    elif action == "Average":
        print("average is:",contact_utils.avg_age(contact))
        action = input("enter the action you want to perform: for eg. Add, View, Average or Exit :")
    elif action == "Exit":
        sys.exit()
    else:
        print("please enter valid action")
        sys.exit()

    








