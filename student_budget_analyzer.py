# about student 
name = input("enter student name:")
print("student name:",name)
income = float(input("enter income:"))
print("monthly income:",income)
#about student  transaction
food= float(input("enter food payments:"))
print("food payments",food)
travel= float(input("enter travel payments:"))
print("travel payments",travel)
study= float(input("enter study payments:"))
print("study payments",study)
internet= float(input("enter internet payments:"))
print("internet payments",internet)
other = float(input("enter other payment:"))
print("other payment:"),other
      
#total outcome of payment
total_payment= food +travel+study+internet+other  
print("total_payment:",total_payment)

#left amount
balance=income-total_payment
print("left balance:",balance)
#savings
saving_rate= (balance/income)*100
print("saving_rate:",saving_rate,"%")
#individual payment in percentage
food_percent=(food/total_payment)*100
print("food_percentage:",food_percent,"%")
travel_percent=(travel/total_payment)*100
print("travel_percentage:",travel_percent,"%")
study_percent=(study/total_payment)*100
print("study_percentage:",study_percent,"%")
internet_percent=(internet/total_payment)*100
print("internet_percentage:",internet_percent,"%")
other_percent=(other/total_payment)*100
print("other_percentage:",other_percent,"%")
#type fxn
print(type(name))
print(type(income))
print(type(food))
print(type(total_payment))
#final output of budget_analyzer
print("\n----MONTHLY BUDGET REPORT----")
print("studnet name:",name)

print("monthly income:",income)

print("food :",food)

print("travel:",travel)

print("study:",study)

print("internet:",internet)

print("total_payment:",total_payment)

print("left_balance:",balance)

print("saving_rate:",saving_rate,"%") 



