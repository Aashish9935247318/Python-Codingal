import random

print("🏏 REALISTIC CRICKET GAME 🏏")
print("=" * 35)

player_score = 0
computer_score = 0
player_wickets = 0
computer_wickets = 0

OVERS = 2
BALLS_PER_OVER = 6

# ---------------- PLAYER BATTING ----------------

print("\nYou are batting!")
print("Choose: 1 = Defensive, 2 = Normal, 3 = Attack")

for over in range(OVERS):
    for ball in range(BALLS_PER_OVER):

        if player_wickets >= 2:
            break

        print(f"\nOver {over + 1}.{ball + 1}")
        print(f"Score: {player_score}/{player_wickets}")

        choice = input("Your shot (1/2/3): ")

        if choice not in ["1", "2", "3"]:
            print("Invalid shot!")
            continue

        # Different shots have different risks
        if choice == "1":
            possible_runs = [0, 0, 1, 1, 2]
            wicket_chance = 0.05

        elif choice == "2":
            possible_runs = [0, 1, 1, 2, 3, 4]
            wicket_chance = 0.10

        else:
            possible_runs = [0, 2, 4, 4, 6]
            wicket_chance = 0.20

        if random.random() < wicket_chance:
            player_wickets += 1
            print("💥 OUT!")
        else:
            runs = random.choice(possible_runs)
            player_score += runs

            if runs == 6:
                print("🔥 SIX!")
            elif runs == 4:
                print("🏏 FOUR!")
            else:
                print(f"You scored {runs} run(s).")

print("\n" + "=" * 35)
print(f"Your final score: {player_score}/{player_wickets}")

# ---------------- COMPUTER BATTING ----------------

print("\n🤖 Computer is batting!")

target = player_score + 1

for over in range(OVERS):
    for ball in range(BALLS_PER_OVER):

        if computer_wickets >= 2:
            break

        if computer_score >= target:
            break

        print(f"\nOver {over + 1}.{ball + 1}")
        print(f"Computer: {computer_score}/{computer_wickets}")

        # Computer chooses a random shot
        shot = random.randint(1, 3)

        if shot == 1:
            possible_runs = [0, 0, 1, 1, 2]
            wicket_chance = 0.05

        elif shot == 2:
            possible_runs = [0, 1, 1, 2, 3, 4]
            wicket_chance = 0.10

        else:
            possible_runs = [0, 2, 4, 4, 6]
            wicket_chance = 0.20

        if random.random() < wicket_chance:
            computer_wickets += 1
            print("🎯 You got the computer OUT!")

        else:
            runs = random.choice(possible_runs)
            computer_score += runs

            if runs == 6:
                print("🤖 Computer hit a SIX!")
            elif runs == 4:
                print("🤖 Computer hit a FOUR!")
            else:
                print(f"Computer scored {runs} run(s).")

print("\n" + "=" * 35)
print(f"Computer final score: {computer_score}/{computer_wickets}")

# ---------------- RESULT ----------------

print("\n🏆 MATCH RESULT 🏆")

if player_score > computer_score:
    print("🎉 YOU WIN!")
    print(f"You won by {player_score - computer_score} runs.")

elif computer_score > player_score:
    print("😢 COMPUTER WINS!")
    print(f"Computer won by {computer_score - player_score} runs.")

else:
    print("🤝 MATCH DRAW!")