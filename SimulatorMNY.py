import random
import sys
sys.setrecursionlimit(10000000)

wins = 0
losses = 0

def win():
        print("\nYou Win!\n")
        global wins
        wins = wins + 1
        print(f"Total Number of wins: {wins}")
        print(f"Total Number of losses: {losses}")
        Bops()
        

def lose():
        print("\nYou Lose!\n")
        print(f"Total Number of wins: {wins}")
        global losses 
        losses = losses + 1
        print(f"Total Number of losses: {losses}")
        Bops()

def ops(n):
        while True:
            print("\nRolling Dice...")
            d2 = 0 
            for i in range(2):
                d2 += random.randint(1, 8)
            print(f"Your number: {d2}")

            x = n
            y = 10
            
            if (d2 == x):
                win()
            if (d2 == y):
                lose()
            else:
                ops(n)

def Bops(): 
        while True:
            print("\nRolling Dice...")
            total = 0
            for i in range(2):
                total += random.randint(1, 8)
            print(f"Your number: {total}")

            a = [4, 6, 10]
            b = [9, 13]
            c = [2, 3, 5, 7, 8, 11, 12, 14, 15, 16]

            if any(total == i for i in a):
                win()
            if any(total == i for i in b):
                lose()
            if any(total == i for i in c):
                print("OPS has occured.")
                ops(total)

for n in range(10):
    Bops()
quit()
