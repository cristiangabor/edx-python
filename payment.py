balance=5000
annualInterest=0.02
monthlyInterestRate=annualInterest/12.0
lower_bound=balance/12
upper_bound=(balance*(1+monthlyInterestRate)**12)/12.0
monthlyPayment=(lower_bound+upper_bound)/2
newbalance=balance
month=0

while newbalance>0:
	newbalance=balance

	for month in range(1,13):
		newbalance -= monthlyPayment
		newbalance +=monthlyInterestRate * newbalance
		month +=1
	if newbalance < 0:
		monthlyPayment=lower_bound
	else:
		monthlyPayment=upper_bound
	monthlyPayment=(lower_bound+upper_bound)/2

print "Lowest Payment:" , round(monthlyPayment,2)
