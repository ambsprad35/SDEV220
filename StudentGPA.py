"""
Amber Spradley
StudentGPA.py

This app will get the student's first and last name and GPA.
Based on the student's GPA, the app will display if the 
student is on the Dean's List or Honor Roll.

str lName - student's last name
str fName - student's first name
float gpa - student's GPA
"""

# Prompt the user for the student's last name 'ZZZ' quits the app
lName = input("Enter the student's last name or ZZZ to quit.").upper()

while(lName != "ZZZ"): # Only continue if 'ZZZ' was not entered
    fName = input("Enter the student's first name.")
    try:
        gpa = float(input("Enter the student's GPA."))
    except ValueError:
        print("GPA must be a valid number")
        break
    
    if(gpa >= 3.5): #Determine if the student is either on the Dean's list or Honor Roll
        print("Congrats! " + fName + " " + lName + " has made the Dean's List.")
    elif (3.25 <= gpa < 3.5):
        print("Congrats! " + fName + " " + lName + " has made the Honor Roll.")
    else:
        print("Sorry. " + fName + " " + lName + " did not make either list.") 
    
    lName = input("Enter the student's last name or ZZZ to quit.")