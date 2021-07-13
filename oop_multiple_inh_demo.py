class Santa:
    def __init__(self):
        print("Santa")
    def sing(self):
        print("sing a song by santa")
    def fight(self):
        print("figt by santa")

class Banta:
    def __init__(self):
        print("Banta")

    def sing(self):
        print("sing a song by banta")
    def heal(self):
        print("heal by banta")

class SantaBanta(Banta,Santa):
    # def __init__(self):
    #     print("---------SantaBanta-------")

    def callSingForSanta(self):
        Santa.sing(self)

sb = SantaBanta()
sb.fight()
sb.heal()
sb.sing()
sb.callSingForSanta()