def main():
    # this creates an empty list for the variable 'fabrics' 
    fabrics =fabrics[]

    # this adds three elements at th end of the fabrics list
    fabrics.append("cotton")
    fabrics.append("silk")
    fabrics.append("wool")

    # this inserts an element at the beginning of the fabrics list
    fabrics.insert(0, "satin")
    print(fabrics)


# this will determine if a specific element is in the list of fabrics
if "silk" in fabrics:
    print("silk is in the fabrics list")
else: 
    print("silk is NOT in the fabrics list")

    # this gets the index of where a specific element is stored in the fabrics list. 
i = fabrics.index("silk")
print(i)

#  this replaces silk with taffeta from the fabrics list 
fabrics[i] = "taffeta"

# this removes the last element from the fabrics list
fabrics.pop()

# this removes the first element from the fabrics list
fabrics.pop(0)

#  this is how to completely remove something from the list of fabrics
fabrics.remove("wool")

# this gets the length of the fabrics list and prints it
n = len(fabrics)
print(f"The fabrics list contains {n} elements")

print(fabrics)

if __name__ == "__main__":
    main()





    # this is a demo for the "for" loop 
    def main():
        # this creates a list of color names
        colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
# this is the actual 'for' loop within the function, which is the 'for ITEM in SEQUENCE . . .  execute THIS code'
        for color in colors:
            print (color)
        
if __name__ == "__main__":
    main()




numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0 

for num in numbers: 
    total += num 

print (total)







