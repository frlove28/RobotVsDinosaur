from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon

class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur("Rex the Dino", 200)
        self.robot = Robot("Barney the Robot", 10, Weapon("blaster", 45))


    def run_game(self):
        pass


    def display_welcome(self):
        print("Welcome to the Epic Battle!")


    def battle_phase (self):
        pass


    def display_winner (self):
        pass



