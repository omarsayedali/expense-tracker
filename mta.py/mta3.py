temperatures = [25,11,34,13,27,22]
def analyze_temps(temps):
    avg = sum(temps)/len(temps)
    lowest = min(temps)
    return avg , lowest
avg , lowest = analyze_temps(temperatures)
print("average temp: ", round(avg,1))
print("lowest temp: ", lowest)


input_tuple = (5, 9, 11, 15, 20)
def transform_tuple(t):
    new_list = []
    for num in t:
        if num % 2 == 0:
            new_list.append(num*3)
        else:
            new_list.append(num)
    return sorted(new_list, reverse=True)
print("original tuple:", input_tuple)
print("New List:", transform_tuple(input_tuple))
         