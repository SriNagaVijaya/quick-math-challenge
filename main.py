import random
import operator

high_score = 0

def errorHandle():
    while True:
        try:
            validated_guess = float(input('Please enter a valid number: '))
            return validated_guess
        except ValueError:
            print("Invalid input. Try a numeric value.")

def select_difficulty():
    print("\nChoose difficulty level:")
    print("1. Easy (1–10)")
    print("2. Medium (10–50)")
    print("3. Hard (50–100)")
    while True:
        choice = input("Enter 1, 2 or 3: ")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

def get_number_range(difficulty):
    if difficulty == 1:
        return (1, 10)
    elif difficulty == 2:
        return (10, 50)
    else:
        return (50, 100)

def random_problem(difficulty):
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    min_val, max_val = get_number_range(difficulty)
    num_1 = random.randint(min_val, max_val)
    num_2 = random.randint(min_val, max_val)
    operation = random.choice(list(operators.keys()))

    # Avoid division by zero
    if operation == '/' and num_2 == 0:
        num_2 = random.randint(1, max_val)

    answer = round(operators[operation](num_1, num_2), 2)
    print(f'\nWhat is {num_1} {operation} {num_2}?')
    return answer

def ask_question(difficulty):
    answer = random_problem(difficulty)
    try:
        guess = float(input('Your answer: '))
    except ValueError:
        guess = errorHandle()
    return round(guess, 2) == answer

def game():
    global high_score
    print("🎮 Welcome to the Math Quiz Game!")
    difficulty = select_difficulty()
    score = 0

    while True:
        if ask_question(difficulty):
            score += 1
            print('✅ Correct!\n')
        else:
            print('❌ Incorrect!\n')
            break

    print("======== Game Over ========")
    print(f'Your score: {score}')
    if score > high_score:
        high_score = score
        print("🏆 New High Score!")
    else:
        print(f'High score to beat: {high_score}')

    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again == 'y':
        game()
    else:
        print("Thanks for playing! 👋")

game()
