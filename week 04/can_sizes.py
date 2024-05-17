import math 

CAN_SIZES = [
    {"name": "#1 Picnic", "radius": 6.83, "height": 10.16, "cost": 0.28},
    {"name": "#1 Tall", "radius": 7.78, "height": 11.91, "cost": 0.43},
]
def compute_volume(radius, height):
    return math.pi * radius**2 * height

def compute_surface_area(radius, height):
    return 2 * math.pi *radius * (radius + height) 

def compute_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def compute_storage_efficiency(radius, height):
    volume = compute_volume(radius, height) 
    surface_area = compute_surface_area(radius, height)
    return volume / surface_area

def compute_cost_efficiency(radius, height, cost):
    volume = compute_volume(radius, height)
    return volume / cost 

def main():
    for can in CAN_SIZES:
        name = can['name']
        radius = can['height']
        height = can ['height']
        cost = can['cost']

        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        storage_efficiency = volume / surface_area
        cost_efficiency = compute_cost_efficiency(radius, height, cost)

        print(f'{name} Storage Efficiency: {storage_efficiency:.2f}')
        print(f'{name} Cost Efficiency: {cost_efficiency:.2f}')


        if __name__ == '__main__':
            main()




# """
# Braden Roenfeldt
# Brother Keers
# 12:45
# """

# #Goal is to print out 12 different cans with their radi, height, and cost per can

# import math

# def main():
#     #Define the can names, radii and heights
#     canNames = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cynlinder", "#5", "#6Z", "#8Z Short", "#10", "#211", "#300", "#303"]
#     canRadii = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
#     canHeights = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
#     #Create empty list for storage efficiencies
#     storageEfficiencies = []
#     #Iterate through the list of cans and calculate the storage efficiency
#     for i in range (0,12):
#         #Append the storage efficiency to the list
#         storageEfficiencies.append(compute_storage_efficiency(canRadii[i], canHeights[i]))
#         #Print the can name and storage efficiency
#         print(f"{canNames[i]} {storageEfficiencies[i]:.2f}")

    

# def compute_volume(radius, height):
#     """
#     Calculate the volume of a right circular cylinder
#     Args:
#         radius: float
#         height: float
#     Returns:
#         volume: float
#     """
#     #Calculate volume and return it
#     volume = math.pi * radius**2 * height
#     return volume

# def compute_surface_area(radius, height):
#     """
#     Calculate the surface area of a right circular cylinder
#     Args:
#         radius: float
#         height: float
#     Returns:
#         surfaceArea: float
#     """
#     #Calculate surface area and return it
#     surfaceArea = math.pi*2*radius*(height+radius)
#     return surfaceArea

# def compute_storage_efficiency(radius, height):
#     """
#     Calculate the surface area to volume ratio of a right circular cylinder
#     Args:
#         radius: float
#         height: float
#     Returns:
#         efficiency/ratio: float
#     """
#     #Call the volume and surface area functions and save them as variables
#     volume = compute_volume(radius, height)
#     surfaceArea = compute_surface_area(radius, height)
#     #Calculate the efficiency by dividing the volume by the surface area and return it
#     efficiency = volume / surfaceArea
#     return efficiency

# #Start the program by calling the main function
# if __name__ == "__main__":
#     main()


