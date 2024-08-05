#customer is purchasing five items and then he pay 7% tax we have to show total payment with tax
#also we have to take input from user as well for those 5 items 
item1=float(input("Enter price of item 1:\n"))
item2=float(input("Enter price of item 2:\n"))
item3=float(input("Enter price of item 3:\n"))
item4=float(input("Enter price of item 4:\n"))
item5=float(input("Enter price of item 5:\n"))
Totalamount=item1+item2+item3+item4+item5
Salestax=7/100*Totalamount
print("Amount of Salestax are :",Salestax,"pkr")
NetTotal=Salestax+Totalamount
print("The net total is :",NetTotal,"pkr")