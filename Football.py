matches = input("Match outcomes: ")
bets = input("Bets: ")
won = 0
for i in range(15):
    if matches[i] == bets[i]:
        won += 1
print(won)