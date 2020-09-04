grade_one = (input("Enter your Course 1 grade: "))
credit_one = input("Enter your Credit 1 grade: ")
if grade_one == 'A':
  print(4.0)
elif grade_one == 'A-':
  print(3.67)
elif grade_one == 'B+':
  print(3.33)
elif grade_one == 'B':
  print(3.0)
elif grade_one == 'B-':
  print(2.67)
elif grade_one == 'C+':
  print(2.33)
elif grade_one == 'C':
  print(2.0)
elif grade_one == 'D':
  print(1.0)
else:
  print(0.0)
grade_two = (input("Enter your Course 2 grade: "))
credit_two = input("Enter your Credit 2 grade: ")
if grade_two == 'A':
  print(4.0)
elif grade_two == 'A-':
  print(3.67)
elif grade_two == 'B+':
  print(3.33)
elif grade_two == 'B':
  print(3.0)
elif grade_two == 'B-':
  print(2.67)
elif grade_two == 'C+':
  print(2.33)
elif grade_two == 'C':
  print(2.0)
elif grade_two == 'D':
  print(1.0)
else:
  print(0.0)
grade_three = (input("Enter your Course 3 grade: "))
credit_three = input("Enter your Credit 3 grade: ")
if grade_three == 'A':
  print(4.0)
elif grade_three == 'A-':
  print(3.67)
elif grade_three == 'B+':
  print(3.33)
elif grade_three == 'B':
  print(3.0)
elif grade_three == 'B-':
  print(2.67)
elif grade_three == 'C+':
  print(2.33)
elif grade_three == 'C':
  print(2.0)
elif grade_three == 'D':
  print(1.0)
else:
  print(0.0)
GPA = (f"{grade_one} * {credit_one} + {grade_two} * {credit_two} +{grade_three} * {credit_three}) / ({credit_one} + {credit_two} + {credit_three}")
print(f"Your GPA is: {GPA}")
