from modulos import what_is_a_module, what_is_a_package
from modulos import Cat
from oop import CatSolid
from oop import CatGun
from operadores import sum_two_numbers

what_is_a_module()
what_is_a_package()
sum_two_numbers(1, 2)

catObject = Cat()

catObject.meow()

catGun = CatGun(6)
# Le doy un arma a este gato para que pueda disparar
catSolid = CatSolid(catGun)

catSolid.meow()
catSolid.shot_cat_gun()
catSolid.leg_count()
