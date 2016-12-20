"""
Model with equipment classes.
"""

__author__ = "ultravegan"


class _Equipment(object):
    def __init__(self, name):
        self.name = name


class _Weapon(_Equipment):
    pass


class _CloseCombatWeapon(_Weapon):
    pass


class _ShootingWeapon(_Weapon):
    pass


class _ArtilleryWeapon(_Weapon):
    pass


class _Armour(_Equipment):
    pass


class _SuitOfArmor(_Armour):
    pass


class _Shield(_Armour):
    pass


class _OtherProtections(_Armour):
    pass


class _MountProtection(_Armour):
    pass


class _InnateDefence(_Armour):
    pass


class HandWeapon(_CloseCombatWeapon):
    pass


class Flail(_CloseCombatWeapon):
    pass


class GreatWeapon(_CloseCombatWeapon):
    pass


class Halberd(_CloseCombatWeapon):
    pass


class PairedWeapon(_CloseCombatWeapon):
    pass


class Lance(_CloseCombatWeapon):
    pass


class LightLance(_CloseCombatWeapon):
    pass


class Spear(_CloseCombatWeapon):
    pass


class Bow(_ShootingWeapon):
    pass


class Longbow(_ShootingWeapon):
    pass


class Crossbow(_ShootingWeapon):
    pass


class Handgun(_ShootingWeapon):
    pass


class Pistol(_ShootingWeapon):
    pass


class ThrowingWeapon(_ShootingWeapon):
    pass


class BoltThrower(_ArtilleryWeapon):
    pass


class Cannon(_ArtilleryWeapon):
    pass


class Catapult(_ArtilleryWeapon):
    pass


class FlameThrower(_ArtilleryWeapon):
    pass


class VolleyGun(_ArtilleryWeapon):
    pass


class LightArmour(_SuitOfArmor):
    pass


class HeavyArmour(_SuitOfArmor):
    pass


class PlateArmour(_SuitOfArmor):
    pass


class Shield(_Shield):
    pass


class MountProtection(_MountProtection):
    pass


class Barding(_MountProtection):
    pass


class InnateDefence(_InnateDefence):
    pass
