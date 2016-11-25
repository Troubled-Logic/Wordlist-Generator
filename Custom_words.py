Custom_words = []
Custom_numbers = []
PI = []

with open ("Custom_words.txt", 'r') as file:
    for line in file:
        Custom_words.append (line.replace("\n", ""))
file.close()

with open ("Custom_numbers.txt", 'r') as file:
    for line in file:
        Custom_numbers.append (line.replace("\n", ""))
file.close()


fcounter = int(0)
while fcounter < len(Custom_words):
    counter = int(0)
    while counter < len(Custom_numbers):
            PI.append (Custom_words[fcounter] + Custom_numbers[counter])
            counter += 1
    fcounter += 1

fcounter = int(0)
while fcounter < len(Custom_numbers):
    counter = int(0)
    while counter < len(Custom_words):
            PI.append (Custom_numbers[fcounter] + Custom_words[counter])
            counter += 1
    fcounter += 1

fcounter = int(0)
while fcounter < len(Custom_words):
    counter = int(0)
    while counter < len(Custom_words):
            PI.append (Custom_words[fcounter] + Custom_words[counter])
            counter += 1
    fcounter += 1

counter = int(0)
with open ("Wordlist.txt", "a") as file:
    while counter < len(PI):
        file.write (PI[counter])
        file.write ("\n")
        counter += 1
file.close()
