from modulos import what_is_a_module, what_is_a_package
from modulos import Cat
from funcional import test_basic_reduce
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
catSolid = CatSolid("lanita", 29, "angora", 4, catGun)

catSolid.meow()
catSolid.shot_cat_gun()
catSolid.leg_count()

test_basic_reduce()
