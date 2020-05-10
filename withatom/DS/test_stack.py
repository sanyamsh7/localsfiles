#from stack import *
from test import *
def test_push():
    bundle = Stack()
    assert bundle.count() == 0
    bundle.push("register")
    assert bundle.count() == 1
    bundle.push("diary")
    assert bundle.count() == 2
    bundle.push("photo_album")
    assert bundle.count() == 3

def test_pop():
    bundle = Stack()
    bundle.push("register")
    bundle.push("diary")
    bundle.push("photo_album")
    assert bundle.pop() == "photo_album"
    assert bundle.count() == 2
    assert bundle.pop() == "diary"
    assert bundle.count() == 1
    assert bundle.pop() == "register"
    assert bundle.count() == 0
    assert bundle.pop() == None
    assert bundle.count() == 0

def test_top():
    bundle = Stack()
    assert bundle.first() == None
    assert bundle.pop() == None
    bundle.push("register")
    assert bundle.first() == "register"
    bundle.push("diary")
    assert bundle.first() == "diary"
    assert bundle.count() == 2
    bundle.pop()
    assert bundle.count() == 1
    assert bundle.first() == "register"
    bundle.pop()
    bundle.pop()
    assert bundle.first() ==  None

def test_count():
    bundle = Stack()
    bundle.push("register")
    bundle.push("diary")
    assert bundle.count() == 2
    bundle.pop()
    assert bundle.count() == 1
    bundle.pop()
    assert bundle.count() == 0
    bundle.pop()
    bundle.pop()
    assert bundle.count() == 0
