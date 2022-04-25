total_cost = 1000000
portion_down_payment = 0.25
down_payment = portion_down_payment*total_cost
print(f"{down_payment:,}")

months = 36
savings = 0
investment_rate = 0.04
semi_annual_raise = 0.07

annual_salary = 78540 # float(input("Enter starting salary: "))

low = num_guesses = 0
high = initial_high = 10000
epsilon = 100
portion_saved = (high + low)/2
while abs(savings - down_payment) >= epsilon:
    monthly_salary = annual_salary/12
    savings = 0

    monthly_deposit = monthly_salary * portion_saved / 10000

    # calculate savings after n months
    for i in range(1, months+1):
        savings += (savings * investment_rate / 12) \
            + (monthly_deposit)
        if (i % 6 == 0):
            monthly_salary += (monthly_salary * semi_annual_raise)

    num_guesses += 1

    # move bounds
    if savings < down_payment:
        low = portion_saved
        print("up  ", end=' ')
    else:
        high = portion_saved
        print("down", end=' ')
    portion_saved = (high + low)/2

    print(f"{num_guesses} : {savings:,}  {portion_saved / 10000} {abs(savings - down_payment)} {high} {low}")

    # break if bounds get stuck
    if high == low:
        break

if initial_high == portion_saved:
    print("It is not possible to pay the down payment in three years")
else:
    print(f"Best savings rate: {round(portion_saved / 10000, 4)}")
    print(f"Steps in bisection search: {num_guesses}")
