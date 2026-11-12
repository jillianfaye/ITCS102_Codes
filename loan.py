loan_amt=float(input("Enter amount"))
years=int(input("Enter year to pay"))
month=years*12
principal=loan_amt /month
remaining_bal=loan_amt
total=0
#for looop
print("|MONTH\t|\tPAYMENT\t\t|\tINTEREST\t|\tPRINCIPAL\t|\tBALANCE\t|")
for count in range (1,month+1):
    remaining_bal-=principal
    loan_interest=remaining_bal*0.00256
    monthly_pay=loan_interest+principal
    #print(count,round(monthly_pay,2), round(loan_interest,2), round(principal,2), round(remaining_bal,2))
    print(f"|    {count}\t\t{round(monthly_pay,2)}\t\t\t {round(loan_interest,2)}\t\t\t {round(principal,2)}\t\t\t {round(remaining_bal,2)}\t\t|")

print(total)