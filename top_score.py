# user_data = input("Enter scores:\t").split()
# top_score = 0
# for i in range(0,len(user_data)):
#     if top_score >= int(user_data[i]):
#         top_score = top_score
#     else:
#         top_score = int(user_data[i])
# print(f"Top score is {top_score}")
import random
computer_data = []
top_score = 0
counter = random.randint(10,50)
for i in range(1,counter):
    computer_data.append(random.randint(0,100))
print(computer_data)
for i in range(0,len(computer_data)):
    if top_score >= int(computer_data[i]):
        top_score = top_score
    else:
        top_score = int(computer_data[i])
print(f"Top score is {top_score}")
