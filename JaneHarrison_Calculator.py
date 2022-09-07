#Functions
def calculate_area (height, width, length):
    area = height * width * length
    return (area)

def create_line():
    print("\n"+"*" * 80)

#Welcome Message
create_line()
print("\nHello! Welcome to The Area Calculator!")
create_line()

#Input
height_input = input("\nPlease enter the height of your item: ")
width_input = input("\nPlease enter the width of your item: ")
length_input = input("\nPlease enter the length of your item: ")
unit_input = input("\nWhat is your unit of measurement?")

#Convert inputs to float
height = float(height_input)
width = float(width_input)
length = float(length_input)

#Call function
calculated_area = round(calculate_area(height,width,length),2)

#Print results and summary
create_line()
print(f"\nThe area of your item is {calculated_area} {unit_input} cubed!\n")
create_line()
print(f"\nSummary: \nheight = {height} {unit_input}\nwidth = {width} {unit_input}\nlength = {length} {unit_input}.\nTherefore, the area is {calculated_area} {unit_input} cubed (to the nearest two decimal places). ")
create_line()
print("Thank you for using the calculator.")
create_line()
exit()