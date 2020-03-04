def greet(name):
    print('Hello ' + name)

def name_input():
    name = input('Can I have your name please?\n')
    return name

greet(name_input())

