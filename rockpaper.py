from random import randint

listChoice = ["Rock", "Paper", "Scissors"]

class player:
    #initial setting
    def __init__(self):
        self.choice = "None"
        self.score = 0
    #input receive and check
    def getInput(self, choice, run):
        zero = 0
        for x in range (3):
            if choice == listChoice[x]:
                zero = 1
        if zero == 0:
            print('Wrong Input')
            return run
        if zero == 1:
            print ('input accpeted')
            self.choice = choice
            return run
    #return the choice
    def returnChoice(self):
        return self.choice
    #check the plays
    def check(self, computerChoice):
        if self.choice != None:
            if self.choice == 'Rock' and computerChoice == 'Scissors':
                print ('You won!')
                self.score += 1
            if self.choice == 'Rock' and computerChoice == 'Paper':
                print ('You lose!')
                self.score -= 1
            if self.choice == 'Paper' and computerChoice == 'Rock':
                print ('You won!')
                self.score += 1
            if self.choice == 'Paper' and computerChoice == 'Scissors':
                print ('You lose!')
                self.score -= 1
            if self.choice == 'Scissors' and computerChoice == 'Paper':
                print ('You won!')
                self.score += 1
            if self.choice == 'Scissors' and computerChoice == 'Rock':
                print ('You lose!')
                self.score -= 1
            elif self.choice == computerChoice:
                print ('Draw.')
                self.score = self.score
    #return the score
    def returnScore(self):
        return self.score

player = player()

run = True
while run == True:
    print('Your choices are: \n"Rock"\n"Paper"\n"Scissors"')
    run = player.getInput(input('Enter your choice: '), run)
    if run == True:
        computerChoice = listChoice[randint(0,2)]
        print(f'Computer choice is {computerChoice}.')
        player.check(computerChoice)
        print(player.returnScore())
        choice = input('Wanna go another round? Y/N ')
        if choice.upper() == 'Y': 
            run = True
        else: 
            run == False
            break
    