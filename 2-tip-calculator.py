#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("welcome to tip calculator")
bill=float(input("What is the bill amount? $"))
people=int(input("How many people shared the food?"))
tip_percent=int(input("How much tip you want to give? 10, 12, or 15? "))
share=round((bill+(bill* (tip_percent/100)))/people,2)
share ="{:.2f}".format(share)
print(f'Each person should pay: ${share}')