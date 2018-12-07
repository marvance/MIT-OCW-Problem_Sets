def timeToSave():
    annual_salary = float(input("What's your annual salary?"))
    portion_saved = float(input("What portion of your salary can you save, as a decimal?"))
    total_cost = float(input("How much does your dream home cost?"))
    semi_annual_raise = float(input("What's your semi-annual raise percentage, as a decimal?"))
    portion_down_payment = 0.25
    current_savings = 0
    r = .04
    number_of_months = 0
    
    while current_savings < total_cost * portion_down_payment:
        number_of_months += 1
        current_savings += (current_savings*r/12) + annual_salary/12 * portion_saved
        if number_of_months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
        
    print("Number of months: ", number_of_months)

    
timeToSave()