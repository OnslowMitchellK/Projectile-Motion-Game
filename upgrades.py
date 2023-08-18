import pygame


class Upgrades:
    """
    In this class, all the basic upgrades data will be
    stored in this class. This will include the upgrades
    for the heroine/enemies e.g. increased player damage dealt,
    increased player health, decreased enemy shield, ect
    """
    def __init__(self, name, description, price):
        """
        This function is for each upgrade, it uses
        arguments to put data in each upgrade.
        """
        self.name = name
        self.description = description
        self.price = price


class SuperUpgrades:
    """
    In this class, all the super upgrades data will be
    stored in this class. This will include the the
    upgrades for the projectile e.g. projectile hitbox,
    different projectiles, ect.
    """
    def __init__(self, name, description, price):
        """
        This function is for each super upgrade, it uses
        arguments to put data in each super upgrade.
        """
        self.name = name
        self.description = description
        self.price = price


"Tough Gunk": "moreh eath",
"Slime Intimidation": "lowers eneimy shield"}
proj_hitbox_upgrade = SuperUpgrades(
                               "Super Slime Shooter",
                               """
                               Projecitle boiggr
                               """,
                               #price
                               )