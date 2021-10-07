"""
Program: inner_functions_assignment.py
Author: Andy Volesky
Last date modified: 10/06/2021

The purpose of this program:

write a function measurements that accepts a list of measurements for a rectangle and returns a string
with perimeter and area

Write 2 inner functions that accept a list as parameter

area(a_list) -- calculates the area
recall accessing items in a list: a_list[#]

perimeter(a_list) -- calculates the perimeter
recall accessing items in a list: a_list[#]

The outer, measurements function will call the area() and the perimeter()
The outer function will build a string and return the following string:

Perimeter = 11.0 Area = 7.14  # if this is the perimeter and the area.

Next, add necessary statements to calculate for a square the perimeter and the area.

len(a_list) is helpful to decide if the list has 1 or 2 items.

In your main, call the function for a square and for a rectangle
"""

def measurements(a_list):
    def area(a_list):
        if len(a_list) > 1:
            a_calc = a_list[0]*a_list[1]
            return a_calc
        else:
            a_calc = a_list[0]**2
            return a_calc
    def perimeter(a_list):
        if len(a_list) > 1:
            p_calc = 2*a_list[0] + 2*a_list[1]
            return p_calc
        else:
            p_calc = 4*a_list[0]
            return p_calc
    return f"Perimeter = {perimeter(a_list)} Area = {area(a_list)}"



if __name__ == '__main__':
    rectangle = [2.1, 3.4]
    result = measurements(rectangle)
    print(result)
    square = [3.5]
    result = measurements(square)
    print(result)