import os
Personal_info = []
Custom_numbers = []
Custom_words = []
Backwards_numbers = []
con = int(0)


fname = input("what is the first name \n")
lname = input("what is the last name \n")
bday = input("when were they born? dd/mm/yyyy \n")
bday = bday.replace("/", "")
year = bday[4:]
Personal_info.append (fname)
Personal_info.append (lname)
Personal_info.append (bday)
Personal_info.append (year)


Special_numbers = str(input("Enter a number you would like to add followed by a ',' \nthen the next number 1,2,3,\n"))
Check = len(Special_numbers)-1
if not Special_numbers[Check] == ",":
    Special_numbers += ","

Number_counter = (0)
while not Special_numbers.strip() == "":
    if not Special_numbers[Number_counter] == ",":
        Number_counter += 1

    if Special_numbers[Number_counter] == ",":
        Special_number = Special_numbers[0:Number_counter]
        Custom_numbers.append (Special_number)
        Backwards_number = Special_number [::-1]
        Special_number = Special_numbers[0:Number_counter+1]
        Special_numbers = Special_numbers.replace (Special_number, "")
        Number_counter = (0)
        Backwards_numbers.append (Backwards_number)
Custom_numbers.sort()


Special_words = input("Enter a word that you would like to add followed by a ',' \nthen the next word  e.g pass,secret, \n")
Check = len(Special_words)-1
if not Special_words[Check] == ",":
    Special_words += ","

    
Word_counter = (0)
while not Special_words.strip() == "":
    if not Special_words[Word_counter] == ",":
        Word_counter += 1
        
    if Special_words[Word_counter] == ",":
        Custom_word = Special_words[0:Word_counter]
        Custom_words.append (Custom_word)
        Custom_word = Special_words[0:Word_counter+1]
        Special_words = (Special_words.replace(Custom_word, ""))
        Word_counter = (0)


con = int(0)
with open ("Personal.txt",'w') as outputfile:
    while con < len(Personal_info):
        outputfile.write (Personal_info[con])
        outputfile.write ("\n")
        con += 1
outputfile.close()


con = int(0)
with open ("Backwards_numbers.txt",'w') as outputfile:
    while con < len(Backwards_numbers):
        outputfile.write (Backwards_numbers[con])
        outputfile.write ("\n")
        con += 1
outputfile.close()


con = int(0)
with open ("Custom_numbers.txt",'w') as outputfile:
    while con < len(Custom_numbers):
        outputfile.write (Custom_numbers[con])
        outputfile.write ("\n")
        con += 1
outputfile.close()


con = int(0)
with open ("Custom_words.txt",'w') as outputfile:
    while con < len(Custom_words):
        outputfile.write (Custom_words[con])
        outputfile.write ("\n")
        con += 1
outputfile.close()


print ("This may take a while .... \n")
os.system ('Personal.py')
os.system ('Custom_words.py')
os.system ('Custom_numbers.py')
os.system ('Leet module.py')

print ("Wordlist has been generated it is Custom_wordlist.txt")

counter = int(0)
with open ("Wordlist.txt", 'r') as file:
    for line in file:
        counter += 1
file.close()
print ("There is ", counter, " passwords in the list")
