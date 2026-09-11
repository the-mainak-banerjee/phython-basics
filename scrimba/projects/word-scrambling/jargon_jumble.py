import random

word_bank = [
    ("standup", "Every morning, our fifteen-minute ____ meeting lasts until lunch."),
    ("syntax", "One missing bracket, and Python hits me with a ____ error."),
    (
        "debug",
        "I spent four hours trying to ____ my code. Turns out I was missing comma.",
    ),
    ("deploy", "It's Friday at 5pm, definitely the best time to ____ new code."),
    ("bandwidth", "Sorry boss, I can't take on more work. I just don't have the ____."),
    ("meeting", "That ninety-minute ____ could have been an email."),
    (
        "deadline",
        "Of course we'll hit the ____, no problem! Well, within a couple of days. Maybe a week.",
    ),
    ("backup", "We finally made a ____ of everything, the day after the laptop died."),
    ("server", "I'm getting a 500 error, which means the ____ is down again."),
    (
        "prototype",
        "It's just an early ____, so please ignore that clicking anywhere crashes it.",
    ),
]

print("~" * 40)
print()
print("   Welcome to Jargon Jumble!")
print("   A Tech-Themed Word Scramble Game")
print()
print("~" * 40)

# words = ["Deadline", "Urgent", "Client"]
# random_word = random.choice(words)
played_words = []
ROUND = 5
round = 1
score = 0

while round <= ROUND:
    random_word, hint = random.choice(word_bank)

    while (random_word, hint) in played_words:
        random_word, hint = random.choice(word_bank)

    played_words.append((random_word, hint))

    random_word_list = list(random_word)
    random.shuffle(random_word_list)
    shuffled_word = "".join(random_word_list)

    print(f"Welcome to Round {round}")
    print()
    print(f"Your word is {shuffled_word.upper()}")
    print()

    user_guess = (
        input("Please guess the word or type 'skip' / 'hint' / 'quit': ")
        .strip()
        .lower()
    )

    if user_guess == "hint":
        print(hint)
        user_guess = input("Enter your guess now or 'skip' / 'quit': ").strip().lower()

    if user_guess == "quit":
        print("Thanks for playing")
        break

    if user_guess == "skip":
        print(f"Skipped the word was '{random_word.lower()}'.\n")
    elif user_guess == random_word.lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Sorry, the word was '{random_word.lower()}'.\n")

    round += 1

print()
print(f"Final Score: {score}/{ROUND}")
print()

if score == 5:
    print("Flawless! All tests passing, zero bugs.")
elif score == 4:
    print("Near perfect, only one failing test!")
elif score == 3:
    print("Good effort! The code runs, and that's what counts.")
else:
    print("Have you tried turning it off and on again?")
