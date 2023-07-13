import json
def pay_to_contact(user):
    print("Enter 1-pay My contacts:"
          "      2-dial a number which is not saved in my contact list"
          "      press any key except 1,2 to Exit")
    i=input()
    if i=="1":
        saved(user)
    elif i=="2":
        dial(user)
    else:
        print("Thank you! Wish You Luck")
        exit()
def saved(user):
    try:
        with open('mycontacts.json', 'r') as file:
            dic= json.load(file)
        
    except FileNotFoundError:
        dic={} 
    max_column=0
    for j in dic:
        if len(j)>max_column:
            max_column=len(j)
    max_row=len("Name"+" "*(max_column-4)+"|  "+"Phone Number")+3
    for i in dic:
        print("-"*max_row)
        print(i," "*(max_column-len(i)),"|  ",dic[i])
    num=input("Input phone number to whom you want to pay:")
    flag=0
    for i in dic:
        if dic[i]==num:
            print("Name:",i)
            rupee=input("Amount to be paid = ₹")
            flag=1
            digit(user)
    if flag==0:
        print("Number is incorrect")
        print()
        print("---->Try again")
        saved(user)
def dial(user):
    print("Input number below the Num pad:")
    num_pad=[["【７】","【８】","【９】"],["【４】","【５】","【６】"],["【１】","【２】","【３】"]]
    for i in num_pad:
        for j in i:
            print(j,end=" ")
        print()
    print("_"*20)
    print(" "*5,end="")
    phone=input()
    if len(phone)==10 :
        name=input("if you want to save phone number for future use ,please enter the Name of reciever else press only Enter key:")
        if name!="":
            with open('mycontacts.json','r') as files:
                dic=json.load(files)
            dic[name]=phone
            with open('mycontacts.json', 'w') as file:
                json.dump(dic,file)
            rupee=input("Amount to be paid = ₹")
            digit(user)
        else:
            rupee=input("Amount to be paid = ₹")
            digit(user)
    else:
        print("Number is wrong")
        print()
        print("---->Try again")
        dial(user)
def digit(user):
    pin=input("Input the 4-digit pin :")
    for i in user:
        if pin ==  user[i]["pin"]:
            print("Payment was Successful!")
            print("Thank you! Wish You Luck")
        else:
            print("pin is incorrect")
            print("---->Try again")
            print()
            digit(user)
