import contacts
def recharge(user):
    print("Mobile Recharge Online")
    num=input('Number:')
    if len(num)==10:
        print("Select Operator:\n"
              "1-Jio\n"
              "2-Airtel\n"
              "3-BSNL\n")
        choice=input()
        if choice=="1" or choice=="2" or choice=="3":
            amt=int(input("Enter amount to be paid:₹"))
            bill(user,num,amt,choice)
        else:
            print("Select from only those SIM")
            recharge(user)
    else:
        recharge(user)

def bill(user,num,amt,choice):
    print()
    sim={"1":"Jio","2":"Airtel","3":"BSNL"}
    print(sim[choice].center(20))
    print("Plan Amount :   ₹",amt)
    print("Processing Fee: ₹ 50")
    print("Total Amount:   ₹",amt+50)
    print()
    contacts.digit(user)
