from character import Gnome, Orc

# Use exactly this 'MAIN'
# This code must run correctly, producing the showed output.
orc1 = Orc()
orc2 = Orc()
gnome1 = Gnome()
gnome2 = Gnome()
print('orc1 energy:', orc1.energy)
print('orc2 energy:', orc2.energy)
print('gnome1 energy:', gnome1.energy)
print('gnome2 energy:', gnome2.energy)
print('gnome1 eats 10')
#gnome1.eat(10)
print('gnome1 energy:', gnome1.energy)

"""
The output is:
orc1 energy: 200
orc2 energy: 200
gnome1 energy: 100
gnome2 energy: 100
gnome1 eats 10
gnome1 energy: 110
"""


## ATTACK
print('\n \n')
print('\nWhen an orc attacks an orc, they both lose 10 energy points.')
print('orc1 energy:', orc1.energy, '- orc2 energy:', orc2.energy)
print('ATTACK!')
orc1.attack(orc2)
print('orc1 energy:', orc1.energy, '- orc2 energy:', orc2.energy)
print('\nWhen a gnome attacks a gnome, they both lose 7 points of energy.')
print('gnome1 energy:', gnome1.energy, '- gnome2 energy:', gnome2.energy)
print('ATTACK!')
gnome1.attack(gnome2)
print('gnome1 energy:', gnome1.energy, '- gnome2 energy:', gnome2.energy)
print('\nWhen an orc attacks a gnome, the gnome loses 5 points and the orc 1 point.')
print('gnome1 energy:', gnome1.energy, '- orc1 energy:', orc1.energy)
print('ATTACK!')
orc1.attack(gnome1)
print('gnome1 energy:', gnome1.energy, '- orc1 energy:', orc1.energy)
print('\nWhen a gnome attacks an orc, the orc loses 3 points and the gnome 2 points.')
print('gnome1 energy:', gnome1.energy, '- orc1 energy:', orc1.energy)
print('ATTACK!')
gnome1.attack(orc1)
print('gnome1 energy:', gnome1.energy, '- orc1 energy:', orc1.energy)


"""
When an orc attacks an orc, they both lose 10 energy points.
orc1 energy: 200 - orc2 energy: 200
ATTACK!
orc1 energy: 190 - orc2 energy: 190
When a gnome attacks a gnome, they both lose 7 points of energy.
gnome1 energy: 100 - gnome2 energy: 100
ATTACK!
gnome1 energy: 93 - gnome2 energy: 93
When an orc attacks a gnome, the gnome loses 5 points and the orc 1 point.
gnome1 energy: 93 - orc1 energy: 190
ATTACK!
gnome1 energy: 88 - orc1 energy: 189
When a gnome attacks an orc, the orc loses 3 points and the gnome 2 points.
gnome1 energy: 88 - orc1 energy: 189
ATTACK!
gnome1 energy: 86 - orc1 energy: 186
"""