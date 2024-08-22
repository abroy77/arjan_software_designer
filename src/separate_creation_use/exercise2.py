from dataclasses import dataclass
from enum import StrEnum
from random import randint, choice
from abc import ABC, abstractmethod


class EnemyType(StrEnum):
    KNIGHT = "knight"
    ARCHER = "archer"
    WIZARD = "wizard"


@dataclass
class Enemy:
    enemy_type: EnemyType
    health: int
    attack_power: int
    defense: int


class EnemyFactory(ABC):
    @abstractmethod
    def spawn(self) -> Enemy:
        pass


class EasyEnemyFactory(EnemyFactory):
    def spawn(self) -> Enemy:
        # needs low numbers
        health = randint(20, 40)
        attack_power = randint(10, 20)
        defense = randint(5, 10)
        enemy_type = choice([EnemyType.KNIGHT, EnemyType.ARCHER])

        return Enemy(enemy_type, health, attack_power, defense)


class MediumEnemyFactory(EnemyFactory):
    def spawn(self) -> Enemy:
        # needs medium numbers
        health = randint(40, 60)
        attack_power = randint(30, 50)
        defense = randint(15, 25)
        enemy_type = choice([EnemyType.KNIGHT, EnemyType.ARCHER, EnemyType.WIZARD])

        return Enemy(enemy_type, health, attack_power, defense)


class HardEnemyFactory(EnemyFactory):
    def spawn(self) -> Enemy:
        # needs high numbers
        health = randint(70, 90)
        attack_power = randint(50, 70)
        defense = randint(35, 55)
        enemy_type = choice([EnemyType.WIZARD])

        return Enemy(enemy_type, health, attack_power, defense)


def main() -> None:
    easy_factory = EasyEnemyFactory()
    for _ in range(5):
        enemy = easy_factory.spawn()
        print(enemy)

    medium_factory = MediumEnemyFactory()
    for _ in range(5):
        enemy = medium_factory.spawn()
        print(enemy)

    hard_factory = HardEnemyFactory()
    for _ in range(5):
        enemy = hard_factory.spawn()
        print(enemy)


if __name__ == "__main__":
    main()
