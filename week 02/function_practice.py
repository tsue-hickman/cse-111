"""
Author: Brother Keers

This is a simple demonstration of python functions and different ways to declare
(create) them.

Remember that `arguments` refers to when you are calling (invoking) a function
and `parameters` refers to the parameters that function will use/replies on
based on its function signature (where you defined the function).
"""

"""
Positional
---------- 
This is an example of positional parameters in a function. The arguments you call
a function with will be assigned as the functions parameters left to right.
"""
def foo(bar, baz):
    print(bar, baz)

foo("Hello", "World")

"""
Default values
--------------
You can set a default value that will be used for parameters that may not always
be needed. Optional parameters (parameters with default values) MUST be placed
at the end of your parameter lists.
"""
def bar(foo, baz=42):
    print(foo, baz)

bar("Hello")

""" 
*args
-----
You can also accept infinite non-keyword arguments with an `*args` parameter.
This MUST be placed after positional parameters and will create a list of any
additional parameters the function was called with.

For example here is what `names` will be set to:

names = ['Reyna', 'Chris', 'Matthew']
"""
def family(surname, *names):
    for name in names:
        print(f"{name} {surname}")

family('Keers', 'Reyna', 'Chris', 'Matthew')

# **kwargs
""" 
*kwargs
-----
You can also accept infinite keyword arguments with an `*kwargs` parameter.
This MUST be placed after positional parameters and will create a dictionary of
any additional parameters the function was called with.

For example here is what `person` will be set to:

person = {
    "fname": "Christopher",
    "lname": "Keers"
}
"""
def individual(**person):
    print(f"{person['fname']} {person['lname']}")

individual(fname="Christopher", lname="Keers")


"""
You can nest functions inside functions but keep in mind that inner functions
will only be available to its parent(s) function(s). If you find yourself wanting
to do this often you probably need a class which is covered in CSE 210.
"""
def outer(a):
    print(f"I was printed by outer(): {a}")

    def inner(a):
        print(f"I was printed by inner(): {a * 3}")
    
    inner(a)

outer("Hello!")