def greet(name):
    print('Hello ' + name)
"""The function that will take the name variable based on user input and print the response"""

def name_input():
    name = input('Can I have your name please?\n')
    return name
"""The function that asks the user the initial question and sets the name variable"""
greet(name_input())

