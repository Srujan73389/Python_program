# Python_program
size=input("Enter which size you want (S/M/L):")
bill=0
if size=='S' or size=='s':
    bill+=100
    print("Bill for Small Size pizza is 100Rs.")
elif size=='M' or size=='m':
    bill+=200
    print("Bill for Medium Size pizza is 200Rs.")
else:
    bill+=300
    print("Bill for Large Size pizza is 300Rs.")
add_pepproni=input("Do you want pepporini(Y/N):")
if add_pepproni=="Y" or add_pepproni=='y':
    if size=='S' or size=='s':
        bill+=30
    else:
        bill+=50
add_cheese=input("do u want cheese(Y/N")
if add_cheese=='Y' or add_cheese=='y':
    bill+=20
print(f"Your Final Bill is {bill} Rs.")
