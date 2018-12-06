def timeToSave():
    total_cost = float(input("How much does your dream home cost?"))
    portion_down_payment = 0.25
    current_savings = 0
    r = .04
    annual_salary = float(input("What's your annual salary?"))
    portion_saved = float(input("What portion of your salary can you save?"))
    number_of_months = 0
    
    while current_savings < total_cost * portion_down_payment:
        number_of_months += 1
        current_savings += (current_savings*r/12) + annual_salary/12 * portion_saved
        
    print(number_of_months)

    
timeToSave()