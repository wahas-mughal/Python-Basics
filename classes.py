# basic class
# class TestClass: 
#     test_var = (1,2,3)
#     another_var = 'something'
#     def test_func(self):
#         print('func in a class')
#         print(self.another_var)
#         self.another_func('123 ')
#     def another_func(self, test_param):
#         print(test_param)

# # create an instance
# test = TestClass()
# print(test.test_var)
# test.another_var = 'another value'
# print(test.another_var)

# test1 = TestClass();
# print(test1.another_var)
# test1.test_func()
# test1.another_func('test')

# mage class
# class Mage:
#     def __init__(self, health, mana):
#         self.health = health
#         self.mana =  mana
#         print('the mage class was created')
#         print(self.health)
    
    # def __len__(self):
    #     return self.mana

#     def attack(self, target):
#         target.health -= 10 

# class Monster:
#     health = 40

# mage = Mage(100, 200) 
# print(len(mage))
# monster = Monster()

# print(monster.health)
# mage.attack(monster)
# print(monster.health) 

# output: 
# 100
# 40
# 30

# Inheritance
# class Human:

#     def __init__(self, health):
#         self.health = health 

#     def attack(self):
#         print('attack')


# class Warriors(Human):
#     def __init__(self, health, defense):
#         super().__init__(health)
#         self.defense = defense
    
    # def attack(self):
    #     print('attack')

# class Barbarians(Human): 
#     def __init__(self, health, damage):
#         super().__init__(health)
#         self.damage = damage
    
    # def attack(self):
    #     print('attack')

# warrior = Warriors(50, 5.5)
# barbarians = Barbarians(100, 8.1)

# warrior.attack()
# barbarians.attack()
# print(warrior.health)
# print(barbarians.health)

# exercise
# class Entity:
#     def attack(self):
#         print(f'attack with {self.damage} damage')

# class Monster(Entity):
#     def __init__(self, health, damage):
#         self.health = health
#         self.damage = damage
    
#     def __repr__(self):
#         return f'a monster with {self.health} hp'

# monster = Monster(100, 50)
# print(monster.health) 
# monster.attack()

# print(monster)