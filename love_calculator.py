his_name = input("Enter his name:\n")
her_name = input("Enter her name:\n")
total_count_1,total_count_2 = 0,0
for i in "true":
    his_counter = (his_name.lower().count(i))
    her_counter = (her_name.lower().count(i))
    total_count_1 = his_counter + her_counter + total_count_1

for i in "love":
    his_counter = (his_name.lower().count(i))
    her_counter = (her_name.lower().count(i))
    total_count_2 = his_counter + her_counter + total_count_2

print(f"Your Score is {total_count_1}{total_count_2}%")
