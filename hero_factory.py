from python_practice.ez import EZ
from python_practice.jinx import Jinx
from python_practice.police import Police
from python_practice.timo import Timo


class HeroFactory:
    """
    简单工厂模式专门定义一个类来负责创建其他类型的英雄的实例
    """
    def creat_hero(self, name):
        if name == "Jinx":
            return Jinx()
        elif name == "EZ":
            return EZ()
        elif name == "Timo":
            return Timo()
        elif name == "Police":
            return Police()
        else:
            raise ("not in HeroFactory")

hero_factory = HeroFactory()
jinx = hero_factory.creat_hero("Jinx")
ez = hero_factory.creat_hero("EZ")

jinx.fight(ez.hp, ez.power)
timo = hero_factory.creat_hero("Timo")
police = hero_factory.creat_hero("Police")
timo.speak_lines()
police.speak_lines()


