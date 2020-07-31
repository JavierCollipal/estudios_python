class CatGun:
    balas = 0

    def __init__(self, balas):
        self.balas = balas

    def fire(self):
        print(f"te disparo con todas estas balas {self.balas}")
