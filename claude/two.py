




def calculate_average(grade1, grade2, grade3=None, grade4=None):
    return (grade1 + grade2 + grade3 + grade4) / 4

 

def is_passing(avg):
    return avg >= 60

def get_result(grade1, grade2, grade3, grade4):
    average = calculate_average(grade1, grade2, grade3, grade4)
    return "PASS" if is_passing(average) else "FAIL"

print(calculate_average(80, 90))           # 85.0
print(calculate_average(80, 90, 85))       # 85.0
print(calculate_average(80, 90, 85, 75))   # 82.5