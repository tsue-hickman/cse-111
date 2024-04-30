

def add_to_roster(roster):
    while True:
        name = input('What name would you like to add to the roster? ')
        if name == '':
            break
        roster.append(name)



# what is wrong with this code?
roster = []
add_to_roster(roster)

print(roster)






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



    
    

