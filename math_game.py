#!/usr/bin/env python

import os
from time import time
from random import randint
from datetime import datetime
import pickle
import bisect


ntimes = 10
subtraction = True
lo = 0
hi = 10
player_directory = "players"
highscore_fname = "highscores"

class Player:
    def __init__(self, name):
        self.name = name
        self.scores = list()

    def record_score(self, time):
        self.scores.append((datetime.now(), time))

    def print_recent_scores(self):
        num_scores = 10
        for date, score in self.scores[-num_scores:]:
            print("%s: %.2f seconds" % (date.strftime("%b %d"), score))

class HighScores:
    def __init__(self):
        self.scores = list()
        self.num_scores = 10

    def update(self, player, score):
        """Add a player's score to the list of high scores

        Return True if player got a high score, otherwise False
        """
        new_score = (score, player)
        if len(self.scores) < self.num_scores:
            self.scores.append(new_score)
            self.scores.sort()
            return True
        i = bisect.bisect(self.scores, new_score)
        if i < self.num_scores:
            self.scores.insert(i, new_score)
            self.scores.pop()
            return True
        else:
            return False

    def __str__(self):
        l = list()
        for i, score in enumerate(self.scores):
            l.append("%2d) %-15s %.2f sec" % (i+1, score[1].name, score[0]))
        return '\n'.join(l)

def load_scores():
    try:
        with open(highscore_fname, 'rb') as f:
            scores = pickle.load(f)
    except:
        scores = HighScores()
    return scores

def save_scores(scores):
    with open(highscore_fname, 'wb') as f:
        pickle.dump(scores, f)


def new_player(existing_players):
    while True:
        name = raw_input("Enter player name: ")
        if name in existing_players:
            print("That name is already taken.  Please enter another name.")
        elif name:
            return Player(name)

def select_player():
    player_list = list()
    try:
        player_list = os.listdir(player_directory)
        for i, name in enumerate(player_list):
            print("%2d: %s" % (i+1, name))
        num = int(raw_input("Select player (or leave empty for new player): "))
        name = player_list[num-1]
        with open(os.path.join(player_directory, name)) as f:
            return pickle.load(f)
    except:
        return new_player(player_list)

player = select_player()

os.system('clear')
print("Hello, %s!" % player.name)

def dump_player(player):
    with open(os.path.join(player_directory, player.name), 'wb') as f:
        pickle.dump(player, f)


score = 0
start = time()
while (score < ntimes):
    a = randint(lo,hi)
    b = randint(lo,hi)
    do_subtraction = subtraction and bool(randint(0,1))
    if do_subtraction:
        question = "%d - %d = " % (a + b, b)
        correct_answer = a
    else:
        question = "%d + %d = " % (a, b)
        correct_answer = a + b
    while True:
        try:
            ans = int(raw_input("%2d) " % (score + 1) + question))
            break
        except ValueError:
            print("Invalid input.  Please enter a number.")
    if ans == correct_answer:
        score += 1
    else:
        print("Oops.  The correct answer is %d." % correct_answer)
end = time()
elapsed = end - start
player.record_score(elapsed)
print("Total time: %.2f seconds" % elapsed)

highscores = load_scores()
got_high_score = highscores.update(player, elapsed)
if got_high_score:
    print("Congratulations! You got one of the %d fastest scores!" %
          highscores.num_scores)

print("\nHigh scores:")
print(highscores)
save_scores(highscores)
dump_player(player)

if (False):
    print("\nYour recent scores:")
    player.print_recent_scores()
