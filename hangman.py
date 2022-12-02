secret_word = "Hangman"
secret_word_list  = list(secret_word.lower())
guessing = True
display_word = []
counter  = 0
counter1 = 0
v = ""
for i in range(0,len(secret_word)):
    display_word.append("_")

for i in range(0,len(secret_word)):
    v = v + "_"
print(v)

while guessing:
    user_data = input("Enter a letter:\t").lower()
    if user_data == "":
        print("Please enter a letter")
    else:
        if user_data in secret_word_list:
            for i in range(0,len(secret_word)):
                if (secret_word[i]).lower() == user_data and display_word[i] == "_":  
                    display_word[i] = user_data
                    result = ""
                    for i in display_word:
                        result = result + i
                    print(result)
                    secret_word_list.remove(user_data)
                    counter1 = counter1 + 1
                    if counter1 == len(secret_word):
                        print("Save from hanging!")
                        guessing = False
                    break
        else:
            counter = counter + 1
            if counter == 7:
                print("Hanged!")
                guessing = False
            else:
                if counter == 1:
                    print("From Happy face to no expression face")
                elif counter == 2:
                    print("Stand No 1")
                elif counter == 3:
                    print("Stand No 2")
                elif counter == 4:
                    print("Stand No 3")
                elif counter == 5:
                    print("Rope hanging")
                elif counter == 6:
                    print("Rope hanging around neck")