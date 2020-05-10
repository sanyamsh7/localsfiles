from nose.tools import *
from ex47.game import Room

def test_room():
    gold = Room("GoldRoom",
                """ This room has gold in it you can grab. There's a door
                       to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})
    assert_equal(gold.description,""" This room has gold in it you can grab. There's a door
                       to the north.""")

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east').go('down'), down)
    assert_equal(start.go('down').go('up'), start)
    
def test_weapon():
    weapon1 = Room('fight_soldiers', 'you have to fight the soldiers here.')
    weapon1.add_weapon(["knife", "gun", "sword"])

    assert_equal(weapon1.acquire_weapon(0), "KNIFE")
    assert_equal(weapon1.acquire_weapon(1), "gun")
    assert_equal(weapon1.acquire_weapon(2), "sword")
