
starting_salary = float(input("What's your annual salary? "))

total_cost = 1000000
down_payment = total_cost * .25
r = .04
semi_annual_raise = 0.07
months = 36
current_savings = 0
epsilon = 100
high = 10000
low = 0
guess = (high + low) / 2
steps = 0
can_i_pay_in_3_years = True

while abs(current_savings - down_payment) >= epsilon:
    steps +=1
    #reset current savings to 0 each time
    current_savings = 0
    #reset annual_salary to original salary each time
    annual_salary = starting_salary
    #calculate monthly savings using original salary each time
    monthly_savings = (annual_salary / 12) * (guess / 10000)
    for month in range(1, months+1):
        #collect interest on current savings
        current_savings *= 1 + (r/12)
        #add this month's savings to current savings
        current_savings += monthly_savings
        if month % 6 == 0:
            #recalculate annual salary
            annual_salary += annual_salary * semi_annual_raise
            #recalculate monthly savings
            monthly_savings = (annual_salary / 12) * (guess / 10000)
    
    if abs(current_savings - down_payment)  < epsilon:
        break
    
    if current_savings > down_payment:
        high = guess
    else:
        low = guess
        
    if low >= high:
        can_i_pay_in_3_years = False
        break
    
    guess = int(round((high + low) / 2))

  
if can_i_pay_in_3_years:
    print("Ideal Portion Saved: ", guess / 10000)
    print("Num steps: ", steps)
else:
    print("Can't save enough in 3 years")