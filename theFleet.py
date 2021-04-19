from robots import robot

class the_Fleet:
    i = 0
    j = 0

    robot_one = robot()
    robot_one.get_name(i)
    robot_one.get_Weapon(j)
    robot_one.set_attack_damage()
    i = i + 1
    j = j + 1
    robot_two = robot()
    robot_two.get_name(i)
    robot_two.get_Weapon(j)
    robot_two.set_attack_damage()
    i = i + 1
    j = j + 1
    robot_three = robot()
    robot_three.get_name(i)
    robot_three.get_Weapon(j)
    robot_three.set_attack_damage()
    i = 0
    j = 0
