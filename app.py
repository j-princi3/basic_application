import contacts,phone,cylinder
import login
print("WELCOME".center(150))
print("Rapid_pay".center(150))
print("Make your transaction fast , join us !".center(150))
def mainmenu():
    print("Enter 1 - SignIn"
          "      2 - Register"
          "      Press any key except 1,2 to Exit")
    choice=input()
    if choice=="1":
        x=login.signin()
        return x
    elif choice=="2":
        y=login.register()
        return y
    else:
        print("Thank you! Wish You Luck")
        exit()

def second(user):
    print("Enter 1-Pay to Contacts"
          "      2-Recharge"
          "      3-Book a Cylinder"
          "      4-SignOut"
          "      Press any key except 1,2,3,4 to Exit")
    cho=input()
    if cho=="1":
        contacts.pay_to_contact(user)
    elif cho=="2":
        phone.recharge(user)
    elif cho=="3":
        cylinder.book(user)
    elif cho=="4":
        user=mainmenu()
        second(user)
    else:
        print("Thank you! Wish You Luck")
user=mainmenu()
second(user)