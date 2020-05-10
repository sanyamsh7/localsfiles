from que import *

def test_shift():
    colors = Queue()
    colors.shift("Pthalo Blue")
    assert colors.count() == 1
    colors.shift("Ultramarine Blue")
    assert colors.count() == 2
    assert colors.count() == 2

def test_unshift():
    colors = Queue()
    colors.shift("Magenta")
    colors.shift("Alizarin")
    assert colors.unshift() == "Magenta"
    assert colors.unshift() == "Alizarin"
    assert colors.unshift() == None
    assert colors.count() == 0
