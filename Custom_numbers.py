Custom_numbers = []
Custom_words = []
Backwards_numbers = []
PI = []


with open ("Custom_numbers.txt", 'r') as file:
    for line in file:
        Custom_numbers.append (line.replace("\n", ""))
file.close()

with open ("Custom_words.txt", 'r') as file:
    for line in file:
        Custom_words.append (line.replace("\n", ""))
file.close()

with open ("Backwards_numbers.txt", 'r') as file:
    for line in file:
        Backwards_numbers.append (line.replace("\n", ""))
file.close()


fcounter = int(0)
while fcounter < len(Custom_numbers):
    counter = int(0)
    while counter < len(Custom_numbers):
            PI.append (Custom_numbers[fcounter] + Custom_numbers[counter])
            counter += 1
    fcounter += 1

fcounter = int(0)
while fcounter < len(Backwards_numbers):
    counter = int(0)
    while counter < len(Custom_numbers):
            PI.append (Backwards_numbers[fcounter] + Custom_numbers[counter])
            counter += 1
    fcounter += 1

fcounter = int(0)
while fcounter < len(Custom_numbers):
    counter = int(0)
    while counter < len(Backwards_numbers):
            PI.append (Custom_numbers[fcounter] + Backwards_numbers[counter])
            counter += 1
    fcounter += 1
    
fcounter = int(0)
while fcounter < len(Backwards_numbers):
    counter = int(0)
    while counter < len(Backwards_numbers):
            PI.append (Backwards_numbers[fcounter] + Backwards_numbers[counter])
            counter += 1
    fcounter += 1

fcounter = int(0)
while fcounter < len(Custom_words):
    counter = int(0)
    while counter < len(Backwards_numbers):
            PI.append (Custom_words[fcounter] + Backwards_numbers[counter])
            counter += 1
    fcounter += 1

fcounter = int(0)
while fcounter < len(Backwards_numbers):
    counter = int(0)
    while counter < len(Custom_words):
            PI.append (Backwards_numbers[fcounter] + Custom_words[counter])
            counter += 1
    fcounter += 1

    
counter = int(0)
with open ("Wordlist.txt", "a") as file:
    while counter < len(PI):
        file.write (PI[counter])
        file.write("\n")
        counter += 1
file.close()
