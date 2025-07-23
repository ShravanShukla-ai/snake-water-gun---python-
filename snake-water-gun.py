snake-water-gun - python
import random

# 0 - Snake, 1 - Water, 2 - Gun
choices = ['snake', 'water', 'gun']

# Winner matrix: rows = user, columns = computer
# U = User wins, C = Computer wins, D = Draw
winner_matrix = [
    ['D', 'U', 'C'],  # User: Snake
    ['C', 'D', 'U'],  # User: Water
    ['U', 'C', 'D']   # User: Gun
]

def get_result(user_choice, comp_choice):
    return winner_matrix[user_choice][comp_choice]

print("\n🐍 SNAKE - WATER 💧 - GUN 🔫 GAME (Matrix Version)")
print("===================================================")

rounds = 5
user_score = 0
comp_score = 0

for round in range(rounds):
    print(f"\nRound {round+1} of {rounds}")
    for idx, val in enumerate(choices):
        print(f"{idx} - {val}")
    try:
        user_input = int(input("Enter your choice (0/1/2): "))
        if user_input not in [0, 1, 2]:
            print("Invalid input! Try again.")
            continue
    except:
        print("Please enter a valid number.")
        continue

    comp_input = random.randint(0, 2)
    print(f"Computer chose: {choices[comp_input]}")

    result = get_result(user_input, comp_input)

    if result == 'U':
        print("✅ You win this round!")
        user_score += 1
    elif result == 'C':
        print("❌ Computer wins this round!")
        comp_score += 1
    else:
        print("😐 It's a draw!")

print("\n🏁 Final Scores:")
print(f"You: {user_score} | Computer: {comp_score}")
if user_score > comp_score:
    print("🎉 Congratulations! You Won!")
elif user_score < comp_score:
    print("😔 Computer Won! Better luck next time.")
else:
    print("🤝 It's a Tie!")

