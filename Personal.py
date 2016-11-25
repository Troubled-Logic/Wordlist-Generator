Personal_info = []
Custom_words = []
Custom_numbers = []
Backwards_numbers = []
PI = []
import time

with open ("Backwards_numbers.txt", "r") as file:
  for line in file:
    Backwards_numbers.append(line.replace("\n", ""))
file.close()

with open ("Personal.txt", "r") as file:
  for line in file:
    Personal_info.append(line.replace("\n", ""))
file.close()

with open ("Custom_numbers.txt", "r") as file:
  for line in file:
    Personal_info.append(line.replace("\n", ""))
file.close()

with open ("Custom_words.txt", "r") as file:
  for line in file:
    Custom_numbers.append(line.replace("\n", ""))
file.close()

fname = Personal_info[0]
lname = Personal_info[1]
bday = Personal_info[2]
year = Personal_info[3]
lyear = year[2:]


Personal_info.append(lyear)
Personal_info.append(fname.capitalize())
Personal_info.append(lname.capitalize())
Personal_info.append(fname.upper())
Personal_info.append(lname.upper())
Personal_info.append(fname[0].upper())
Personal_info.append(lname[0].upper())


counter = int(0)
while counter < len(Personal_info):
    PI.append(Personal_info[counter])
    counter += 1

    
fcounter = int(-1)
while (fcounter+1) < len(Personal_info):
    fcounter += 1
    counter = int(0)
    while counter < len(Personal_info):
            PI.append (Personal_info[fcounter] + Personal_info[counter])
            counter += 1

fcounter = int(-1)
while (fcounter+1) < len(Personal_info):
    fcounter += 1
    counter=int(0)
    while counter < len(Custom_words):
            PI.append (Personal_info[fcounter] + Custom_words[counter])
            counter += 1

fcounter = int(-1)
while (fcounter+1) < len(Custom_words):
    fcounter += 1
    counter = int(0)
    while counter < len(Personal_info):
            PI.append (Custom_words[fcounter] + Personal_info[counter])
            counter += 1

fcounter = int(-1)
while (fcounter+1) < len(Personal_info):
    fcounter += 1
    counter=int(0)
    while counter < len(Custom_numbers):
            PI.append (Personal_info[fcounter] + Custom_numbers[counter])
            counter += 1

fcounter = int(-1)
while (fcounter+1) < len(Custom_numbers):
    fcounter += 1
    counter=int(0)
    while counter < len(Personal_info):
            PI.append (Custom_numbers[fcounter] + Personal_info[counter])
            counter += 1

fcounter = int(-1)
while (fcounter+1) < len(Personal_info):
    fcounter += 1
    counter=int(0)
    while counter < len(Backwards_numbers):
            PI.append (Personal_info[fcounter] + Backwards_numbers[counter])
            counter += 1

fcounter = int(-1)
while (fcounter+1) < len(Backwards_numbers):
    fcounter += 1
    counter=int(0)
    while counter < len(Personal_info):
            PI.append (Backwards_numbers[fcounter] + Personal_info[counter])
            counter += 1


Counter = int(0)
with open("Wordlist.txt", "a") as file:
    while Counter < len(PI):
        file.write (PI[Counter])
        file.write("\n")
        Counter += 1
file.close()
