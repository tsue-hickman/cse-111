

    # *kwargs is a prameter that accepts any number of arguments (infinite)

#you can nest a function inside of a function,
#  but that function will only be available to it's parent(s) function(s).

def outer(a):
    print(f"I was printed by outer(): {a}")

    def inner(a):
        print(f"I was printed by inner(): {a * 3}")
    
    inner(a)

outer()


def individual (**person):
    print(f"{person['fname']} {person['lname']}")
    

#the data for names becomes a list of names because of the astrick *
def family(surname, *names):
    for name in names:
        print(f"{name} {surname}")


# the d is a default parameter
def family(surname, d"*" *names):
    for name in names:
        print(f"{name} {surname}")


family("Doe", "John", "Jane", "Jim")










# # what is wrong with this code?
# roster = []
# add_to_roster(roster)

# print(roster)


# #this is demonstrating default values 
# def foo (bar, baz):
#     print(bar, baz)

# foo('Hello', 42)

# def bar (foo, baz=42):
#     print(foo, baz)

# bar('Hello')



# def add_to_roster(roster):
#     while True:
#         name = input('What name would you like to add to the roster? ')
#         if name == '':
#             break
#         roster.append(name)


# simple function example
# def area_of_a_square(side):
#     area = side ** 2 
#     return area

# print (area_of_a_square(5)) 




# from datetime import datetime

# def what_is_the_day():
#     timestamp = datetime.now()
#     print (timestamp)

# what_is_the_day()



# def hello ():
#     print('Hello, World!')

# class Greeter(): THIS WAS AN EXAMPLE TO TEACH US THE DIFFERENCE BETWEEN FUNCTIONS AND METHODS... METHODS ARE FUNCTIONS INSIDE OF CLASSES

#     def __init__(self):
#         pass
    
#     def hello(self):
#         print(self.msg)

#     def hello():
#         print('Hello, A')

#     g = Greeter()
#     g.

#     hello ()



    
    

