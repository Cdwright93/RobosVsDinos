class robot:
    def __init__(self):
        self.name = ''
        self.hp = 225
        self.attack_damage = ''
        self.weapon = ''
        self.position = ''

    def get_name(self, i):
        robot_names = ['Dome-o', 'Gat-o', 'Mr. Roboto']
        if i == 0:
            self.name = robot_names[0]
        if i == 1:
            self.name = robot_names[1]
        if i == 2:
            self.name = robot_names[2]

    def get_Weapon(self, j):
        weapon_names = ['Sword', 'Nunchaku', 'Cannon']
        if j == 0:
            self.weapon = weapon_names[0]
        if j == 1:
            self.weapon = weapon_names[1]
        if j == 2:
            self.weapon = weapon_names[2]

    def set_attack_damage(self):
        if self.weapon == 'Sword':
            self.attack_damage = 40
        if self.weapon == 'Nunchaku':
            self.attack_damage = 40
        if self.weapon == 'Cannon':
            self.attack_damage = 60

