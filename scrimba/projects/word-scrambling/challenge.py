# Challenge A: Scramble a Word
# 1. Create a game file named `jargon_jumble.py`
# 2. Create a list of at least 3 words and save to a variable called `words`
# 3. Use random.choice() to pick a word from the list
# 4. Use list(), random.shuffle(), and "".join() to scramble the word
# 5. Print the scrambled word

# ------------------------------------------------
# Challenge B: Check if the Guess Is Correct
# Add interactivity so a player
# can either a) skip the word and get the correct answer or b) guess the word and find out if they're correct.

# 1. Prompt the player for input and give them two options: type a guess or type 'skip' to skip the word.
# 2. Use string methods to clean the player's guess and improve the display:
#    - We want to be as forgiving as we can with the player's guess. Clean the player's guess so that capitalization and white space don't matter when comparing to the correct answer.
#    - Display the scrambled word in all caps so it stands out on screen.
# 3. Use if/elif/else to handle three cases:
#    - Player types "skip": Skipped! The word was 'apple'.
#    - Player's guess is correct: ✅ Correct!
#    - Player's guess is incorrect: ❌ Sorry, the word was 'apple'.

# Challenge C: Let the Player Ask for a Hint
# The word_bank below pairs each word with a hint. Wire up a 'hint' option
# so a stuck player can reveal the clue and then keep guessing.

# 1. Pick a random pair from word_bank and unpack it into word and hint.
# 2. Update the guess prompt so the player knows 'hint' is now an option.
# 3. If the player types 'hint', show them the hint, then ask them to guess again.
#    * Hint: this will require adding a second input prompt!
#    * Hint: keep the 'hint' check in its own separate if, above the
#      skip/correct/wrong block. Skip, correct, and wrong all end the turn,
#      but a hint doesn't. Keeping it separate lets the game show the hint
#      and then still check the guess the player types next.
# 4. Optional: add a couple of your own word/hint pairs to the bank.

# Challenge D: Add a Game Loop
# Right now the game ends after a single word. Add the ability to play multiple rounds and quit out of the game at any point.

# 1. Wrap the game code in a loop that runs for 5 rounds.
# 2. Display the round number at the beginning of each round.
# 3. Give the player a way to quit early by typing 'quit'.
#    * Hint: you'll want to break out of the loop when they do.


# Challenge E: Avoid Repeating Words
# Ensure that a word shows up no more than once per game.
# 1. Outside the game loop, make an empty list called `used` to track already used (word, hint) pairs.
# 2. Inside the game loop, write another loop that checks if the picked (word, hint) pair is already in `used`, and keeps re-picking until it finds an unused pair.
# 3. Once a fresh pair is found, append it to `used` so it won't come up again.
# 4. Test your game to make sure it plays five unique words.

# Challenge F: Track the Score
# Tell the player their score and how they did!
# 1. Before the loop, set up a `score` variable to count correct guesses. Initalize to 0.
# 2. Each time the player guesses correctly, increment the score by one.
# 3. Once the game ends, show a final score out of the total rounds. Example: "Final score: 3/5"
# 4. Use an if/elif/else chain to give fun feedback based on their score. Here's an example output, but feel free to write your own:
#    A score of 5: "Flawless! All tests passing, zero bugs."
#    A score of 4: "Near perfect, only one failing test!"
#    A score of 3: "Good effort! The code runs, and that's what counts."
#    A score under 3: "Have you tried turning it off and on again?"