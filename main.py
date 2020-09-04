grade_one = (input("Enter your Course 1 grade: "))
credit_one = input("Enter your Credit 1 grade: ")
point_one = 0
if point_one == 'A':
  print(4.0)
elif point_one == 'A-':
  print(3.67)
elif point_one == 'B+':
  print(3.33)
elif point_one == 'B':
  print(3.0)
elif point_one == 'B-':
  print(2.67)
elif point_one == 'C+':
  print(2.33)
elif point_one == 'C':
  print(2.0)
elif point_one == 'D':
  print(1.0)
else:
  print(0.0)
print(point_one)
grade_two = (input("Enter your Course 2 grade: "))
credit_two = input("Enter your Credit 2 grade: ")
point_two = 0
if point_two == 'A':
  print(4.0)
elif point_two == 'A-':
  print(3.67)
elif point_two == 'B+':
  print(3.33)
elif point_two == 'B':
  print(3.0)
elif point_two == 'B-':
  print(2.67)
elif point_two == 'C+':
  print(2.33)
elif point_two == 'C':
  print(2.0)
elif point_two == 'D':
  print(1.0)
else:
  print(0.0)
print(point_two)
grade_three = (input("Enter your Course 3 grade: "))
credit_three = input("Enter your Credit 3 grade: ")
point_three = 0
if point_three == 'A':
  print(4.0)
elif point_three == 'A-':
  print(3.67)
elif point_three == 'B+':
  print(3.33)
elif point_three == 'B':
  print(3.0)
elif point_three == 'B-':
  print(2.67)
elif point_three == 'C+':
  print(2.33)
elif point_three == 'C':
  print(2.0)
elif point_three == 'D':
  print(1.0)
else:
  print(0.0)
GPA = (f"{point_one} * {credit_one} + {point_two} * {credit_two} +{point_three} * {credit_three}) / ({credit_one} + {credit_two} + {credit_three}")
print(f"Your GPA is: {GPA}")
