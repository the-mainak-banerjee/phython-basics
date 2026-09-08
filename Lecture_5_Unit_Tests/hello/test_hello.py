from hello import hello

def test_hello_default():
    assert hello() == "hello, world"

def test_hello_arg():
    assert hello("Alice") == "hello, Alice"
    assert hello("Bob") == "hello, Bob"
