forScores = input("write the sequence of scores in terms of ones and twos: ")

try:
    int(forScores)
except:
    print("You have entered letters.")
    print("Restart and try again.")

scores = ["Love", 15, 30, 40, "Deuce", "Advantage","has won"]

a = 0
b = 0
i = 0

print()
while not(((a == b+2) or (b == a+2)) and ((a >= 4) or (b >= 4))):   
    try:
        if forScores[i] == "1":
            i += 1
            a += 1
            if a == b and a >= 3:
                print(scores[4])
            elif a <= 3:
                print(f"{scores[a]} - {scores[b]}")
            elif a == b + 1:
                print(f"{scores[5]} for Player 1")
            else:
                print(f"Player 1 {scores[6]}")
        elif forScores[i] == "2":
            i += 1
            b += 1
            if b == a and b >= 3:
                print(scores[4])
            elif b <= 3:
                print(f"{scores[a]} - {scores[b]}")
            elif b == a + 1:
                print(f"{scores[5]} for Player 2")
            else:
                print(f"Player 2 {scores[6]}")
        else:
            print()
            print("You have entered a number which is not 1 nor 2.")
            print("Restart and try again.")
            break
    except:
        print()
        print("The game finished earlier than expected I guess")
        break