def serve_chai():
    yield "Cup 1: Ginger Tea"
    yield "Cup 2: Lemon Tea"
    yield "Cup 3: Masala Tea"
    yield "Cup 4: Normal Tea"

stall = serve_chai()

for cup in stall:
    print(cup)

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()

print(next(chai))
print(next(chai))
print(next(chai))
# print(next(chai)) #This will throw an StopIteration error
