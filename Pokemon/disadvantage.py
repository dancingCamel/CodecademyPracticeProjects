def disadvantage(pok1, pok2):
    if pok1._type == "Fire" and pok2._type == "Water":
        return True

    if pok1._type == "Grass" and pok2._type == "Fire":
        return True

    if pok1._type == "Water" and pok2._type == "Grass":
        return True

    return False
