import random

#This is the word to guess
secret_word = "Hobby"

#Making a list called secret_word_list that will store all lettes of secret_word in lower case
secret_word_list  = list(secret_word.lower())

#Flag to Start and Stop the 1st While Loop
guessing = True

#An Empty list where right guessed letters will be stored
display_word = []
counter  = 0
counter1 = 0

#An empty string to store the undersocres that will be printed
v = ""

#Loop to create undersocres and store it to display_word list
for i in range(0,len(secret_word)):
    display_word.append("_")

#Loop to create a string of underscores to print
for i in range(0,len(secret_word)):
    v = v + "_"

#print the string of underscores
print(v)

#While Loop starts
while guessing:
    #User Input Letter
    user_data = input("Enter a letter:\t").lower()

    #If User send empty string
    if user_data == "":
        print("Please enter a letter")
    
    #If User send a correct letter two times but the correct letter's occurance in secret_word is 1
    elif user_data in display_word and (secret_word.lower()).count(user_data) == 1:
        print(f"Hint: There is no repetition of {user_data}")

    #Main Mechanism
    else:
        #if the letter entered by User is in secret_word_list list
        if user_data in secret_word_list:
            for i in range(0,len(secret_word)):

                '''
                If the i'th position letter of secret_word is the User entered letter
                and i'th posting of display_word list has "_" value then proceed
                '''
                if (secret_word[i]).lower() == user_data and display_word[i] == "_":

                    #If the occurance of the User entered letter is greater than 1 then proceed
                    if (secret_word.lower()).count(user_data) > 1:
                        '''creating a empty list called position and it will store the positions of the
                           letters that User entered'''
                        position = []

                        for i in range(0,len(secret_word)):

                            '''
                            Created a condition that will only be satisfied when the User entered letter
                            matches with i'th posting letter of secret_word
                            '''
                            if (((secret_word).lower())[i]) == (user_data):
                                #We are storing the positions of multiple occurant letters in secret_word
                                position.append(i)
                            else:
                                continue

                        #Flag to Start and Stop the 2nd While Loop
                        chossing = True

                        '''
                        Mechanism to choose the postions of mutliple occurant letters of secret_word
                        in random order and put the letter in that correct random postion
                        '''
                        while chossing:
                            #Randomly choosing one of the correct positions and save to n variable
                            n = random.choice(position)

                            #If the n'th position og display_word list has "_" then proceed
                            if display_word[n] == "_":

                                #Putting the User enter letter in the nth position of display_word list
                                display_word[n] = user_data

                                #Making the flag False so that the while loop does not run infinitely
                                chossing = False
                            else:
                                continue
                    #If User entered letter is occured in secret_word only single time then proceed
                    else:
                        display_word[i] = user_data

                    #An empty string to store the data of display_word list in a string form
                    result = ""

                    #Loop to convert the display_word list to a string
                    for i in display_word:
                        result = result + i
                    
                    #Final Result after User enter a correct letter each time
                    print(result)
                    #removing the letters from screcret_word_list that User has entered correctly
                    secret_word_list.remove(user_data)

                    counter1 = counter1 + 1
                    #If counter1 = length of secret_world, then user has gussed all letters correctly
                    if counter1 == len(secret_word):
                        print("Save from hanging!")
                        #To stop the While loop after winning
                        guessing = False
                    #To break the for loop and starts the while loop again
                    break
        #If User guess any incorrect letter
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