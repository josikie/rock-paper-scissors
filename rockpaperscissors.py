#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        index = random.randint(0, 2)
        return moves[index]


class HumanPlayer(Player):

    def move(self):
        while True:
            choose = input("rock, paper, scissors? > ")
            if choose == "quit()":
                exit()
            elif choose not in moves:
                pass
            else:
                return choose

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

        return [self.my_move, self.their_move]


class ReflectPlayer(Player):

    def __init__(self):
        super().__init__()
        self.my_move = ''
        self.their_move = ''

    def move(self, lastOpponent):
        if lastOpponent == '':
            index = random.randint(0, 2)
            return moves[index]
        else:
            return lastOpponent

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.my_move = ''
        self.their_move = ''

    def move(self, lastMove):
        if lastMove == '':
            index = random.randint(0, 2)
            return moves[index]
        elif lastMove == moves[0]:
            return moves[1]
        elif lastMove == moves[1]:
            return moves[2]
        elif lastMove == moves[2]:
            return moves[0]

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.scoreP1 = 0
        self.scoreP2 = 0

    def play_round(self):
        move1 = self.p1.move()
        # move2 = self.p2.move(self.p2.their_move)
        move2 = self.p2.move(self.p2.my_move)
        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2):
            print("** PLAYER ONE WINS ON THIS ROUND**")
            self.scoreP1 += 1
        elif beats(move2, move1):
            print("** PLAYER TWO WINS ON THIS ROUND**")
            self.scoreP2 += 1
        elif move1 == move2:
            print("** TIE **")
        print(f"Score: Player one: {self.scoreP1}, Player two: {self.scoreP2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()

        print("Game over!")
        print("Type quit() if you want to exit from the game \n\n")


if __name__ == '__main__':
    while True:
        game = Game(HumanPlayer(), CyclePlayer())
        game.play_game()
