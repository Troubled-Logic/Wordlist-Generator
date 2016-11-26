Word_list = []
Leet = []
Counter = int(0)

def L33T(Word):
    Word = Word.replace("a" or "A", "4")
    Word = Word.replace("e" or "E", "3")
    Word = Word.replace("g" or "G", "6")
    Word = Word.replace("i" or "I", "1")
    Word = Word.replace("o" or "O", "0")
    Word = Word.replace("s" or "S", "5")
    Word = Word.replace("t" or "T", "7")
    return (Word)

with open("Wordlist.txt", "r") as file:
    for line in file:
        Word_list.append(line.replace("\n", ""))
file.close()

while Counter < len(Word_list):
    Leet.append(L33T(Word_list[Counter]))
    Counter += 1
                         
print(len(Leet)*2, "words in this password list")

Counter = int(0)
with open ("Wordlist.txt", "a") as file:
    while Counter < len(Leet):
        file.write(Leet[Counter])
        file.write("\n")
        Counter += 1
file.close()
