import json

DATA_FILE = "scores.json"

def load_scores():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_scores(scores):
    with open(DATA_FILE, "w") as f:
        json.dump(scores, f, indent=2)

def add_player(scores):
    name = input("Enter player name: ").strip()
    if name not in scores:
        scores[name] = {"found": 0, "escaped": 0, "bonus": 0}
    else:
        print("Player already exists.")

def record_find(scores):
    finder = input("Who found the flag? ").strip()
    if finder in scores:
        scores[finder]["found"] += 2
    else:
        print("Player not found.")

def record_escape(scores):
    escaper = input("Whose flag escaped detection? ").strip()
    if escaper in scores:
        scores[escaper]["escaped"] += 3
    else:
        print("Player not found.")

def award_bonus(scores):
    player = input("Who deserves a bonus point? ").strip()
    if player in scores:
        scores[player]["bonus"] += 1
    else:
        print("Player not found.")

def show_scores(scores):
    print("\n🏆 Leaderboard")
    for player, points in scores.items():
        total = sum(points.values())
        print(f"{player}: {total} points (found: {points['found']}, escaped: {points['escaped']}, bonus: {points['bonus']})")

def main():
    scores = load_scores()
    while True:
        print("\n📋 MENU")
        print("1. Add player")
        print("2. Record flag found")
        print("3. Record successful hiding (escape)")
        print("4. Award bonus point")
        print("5. Show scores")
        print("6. Save & exit")
        choice = input("> ")
        if choice == "1":
            add_player(scores)
        elif choice == "2":
            record_find(scores)
        elif choice == "3":
            record_escape(scores)
        elif choice == "4":
            award_bonus(scores)
        elif choice == "5":
            show_scores(scores)
        elif choice == "6":
            save_scores(scores)
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
