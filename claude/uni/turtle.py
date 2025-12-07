#Add 5 temps and find the lowest without built in functions
def find_min_temperature(lowest):
    temperatue = lowest[0]
    for i in lowest:
        if i < temperatue:
            temperatue = i
    return temperatue
        
temperatures = []
for i in range(5):
    temp = float(input(f"Enter the {i+1} temperature: "))
    temperatures.append(temp)
print(f"The lowest temperature is {find_min_temperature(temperatures)}")
#-----------------------------------------------------------------

# turn temp from celsius to fahrenheit
def celsius_to_fahrenheit(cel):
    return (cel * 9/5) + 32

celsius = float(input("Enter a temperature in celsius: "))
print(f"The temperature you've entered  is equal {celsius_to_fahrenheit(celsius)} in Fahrenheit ")
#-------------------------------------------------------------------

#reverse a string with function
def reverse_string(string):
    return string [::-1]
s = input("Enter a string: ")
print(reverse_string(s))
#-------------------------------------------------------------------

# turn temp from fahrenheit to celsius
def fahrenheit_to_celsius(fahren):
    return (fahren - 32) * 5/9
fahrenheit = float(input("Enter a temperature in fahrenheit: "))
print(f"The temperature you've entered is equal {fahrenheit_to_celsius(fahrenheit)} in celsius ")
#--------------------------------------------------------------------
#Add 5 scores and find the highest without built in functions
def highest_score(highest):
    score = highest[0]
    for i in highest:
        if i > score:
            score = i
    return score

scores_list = []
for i in range(5):
    scores = float(input(f"Enter the {i + 1} score: "))
    scores_list.append(scores)
print(f"Highest score is {highest_score(scores_list)}")

#------------------------------------------------------------------

postive_list = []
even_numbers = []
odd_numbers = []
while True:
    postive_integers = int(input("Enter postive numbers: "))
    if postive_integers > 0:
        postive_list.append(postive_integers)
    else:
        break
    for even in postive_list:
         if even % 2 == 0:
            even_numbers.append(even)   
                       
    for odd in postive_list:
        if odd % 2 != 0:
            odd_numbers.append(odd)
            
print(f"All numbers {postive_list}")
print(f"Even numbers {set(even_numbers)}")
print(f"odd numbers {set(odd_numbers)}")
 
#=====================================================================
scores = [10, 20, 30]
total = 0
for i in scores:
    summ = total + i
print(summ)