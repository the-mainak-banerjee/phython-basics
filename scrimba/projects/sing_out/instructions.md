## Challenge A: Get the App Running

The app has show_queue stubbed and the "quit" command wired up. 
Two more functions need stubs, and the loop only handles "quit" so far.

1. Stub add_singer and remove_singer, following the show_queue example: each takes
   queue, has a one-sentence docstring, and prints a placeholder like "[add a singer]".

2. Finish the if/elif/else chain. When the command is "add" or
   "remove", call the matching function.

3. Add an else that handles when the app receives an unrecognized command (see the example below).

4. Call run_app(queue) and test it. Make sure add, remove, and quit each work, and that
  typing a command that doesn't exist, like "sing", prints your message and doesn't
  crash the app.

Example output:

============================================
Welcome to Sing Out: A Karaoke Queue Manager
============================================

[the queue goes here]

Options: add / remove / quit
 > add

[add a singer]

> sing

Sorry, I don't know the command 'sing'.

> quit

The queue is closed. Good night!

----------------------------------------------------
## Challenge B: Display the Queue
Replace show_queue()'s placeholder code with working code: 
1. Add a header that says "Current Queue:". Give it some visual space by adding a blank
   line above and below.
2. Loop over the queue and print each singer's name and song. 
3. Move the options menu into show_queue(), since we want to keep display items together and show the options menu each time we show the queue. 

Example output:

============================================
Welcome to Sing Out: A Karaoke Queue Manager
============================================

Current Queue:

Annie - Dancing Queen
Allen - Country Roads

Options: add / remove / quit
>

----------------------------------------------------
## Challenge C: Add a Singer
Adding a singer is two separate tasks: 1) prompt the host for a name and a song, and
2) append that singer to the queue. Write a function for each:

1. Write prompt_for_singer():
   - Ask the host for a name and a song
   - The function should return the name and the song, title cased and stripped of any extra spaces
   - A function can return two values at once if you separate them with a comma:
     `return name, song`. You unpack them the same way you would a tuple. 

2. Fill in the add_singer() function:
   - Call prompt_for_singer(), unpack what comes back, and save to variables
   - Add the singer and their song to the end of the queue
   - Print a message confirming the singer was added

Example output: 

Current Queue:

Annie - Dancing Queen
Allen - Country Roads

Options: add / remove / quit
> add

Name:    mike reed
Song: LET IT BE

Added Mike Reed to the queue.

Current Queue:

Annie - Dancing Queen
Allen - Country Roads
Mike Reed - Let It Be

----------------------------------------------------
## Challenge D: Remove a Singer
Find the singer in the queue and remove them. 

In the `remove_singer()` function: 
1. Prompt the host for who to remove. Clean the input: title-cased, no extra spaces. 
2. Loop through the queue looking for a matching singer name. Each singer is a (name, song) tuple, so compare against the name inside the tuple rather than the tuple itself. Check hints.md
   if you need help!
3. If you find a match, remove the whole tuple with .remove(), print a confirmation and return.
4. If the loop finishes without a match, print a message telling the host no match was found. 

Example output:

> remove
Who do you want to remove? allen

Removed Allen from the queue.

> remove
Who do you want to remove? sarah

There's no one named Sarah in the queue.

----------------------------------------------------
## Challenge E: 
1. Update show_queue() so the list is always numbered.
2. Print each singer with their number, starting at 1 (hint: you can do math inside of an f string).
3. Try adding and removing several singers from the list to make sure the numbering stays consistent. 

Example output:
Current Queue:
1. Annie - Dancing Queen
2. Allen - Country Roads
Options: add / remove / quit

----------------------------------------------------
## Challenge F: Call the Next Singer

1. Write next_singer(queue). Take the singer off the front of the queue with .pop(),
   and save the return value. 
2. pop() returns the whole tuple, not just the name. Unpack that singer into a name and a song, and announce that they're next.
3. Add "next" to the options menu and make sure next_singer() is called when a user types "next".

Example output:

Current Queue:

1. Annie - Dancing Queen
2. Allen - Country Roads

Options: add / next / remove / quit
> next

NOW UP: Annie — Dancing Queen

Current Queue:

1. Allen - Country Roads

----------------------------------------------------
## Challenge F: Move a Singer to the Top of the Queue

Moving a singer to the top is two steps:
 1) take them out of their current position, and
 2) insert them at the beginning of the queue.

1. Write move_to_top(queue):
   - Ask the host which position they want to move, and convert their answer to a number
   - Take that singer out of the queue with .pop(). Watch for an off-by-one error: the queue starts at 1 for the host, but Python starts counting at 0, so position 1 is
     index 0. Pass the host's number minus one as the argument to .pop()
   - Put the singer back at the front of the queue with .insert()
   - Print a message announcing who moved to the top

2. Call move_to_top in the app loop so the host can run the command, and add "top" to the Options menu.

Here's what your output should look like:

Current Queue:

1. Annie - Dancing Queen
2. Allen - Country Roads

Options: add / next / top / remove / quit
> top

Who do you want to move to the top? Enter a number: 2

Moved Allen to the top of the queue!

Current Queue:

1. Allen - Country Roads
2. Annie - Dancing Queen


----------------------------------------------------
## Challenge G: Add guard clauses

Expected outputs
### Condition: the queue is empty:
```
The queue is currently empty.

Options: add / next / top / remove / quit
```

### Condition: attempt to move a singer to the top of the queue when there are fewer than two singers:
```
> top

You need at least two singers in the queue to move someone to the top.
```

### Condition: Trying to move a singer to the top of the queue with a position that doesn't exist:

> top

Who do you want to move to the top? Enter a number: 5

There's no singer at position 5.

### Condition: enter a blank name or song:

```
> add

Name:
Song:

Oops! I need a name and a song to add someone to the queue.
```

### Condition: remove singer on an empty queue.
> remove

Oops! There's no one left to remove!

The queue is currently empty.

Options: add / next / top / remove / quit
```
----------------------------------------------------

## Challenge H: Validate User Input

When trying to move a singer to the top of the queue, the app will crash if the user enters input that can't be converted to an integer. Use try/except to handle the error.

Expected output:

> top
Who do you want to move to the top? Enter a number: two

Please enter a number.

> top
Who do you want to move to the top? Enter a number: 2

Moved Allen to the top of the queue!