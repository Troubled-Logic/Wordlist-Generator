Numbers = []
Words = []
Backwards = []
PI = []

def Add (First, Second):
    PI = []
    counter = int(0)
    while counter < len(First):
        Counter = int(0)
        while Counter < len(Second):
            Pass = First[counter] + Second[Counter]
            PI.append(Pass)
            Counter += 1
        counter += 1
    return (PI)

def Read (File):
    List = []
    with open (File, "r") as Output:
        for Line in Output:
            List.append(Line.replace ("\n", ""))
    Output.close()
    return (List)

def Write (File,List):
    with open (File, "a") as Output:
        Counter = int(0)
        while Counter < len(List):
            Output.write (List[Counter])
            Output.write ("\n")
            Counter += 1
    Output.close()

Numbers = Read("Numbers.txt")
Words = Read("Words.txt")
Personal = Read("Personal.txt")

Counter = int(0)
while Counter < len(Numbers):
    Back = Numbers[Counter]
    Backwards.append (Back [::-1])
    Counter +=1


PI = PI + (Add(Numbers, Numbers))
PI = PI + (Add(Numbers, Backwards))
PI = PI + (Add(Numbers, Words))
PI = PI + (Add(Numbers, Personal))
PI = PI + (Add(Backwards, Numbers))
PI = PI + (Add(Backwards, Backwards))
PI = PI + (Add(Backwards, Words))
PI = PI + (Add(Backwards, Personal))
PI = PI + (Add(Words, Numbers))
PI = PI + (Add(Words, Backwards))
PI = PI + (Add(Words, Words))
PI = PI + (Add(Words, Personal))
PI = PI + (Add(Words, Add(Words, Words)))
PI = PI + (Add(Words, Add(Words, Numbers)))
PI = PI + (Add(Words, Add(Words, Backwards)))
PI = PI + (Add(Words, Add(Words, Personal)))
PI = PI + (Add(Words, Add(Personal, Words)))
PI = PI + (Add(Personal, Personal))
PI = PI + (Add(Personal, Words))
PI = PI + (Add(Personal, Numbers))
PI = PI + (Add(Personal, Backwards))
PI = PI + (Add(Personal, Add(Words, Numbers)))
PI = PI + (Add(Personal, Add(Words, Backwards)))
PI = PI + (Add(Personal, Add(Personal, Numbers)))
PI = PI + (Add(Personal, Add(Personal, Backwards)))

Write("Wordlist.txt", PI)

