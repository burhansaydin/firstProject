

print("Welcome to the tip calculator")
total_bill= float(input("what was the total bill? $"))
tip_per= float(input("what percentage tip would you like to give?  10'12 or 15?" ))
people= int(input("how many people split the bill?"))

total=total_bill+(total_bill*tip_per/100)
each=round(total/people,2)

print(f"Each person shold pay ${each}")