def get_scores():
    """Collect and return scores between 0 and 100."""
    scores = []

    while True:
        score_input = input(
            "Enter a score from 0 to 100 "
            "(type 'done' when finished): "
        ).strip()

        if score_input.lower() == "done":
            return scores

        try:
            score = float(score_input)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 0 <= score <= 100:
            scores.append(score)
        else:
            print("The score must be between 0 and 100.")


def main():
    users = []

    while True:
        name = input("\nEnter a name (type 'exit' to quit): ").strip()

        if name.lower() == "exit":
            break

        if not name:
            print("The name cannot be empty.")
            continue

        try:
            age = int(input("Enter an age: "))
        except ValueError:
            print("Please enter a whole number for age.")
            continue

        if age < 0:
            print("Age cannot be negative.")
            continue

        scores = get_scores()
        average = sum(scores) / len(scores) if scores else 0

        users.append({
            "name": name,
            "age": age,
            "scores": scores,
            "average": average,
        })
        print(f"{name} was added.")

    print("\n--- User Records ---")

    if not users:
        print("No users were entered.")
    else:
        for user in users:
            print(f"\nName: {user['name']}")
            print(f"Age: {user['age']}")
            print("Scores:")

            if user["scores"]:
                for score in user["scores"]:
                    print(f"  {score:g}")
            else:
                print("  No scores entered.")

            print(f"Average: {user['average']:.1f}")

    print("\nExiting the program. Goodbye!")


if __name__ == "__main__":
    main()