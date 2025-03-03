from at_tut_1 import Person

def test_combat():
    boxer = Person("Boxer", 100, 10)
    zombie = Person("Zed", 1000, 1000)

    # Assert initial health
    assert boxer.hp == 100, "Boxer should start with 100 HP."
    assert zombie.hp == 1000, "Zombie should start with 1000 HP."

    # Boxer attacks zombie
    boxer.hit(zombie)
    assert zombie.alive(), "Zombie should still be alive."

    # Zombie attacks boxer
    zombie.hit(boxer)
    assert not boxer.alive(), "Boxer should be dead."