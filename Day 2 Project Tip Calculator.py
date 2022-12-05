#If the bill was $150.00, split between 5 people, with a 12% tip.
print("Welcome to the tip calculator!")
Total_bill = float(input("What was the total bill? $"))
Tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
Split_bill = int(input("How many people to split the bill? "))
percent = (Tip / 100) + 1
percent_total = percent * Total_bill
request = percent + Total_bill
Each_person_pay = request / Split_bill
print(Each_person_pay)

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
