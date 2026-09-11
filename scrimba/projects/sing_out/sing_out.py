queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]
# queue = []

def show_queue(queue):
    """Print everyone currently in the queue"""
    if len(queue) == 0:
        print()
        print("The queue is currently empty.")
    else:
        print()
        print("Current Queue:")
        print()
        
        # The enumerate function will return the index as well.
        for idx, performance in enumerate(queue):
            singer, song = performance
            print(f"{idx + 1}. {singer} - {song}")
        
    print()
    print("Options: add / next / top / remove / quit")


def prompt_for_singer():
    name = input("Name: ").strip().title()
    song = input("Song: ").strip().title()
    return (name, song)


def add_singer(queue):
    """This will add a singer to queue"""
    name, song = prompt_for_singer()
    if not name or not song:
        print("Oops! I need a name and a song to add someone to the queue.")
        return
    queue.append((name, song))
    print()
    print(f"Added {name} to the queue.")


def remove_singer(queue):
    """This will remove a singer from the queue"""

    if len(queue) == 0:
        print()
        print("Oops! There's no one left to remove!")
        return
    
    singer_name = input("Who do you want to remove? ").strip().title()

    if singer_name == "":
        print("Please provide a name to remove")
        return

    for singer in queue:
        # Here rather than unpacking the tuple we can also use index to access the name like this singer[0]
        name, _ = singer
        if singer_name == name:
            queue.remove(singer)
            print()
            print(f"Removed {name} from the queue")
            return
    print()
    print(f"There is no one named {singer_name} in the queue.")


def next_singer(queue):
    if len(queue) == 0:
        print()
        print("Oops! There's no one left to call up!")
        return
    # It remove an element from the list and return it
    name, song = queue.pop(0)
    print()
    print(f"NOW UP: {name} - {song}")

def move_to_top(queue):
    if len(queue) <= 1:
        print()
        print("You need at least two singers in the queue to move someone to the top.")
        return

    try:
        singer_position = int(input("Who do you want to move to the top? Enter a number: "))
    except ValueError:
        print("Please enter a number")
        return

    if singer_position <1 or singer_position > len(queue):
        print()
        print(f"There's no singer at position {singer_position}.")
        return

    singer = queue.pop(singer_position - 1)
    queue.insert(0, singer)

    print()
    print(f"Moved {singer[0]} to the top of the queue")

def run_app(queue):
    print("=" * 44)
    print("Welcome to Sing Out: A Karaoke Queue Manager")
    print("=" * 44)

    is_running = True

    while is_running:
        show_queue(queue)
        command = input("> ").strip().lower()

        if command == "quit":
            is_running = False
            print("The queue is closed. GoodNight!")
        elif command == "add":
            add_singer(queue)
        elif command == "remove":
            remove_singer(queue)
        elif command == "next":
            next_singer(queue)
        elif command == "top":
            move_to_top(queue)
        else:
            print(f"Sorry, I don't know the command '{command}'.")


run_app(queue)
