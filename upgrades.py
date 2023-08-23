"""This is a file containing all the upgrades name, description and price."""

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
    Summary.

    This class holds all the data for each super upgrade.

    Description.

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


#Tough Gunk": "moreh eath",
proj_hitbox_upgrade = SuperUpgrades(
                                    "Super Slime Shooter",
                                    """
                                    With the Super Slime Shot ability, your
                                    trusty slimeball projectiles undergo a
                                    mesmerizing transformation - upon
                                    purchase, their hitbox drastically
                                    expands, packing more squishy wallop
                                    into each shot.
                                    """,
                                    #price
                                    )
def_lower_upgrade = Upgrades("Slime Intimidation",
                             """
                             Slime intimidation, a fearsome ability that
                             empowers you to unleash a monstrous roar,
                             sending shockwaves through the battlefield.
                             As the soundwaves ripple outward, the defenses
                             of your enemies weaken, leaving them vulnerable
                             and exposed. Your commanding presence and primal
                             power strike at the heart of their confidence.
                             """
                             #price
                             )
