from bst import *
#from binary_search_tree import *
def test_BSTree_set():
    #colors = BSTree()
    colors = Tree()
    colors.set("Cad", "Cad Red")
    assert colors.root.value == "Cad Red"
    colors.set("Cad", "Cadmium Red")
    assert colors.root.key == "Cad"
    assert colors.root.value == "Cadmium Red"
    assert colors.root.left == None
    assert colors.root.right == None
    colors.set("Pthalo", "Pthalo Blue")
    assert colors.root.right.key == "Pthalo"
    colors.set("Aliz", "Alizarin Crimson")
    assert colors.root.left.key == "Aliz"
    assert colors.root.left.left == None
    assert colors.root.right.right == None
    colors.set("green", "greenish")
    colors.set("blue", "blueish")
    return colors

def test_BSTree_get():
    colors = test_BSTree_set()
    assert colors.get("Cad") == "Cadmium Red"
    assert colors.get("Pthalo") == "Pthalo Blue"
    assert colors.get("Aliz") == "Alizarin Crimson"
    assert colors.get("red") == None
    assert colors.get("blue") == "blueish"
#
def test_list():
    colors = test_BSTree_set()
    colors.list()

def test_delete():
    colors = test_BSTree_set()
    colors.set("Gamb", "New Gamboge")
    assert colors.get("Gamb") == "New Gamboge"
    colors.delete("Pthalo")
    assert colors.get("Pthalo") == None
    assert colors.get("Gamb") == "New Gamboge"
    colors.delete("Aliz")
    assert colors.get("Aliz") == None

    colors = test_BSTree_set()
    colors.set("Gamb", "New Gamboge")
    colors.set("Prus", "Prussian Blue")
    colors.delete("Pthalo")
    assert colors.get("Gamb") == "New Gamboge"
    assert colors.get("Prus") == "Prussian Blue"
    colors.delete("Gamb")
    assert colors.get("Gamb") == None
    assert colors.get("Prus")
    colors.delete("Prus")
    assert colors.get("Prus") == None
    colors.delete("Cad")
    assert colors.root.key == "Aliz"
