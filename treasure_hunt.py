row1 = []
row2 = []
row3 = []
for j in range(0,3):
    row1.append(u'\u25fb')
    row2.append(u'\u25fb')
    row3.append(u'\u25fb')
map = [row1,row2,row3]
user_data = input("Enter Column & Row No:\n")
user_column,user_row = int(user_data[0]),int(user_data[1])
map[user_row - 1][user_column - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")