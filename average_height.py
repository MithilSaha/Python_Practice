import math
user_data = input("Enter heights:\t").split()
counter,total_height = 0,0
for i in user_data:
    total_height = total_height + int(i)
    counter = counter + 1
average_height = total_height/counter
print(average_height)
average_height = math.ceil(total_height/counter)
print(f"Average height is : {average_height}")