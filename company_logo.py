d1,numbers,final_list = {},[],[]

#Getting company's name from user and making it to lower case
user_data = input("Enter company's name:\t").lower()

#Saving all characters and it's number of occurance in the word in a Dictionary d1={}
for i in user_data:

    #counter variable stores the number of occurances of a character in the word
    counter = user_data.count(i)

    #assigning the number of occurances of a charachter in the Dictionary d1
    d1[i] = counter

#Appending the list called number with the number of occuranaces of the every characters in the word
for i in d1:
    numbers.append(d1[i])
if len(numbers) == 1:
    for i in d1:
        print(i,d1[i],sep=" ")
else:
    #Created a temporary list to save the distinct number of occurances of all characters
    temp_list1 = [max(numbers),min(numbers)]

    #Adding distinct number of occurances of all characters in list temp_list1
    for i in range(0,len(numbers)):
        if numbers[i] != max(numbers) and numbers[i] != min(numbers):
            # If same occurance number repeats then IF condition will not allow to append it to list temp_list1
            if temp_list1.count(numbers[i]) == 0:
                temp_list1.append(numbers[i])

    #Sorting and Reversing the list temp_list1
    temp_list1.sort(reverse=True)

    #Crating lists inside the list final_list as per the distinct occurances of all characters in the word
    for i in range(0,len(temp_list1)):
        final_list.append([])

    #Saving characters in the order of their number of occurances inside the lists of final_list
    for i in range(0,len(temp_list1)):
        for j in d1:
            #Saving the characters in list final_list in a manner of occurances in decending order
            if d1[j] == temp_list1[i]:
                final_list[i].append(j)

    #Creating counter for counting top 3 charcgters to choose for logo
    counter = 0

    #Sorting the nested lists inside final_list
    for i in final_list:
        i.sort()

    #Fetching nested sorted lists of final_list
    for i in final_list:
        for j in i:
            #counter stores the number of loopings
            counter = counter +  1
            #Taking top 3 characters for company's logo
            if counter < 4:
                print(j,d1[j],sep=" ")