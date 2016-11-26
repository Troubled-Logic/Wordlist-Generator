import os
Personal = []
Numbers = []
Words = []


def Write (File,List):
    with open (File, "a") as Output:
        Counter = int(0)
        while Counter < len(List):
            Output.write (List[Counter])
            Output.write ("\n")
            Counter += 1
    Output.close()

def Lister (Text):
    List = []
    Check = len(Text)-1
    if not Text[Check] == ",":
        Text += ","
        
    Counter = int(0)
    while not Text.strip() == "":
        if not Text[Counter] == ",":
            Counter += 1
        if Text[Counter] == ",":
            List.append (Text[0:Counter])
            Text = Text.replace (Text[0:Counter+1], "")
            Counter = int(0)
    return(List)


Fname = input("what is the first name \n")
Lname = input("what is the last name \n")
Bday = input("when were they born? dd/mm/yyyy \n")
Bday = Bday.replace("/", "")
Year = Bday[4:]
Personal.append (Fname)
Personal.append (Lname)
Personal.append (Bday)
Personal.append (Year)


Special_numbers = (input("Enter a number you would like to add followed by a ',' \nthen the next number 1,2,3,\n"))
Numbers = Lister(Special_numbers)

Special_words = input("Enter a word that you would like to add followed by a ',' \nthen the next word  e.g pass,secret, \n")
Words = Lister(Special_words)


Write ("Words.txt", Words)
Write ("Numbers.txt", Numbers)
Write ("Personal.txt", Personal)

print ("This may take a while .... \n")
os.system ('Mixer.py')
os.system ('Leet.py')

counter = int(0)
with open ("Wordlist.txt", 'r') as file:
    for line in file:
        counter += 1
file.close()

os.remove('Personal.txt')
os.remove('Words.txt')
os.remove('Numbers.txt')

print ("There is ", counter, " passwords have been generated \nThe file is called Wordlist.txt")
