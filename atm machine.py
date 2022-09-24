Atm machine
flag = 0
pinentered = 0
balance = int(1500)
pinentered = input("whats your pin\n")
while pinentered == '1234':
    print("welcome tristan")
    withdraw = input("how much would you like to withdraw\n")
    if str(withdraw) > str(balance):
        print("withdraw amount is more than your balance\n")
    if str(withdraw) < str(balance):
        print("your balance remaining is " + str(int(balance) - int(withdraw)) + "$")
        print("check cash slot for your " + str(int(withdraw)) + "$")
        break
else:
    print("wrong pin")
    print(str(flag + 1) + ' attempts wrong')
    
