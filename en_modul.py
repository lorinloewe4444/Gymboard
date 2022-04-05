def get_animals(n):
    animals=["Tiger","Elefant","Känguru","Steinadler"]
    if n>len(animals)-1:
        n=len(animals)-1
    return str(animals[:n])
