''' Assignment_5
Question:- write a function called max_of_three that takes three parameters as inputs and returns the largest of the three. The function should use conditional statements to compare the values and determine the greatest.  
-Ensure that your function handles edge cases, such as when two or more numbers are equal.'''


def max_of_three(a,b,c):
    
    if a >= b and a >=c:
        print("The Max Number is ",a)
        
    elif b >= a and b >= c:
        print("The Max Number is ",b)
    
    else:
        print("The Max Number is ",c)        
        
max_of_three(int(input("Enter the 1st number: ")), int(input("Enter the 2nd number: ")), int(input("Enter the 3rd number: ")))

print("Good bye")
