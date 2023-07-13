import json

def signin():
    try:
        with open('user_details.json', 'r') as file:
            all_users = json.load(file)
    except FileNotFoundError:
        all_users = {}
    user_name=input("Enter the user name   :")
    flag1,flag2=1,1
    for j in all_users:
        if user_name==j:
            flag2=0
            password=input("Enter password        :")
            if password==all_users[user_name]["password"]:
                flag1=0
                print("You have successfully logIn")
                dic={j:all_users[j]}
                return dic
    if flag1==1 or flag2==1:
        print("Incorrect credentials")
        print()
        print("Enter   1-Want to register"
              "        2-Try again"
              "         Press any key except 1,2 to Exit")
        ch=int(input())
        if ch==2:
            user=signin()
            return user
        elif ch==1:
            user=register()
            return user
        else:
            print("Thank you! Wish You Luck")


def register():
    user={}
    with open('user_details.json','r') as file:
        all_user=json.load(file)
    dic={}
    name=input("Enter full name     : ")
    ph=input("Enter Phone number   :")
    if len(ph) == 10:
        for i in all_user:
            if all_user[i]["phone"]==ph:
                print("You're phone number was already registrated")
                print()
                print("---->try to SignIn ")
                p=signin()
                return p
            else:
                dic["phone"]=ph
    else:
        print("Number is wrong")
        print("---->Register")
        q=register()
        return q
    y=checking()
    dic["password"]=y
    z=pining()
    dic["pin"]=z
    x=username(all_user)
    all_user[x]=dic
    user[x]=dic
    with open('user_details.json', 'w') as file:
        json.dump(all_user,file)
        print("Registration was Successfull")
    return user


def pining():
    pin=input("Enter any 4-digit pin       :")
    if len(pin)==4:
        return pin
    else:
        print("---->Try again")
        pining()

def username(all_user):
    user_name=input("Enter User Name:")
    flag=1
    for j in all_user:
        if user_name==j:
            print("This userName already exist!")
            username(all_user)
            flag==0
            break
    if flag==1:
        return user_name


def checking():
    password=input("Enter password with atleast one number , capital letter, small letter and one amongst(@,$,*):")
    j=0
    flag_e=0
    flag_num=0
    flag_az=0
    flag_za=0
    while j<len(password):
        k=password[j]
        i=ord(password[j])
        if k=="*" or k=="$" or k== "@":
            flag_e=1
            j+=1
        elif i>=48 and i<=57:
            flag_num=1
            j+=1
        elif i>=65 and i<=90:
            flag_az=1
            j+=1
        elif i>=97 and i<=122:
            flag_za=1
            j+=1
        else:
           flag_e=0
           print("*,$,@ are only allowed")
           print("---->Try again")
           checking()
    if flag_e==1 and flag_za==1 and flag_az==1 and flag_num==1:
        return password
    else:
        print("---->try again")
        checking()
