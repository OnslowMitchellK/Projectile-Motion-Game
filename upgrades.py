"""This is a file containing all the upgrades name, description and price."""

import pygame
COST = 1


class Upgrades:
    """
    This class holds all the data for the basic upgrades.

    In this class, all the basic upgrades data will be
    stored in this class. This will include the upgrades
    for the player/enemies e.g. increased player damage dealt,
    increased player health, decreased enemy shield, ect
    """

    def __init__(self, name, description, price) -> None:
        """
        Set the variables.

        This function is for each upgrade, it uses
        arguments to put data in each player upgrade.
        """
        self.name = name
        self.description = description
        self.price = price

    def dict_return(self):
        return {self.name: [self.description, self.price]}


class SuperUpgrades:
    """
    This class holds all the data for each super upgrade.

    In this class, all the super upgrades data will be
    stored in this class. This will include the upgrades
    for the projectile e.g. projectile hitbox, different
    projectiles, ect.
    """

    def __init__(self, name, description, price) -> None:
        """
        Set the variables.

        This function is for each super upgrade, it uses
        arguments to put data in each projectile upgrade.
        """
        self.name = name
        self.description = description
        self.price = price
    
    def dict_return(self):
        return {self.name: [self.description, self.price]}


bigger_proj_upgrade = SuperUpgrades(
                                    "Super Slime Shooter",
                                    """
                                    With the Super Slime Shot ability, your
                                    trusty slimeball projectiles undergo a
                                    mesmerizing transformation - upon
                                    purchase, their hitbox drastically
                                    expands, packing more squishy wallop
                                    into each shot.
                                    """,
                                    COST
                                    ).dict_return()
arrow_proj_upgrade = SuperUpgrades(
                                   "Slobin Hood",
                                   """
                                   Drawing power from the legendary archer
                                   'Robin Hood', witness the mesmerizing
                                   metamorphosis as your slimeball evolves
                                   into a swift and lethal arrow. This
                                   significantly amplifies the damage dealt
                                   to enimies, turning your attacks into
                                   devastating blows that send foes reeling.
                                   """,
                                   COST
                                   ).dict_return()
cannon_proj_upgrade = SuperUpgrades(
                                    "Steel Slime",
                                    """
                                    Prepare to witness the awe-inspiring
                                    transformation of your slimeball as it
                                    evolves into a mighty cannonball, only to
                                    be coated in a layer of viscous, sticky
                                    slime. Engage in this thrilling upgrade
                                    and establish yourself as a force to be
                                    reckoned with, leaving behind a trail of
                                    astonished enemies struggling to break
                                    free.
                                    """,
                                    COST
                                    ).dict_return()
increase_hp_upgrade = Upgrades(
                               "Tough Gunk",
                               """
                               No longer a mere puddle of gelatinous
                               substance, you now possess a formidable
                               and robust constitution. This upgraded
                               toughness empowers you to withstand even
                               the most ferocious of attacks, shrugging
                               off blows that once would have brought you
                               to your metaphorical knees. Your enemies
                               will be astonished as they struggle to deal
                               with your newfound endurance.
                               """,
                               COST
                               ).dict_return()
decrease_hp_upgrade = Upgrades(
                               "Sticky Sickness",
                               """
                               Plunge your foes into a world of discomfort
                               with the 'Sticky Sickness' ability. Upon
                               purchasing, a malevolent aura engulfs your
                               enemies, afflicting them with an insidious
                               ailment that gradually saps their health.
                               As the name suggests, this affliction clings
                               to them like an inescapable mire, leaving
                               them weakened and vulnerable.
                               """,
                               COST
                               ).dict_return()
increase_luck_upgrade = Upgrades(
                                 "Blessing of the Slime God",
                                 """
                                 As you receive the Blessing of the Slime God,
                                 an aura of fortunate energy envelops you,
                                 guiding your steps and steering fate in your
                                 favor. Embrace this divine gift and watch as
                                 your enemies' frustration grows with each near
                                 miss. Engage in battles with newfound
                                 confidence, knowing that the Blessing of the
                                 Slime God has your back, turning once perilous
                                 encounters into triumphs of improbable odds.
                                 """,
                                 COST
                                 ).dict_return()
def_lower_upgrade = Upgrades(
                             "Slime Intimidation",
                             """
                             Slime intimidation, a fearsome ability that
                             empowers you to unleash a monstrous roar,
                             sending shockwaves through the battlefield.
                             As the soundwaves ripple outward, the defenses
                             of your enemies weaken, leaving them vulnerable
                             and exposed. Your commanding presence and primal
                             power strike at the heart of their confidence.
                             """,
                             COST
                             ).dict_return()
atk_lower_upgrade = Upgrades(
                             "Slimy Solution",
                             """
                             Prepare to wield the power of gooey innovation
                             as you coat your adversaries in a specialized
                             slime solution, drastically reducing their
                             ability to launch fierce attacks. Embrace the
                             tactical prowess of the slimy solution as you
                             witness enemies struggle against the restraints
                             of the slime solution. Engage with newfound
                             confidence, knowing that you've turned their
                             offensive might into a controllable force.
                             """,
                             COST
                             ).dict_return()
small_char_upgrade = Upgrades(
                              "Slime Splitter",
                              """
                              When confronted with adversaries, a slime can
                              cleverly divide itself into multiple smaller
                              entities. This ingenious maneuver not only
                              bewilders opponents but also significantly
                              shrinks the slime's hitbox, rendering it a
                              much more challenging target to strike.
                              """,
                              COST
                              ).dict_return()

upgrades = [increase_hp_upgrade, increase_luck_upgrade, def_lower_upgrade, atk_lower_upgrade, small_char_upgrade]
super_upgrades = [bigger_proj_upgrade, arrow_proj_upgrade, cannon_proj_upgrade]