'''
Michael Mcmanimon
project 7
'''

#read the input starting salary

salary = float(input("Enter starting salary: "));

#read the input percentage increase

increase_percent = float(input("Enter percentage increase: "));

#read the input number of years increase

years = int(input("Enter number of years in the schedule: "));

print("Year\tSalary")

#Begin for-loop to compute the percentage increase

for i in range(1, years+1):

    print("%d\t%.2f" %(i, salary));

    # compute the next year salary using current year salary

    salary = salary + (salary*increase_percent)/100;



