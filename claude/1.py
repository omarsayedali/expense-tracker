def calculate_average(grade1, grade2, grade3=None, grade4=None):
    if grade4 is not None:      
       return (grade1 + grade2 + grade3 + grade4) / 4
    elif grade3 is not None:
        return (grade1 + grade2 + grade3) / 3
    else:
        return (grade1 + grade2) / 2
    
print(calculate_average(80, 90))           
print(calculate_average(80, 90, 85))       
print(calculate_average(80, 90, 85, 75))   


 
