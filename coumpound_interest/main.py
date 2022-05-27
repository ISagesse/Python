# calculate your 10 year investment based on your interest

i = 1

return_investment = 0

investment, interest = input("Please enter your investment follow by the interst rate: ").split()

investment = float(investment)
interest = float(interest) / 100

while (i != 10):
    return_investment += investment * interest
    i += 1
    
print('Your return investment in 10 years is ${:.2f} '.format(return_investment))