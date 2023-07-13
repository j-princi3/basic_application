import json
import contacts
def book(user):
    print("Is your phone number registered with  cylinder- \n"
          "                                                          1-Yes\n"
          "                                                          0-No\n")
    yes=input()
    if yes=="1":
        already(user)
    elif yes=="0":
        notalready(user)
    else:
        print("Wrong input")
        book(user)


def already(user):
    with open ('registered.json','r') as file:
        dict=json.load(file)
    phone=input("Enter phone number              :")
    flag=0
    for i in dict:
        if i==phone:
            print("Gas                             :",dict[i][0])
            print("Cost of one cylinder            :₹",dict[i][1])
            no=int(input("No of cylinders you want        : "))
            print("Total amount to be paid         :₹",no*int(dict[i][1]))
            print()
            contacts.digit(user)
            flag=1
            break
    if flag==0:
        print("Number entered is wrong")
        already(user)
def notalready(user):
    cylinder={"1":["Indane",1149],"2":["HP",1179],"3":["Bharat",1139]}
    print("To register enter the number:")
    num=input()
    if len(num)==10:
        with open ("registered.json","r") as file:
            dic=json.load(file)
        print("Choose Gas company 1-Indane"
              "                   2-HP"
              "                   3-Bharat")
        gas=input()
        if gas=="1" or gas=="2" or gas=="3":
            dic[num]=[cylinder[gas][0],cylinder[gas][1]]
            with open("registered.json","w") as file:
                json.dump(dic,file)
                print()
            already(user)
        else:
            print("Invalid input")
            notalready(user)
    else:
        print("Number entered id wrong")
        notalready(user)
