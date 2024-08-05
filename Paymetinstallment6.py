print("Enter amount of purchase")
purchase=float(input())
NumberofInstallment=float(input("Enter number of installments:\n"))
addfiveper=5/100*purchase
Totalpurchase=addfiveper+purchase
Amountperinstallment=Totalpurchase/NumberofInstallment
print("Total amount of Purchase:",Totalpurchase)
##means u will pay this amount per installlment 
print("Amount per installment:", Amountperinstallment)