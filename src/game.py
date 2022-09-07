from gameround import GameRound
from participant import Participant


class Game:
    def __init__(self):
        self.endGame = False
        self.firstParticipant = Participant("Spock")
        self.secondParticipant = Participant("Kirk")

    def start(self):
        while not self.endGame:
            game_round = GameRound(self.firstParticipant, self.secondParticipant)
            self.checkEndCondition()

    def checkEndCondition(self):
        answer = input("Continue playing? y/n: ")
        if answer == "y":
            GameRound(self.firstParticipant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print("Game ended, {p1name} has {p1points} point(s) and {p2name} has {p2points} point(s)".format(p1name=self.firstParticipant.name, 
            p1points=self.firstParticipant.points, p2name=self.secondParticipant.name, p2points=self.secondParticipant.points))
            self.determineWinner()
            self.endGame = True

    def determineWinner(self):
        resultString = "It's a draw"
        if self.firstParticipant.points > self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.firstParticipant.name)
        elif self.firstParticipant.points < self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.secondParticipant.name)
        print(resultString)
