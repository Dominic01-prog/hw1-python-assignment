# Author: Dominic Savaglio djs7129@psu.edu
# Collaborator: Shakeb 
grade_one = (input("Enter your Course 1 grade: "))
credit_one = float(input("Enter your Credit 1 grade: "))
point_one = 0
if grade_one == 'A':
  point_one = 4.0
elif grade_one == 'A-':
  point_one = 3.67
elif grade_one == 'B+':
  point_one = float(3.33)
elif grade_one == 'B':
  point_one = 3.0
elif grade_one == 'B-':
  point_one = 2.67
elif grade_one == 'C+':
  point_one = 2.33
elif grade_one == 'C':
  point_one = 2.0
elif grade_one == 'D':
  point_one = 1.0
else:
  point_one = 0.0
print(f"Grade point for Course 1 is: {point_one}")
grade_two = (input("Enter your Course 2 grade: "))
credit_two = float(input("Enter your Credit 2 grade: "))
point_two = 0
if grade_two == 'A':
  point_two = float(4.0)
elif grade_two == 'A-':
  point_two = 3.67
elif grade_two == 'B+':
  point_two = 3.33
elif grade_two == 'B':
  point_two = 3.0
elif grade_two == 'B-':
  point_two = 2.67
elif grade_two == 'C+':
  point_two = 2.33
elif grade_two == 'C':
  point_two = 2.0
elif grade_two == 'D':
  point_two = 1.0
else:
  point_two = 0.0
print(f"Grade point for Course 2 is: {point_two} ")
grade_three = (input("Enter your Course 3 grade: "))
credit_three = float(input("Enter your Credit 3 grade: "))
point_three = 0
if grade_three == 'A':
  point_three = 4.0
elif grade_three == 'A-':
  point_three = 3.67
elif grade_three == 'B+':
  point_three = 3.33
elif grade_three == 'B':
  point_three = float(3.0)
elif grade_three == 'B-':
  point_three = 2.67
elif grade_three == 'C+':
  point_three = 2.33
elif grade_three == 'C':
  point_three = 2.0
elif grade_three == 'D':
  point_three = 1.0
else:
  point_three = 0.0
print(f"Grade point for Course 3 is: {point_three}")
GPA = (point_one * credit_one + point_two * credit_two +point_three * credit_three) / (credit_one + credit_two + credit_three)
print(f"Your GPA is: {GPA}")
