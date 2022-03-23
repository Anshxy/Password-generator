import random
import string


#Creating the lists for each category.
letters = list(string.ascii_lowercase + '@' + '_' + '-')
numbers = list(string.digits)


random_num = [6,7,8,9,10,11,12]
num_len_list = [0,1,2,3,4,5,6,7]


#Initialsing an empty list for the password
password = []


check = input("Would you like to customize your password to your preferecences? (y/n): ")



if check.lower() == "y":
  
  length = input("How many letters do you want in the password?: ")
  number_length = input("How many numbers would you like to be in the password?: ")
  exclude = input("What characters would you like to exclude from the password? -- Seperate by spaces -- : ")
  exclude_list = exclude.split()

  #Removing values from 'letters' list
  for list in exclude_list:
    letters.remove(list)
    print(f"removed value - '{list}'")

  
  customize = True
  
else:
  
  print("\n")
  customize = False
  length = random.choice(random_num)
  number_length = random.choice(num_len_list)




print("Creating password...")





  
#Adding letters to the password list
for i in range(int(length)):
  password.append(random.choice(letters))

#Adding numbers to the password list
for i in range(int(number_length)):
  password.append(random.choice(numbers))


#Shuffling the list in a random order.
random.shuffle(password)
print("\n")

#Joining list into a string
print("".join(password))

#Checking if password is true to the 'safe' values

#Courtesy - https://tcblog.protiviti.com/2017/09/26/the-8-character-password-is-dead/
if len(password) < 8:
  failed_1 = True
  print("Failed check #1")
else:
  failed_1 = False
  print("Passed check #1")
  

if int(number_length) < 2:
  failed_2 = True
  print("Failed check #2")
  print("\n")
else:
  failed_2 = False
  print("Passed check #2")
  print("\n")

if failed_1 == True and failed_2 == True and customize == True:
  print("This password isn't safe!")
elif failed_1 == True or failed_2 == True and customize == True:
  print("This password is alright.")
elif failed_1 == False and failed_2 == False and customize == True:
  print("This password is safe!")


