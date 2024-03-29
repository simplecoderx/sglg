def printInstructions(instruction):
    print(instruction)

def getUserScore(username):
    try:
        f = open ( 'game/userScore.txt', 'r')
        print("Exercise 1.2:\n")  
        for line in f:
            content = line.split(',')
            if content[0] == username:
                print("Exercise 1.2:\n",content[0], "has duplicate.")
                f.close()
                return 0
            display(content)      
        f.close()
    except IOError:
         print("File is not found. A new file will be created.")
         f = open('game/userScore.txt', 'w')
         f.write( 'Ann, 100\nBenny, 102\nDarren, 129\nCarol, 214')
         f.close()

def display(words):
        print(words[0], words[1])


sample = printInstructions("Exercise 1.1: This is printInstruction")
sample_again = getUserScore("Lynn")