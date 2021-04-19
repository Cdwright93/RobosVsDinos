# import random
from theHerd import the_Herd
from theFleet import the_Fleet

robots_alive = 3
dinosaurs_alive = 3
robots = [the_Fleet.robot_one, the_Fleet.robot_two, the_Fleet.robot_three]
dinosaurs = [the_Herd.raptor_One, the_Herd.raptor_Two, the_Herd.raptor_Three]

while robots_alive > 0 and dinosaurs_alive > 0:
    dinosaurs[0].hp = dinosaurs[0].hp - robots[0].attack_damage
    dinosaurs[1].hp = dinosaurs[1].hp - robots[1].attack_damage
    dinosaurs[2].hp = dinosaurs[2].hp - robots[2].attack_damage
    robots[0].hp = robots[0].hp - dinosaurs[0].attack_damage
    robots[0].hp = robots[0].hp - dinosaurs[0].attack_damage
    robots[0].hp = robots[0].hp - dinosaurs[0].attack_damage
    if dinosaurs[0].hp <= 0:
        dinosaurs_alive = dinosaurs_alive - 1
    if dinosaurs[1].hp <= 0:
        dinosaurs_alive = dinosaurs_alive - 1
    if dinosaurs[2].hp <= 0:
        dinosaurs_alive = dinosaurs_alive - 1
    if robots[0].hp <= 0:
        robots_alive = robots_alive - 1
    if robots[1].hp <= 0:
        robots_alive = robots_alive - 1
    if robots[2].hp <= 0:
        robots_alive = robots_alive - 1

if robots_alive <= 0:
    print("DINOSAURS WIN")
if dinosaurs_alive <= 0:
    print("ROBOTS WIN")
