import exception

__all__ = ["_Equipment", "_Weapon", "_CloseCombatWeapon", "_ShootingWeapon", "_ArtilleryWeapon", "_Armour",
           "_SuitOfArmor", "_Shield", "_OtherProtections", "_MountProtection", "_InnateDefence", "Barding",
           "BoltThrower", "Bow", "Crossbow", "Flail", "FlameThrower", "GreatWeapon", "Halberd", "Handgun", "HandWeapon",
           "HeavyArmour", "InnateDefence", "Lance", "LightArmour", "LightLance", "Longbow", "MountProtection",
           "PairedWeapon", "Pistol", "PlateArmour", "Shield", "Spear", "ThrowingWeapon", "VolleyGun"]

"""
Model with equipment classes.
"""

__author__ = "ultravegan"


class _Equipment(object):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


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
    def __init__(self, *args, **kwargs):
        super(HandWeapon, self).__init__("Hand Weapon", *args, **kwargs)


class Flail(_CloseCombatWeapon):
    def __init__(self, *args, **kwargs):
        super(Flail, self).__init__("Flail", *args, **kwargs)


class GreatWeapon(_CloseCombatWeapon):
    def __init__(self, *args, **kwargs):
        super(GreatWeapon, self).__init__("Great Weapon", *args, **kwargs)


class Halberd(_CloseCombatWeapon):
    def __init__(self, *args, **kwargs):
        super(Halberd, self).__init__("Halberd", *args, **kwargs)


class PairedWeapon(_CloseCombatWeapon):
    def __init__(self, *args, **kwargs):
        super(PairedWeapon, self).__init__("Paired Weapon", *args, **kwargs)


class Lance(_CloseCombatWeapon):
    def __init__(self, *args, **kwargs):
        super(Lance, self).__init__("Lance", *args, **kwargs)


class LightLance(_CloseCombatWeapon):
    def __init__(self, *args, **kwargs):
        super(LightLance, self).__init__("Light Lance", *args, **kwargs)


class Spear(_CloseCombatWeapon):
    def __init__(self, *args, **kwargs):
        super(Spear, self).__init__("Spear", *args, **kwargs)


class Bow(_ShootingWeapon):
    def __init__(self, *args, **kwargs):
        super(Bow, self).__init__("Bow", *args, **kwargs)


class Longbow(_ShootingWeapon):
    def __init__(self, *args, **kwargs):
        super(Longbow, self).__init__("Longbow", *args, **kwargs)


class Crossbow(_ShootingWeapon):
    def __init__(self, *args, **kwargs):
        super(Crossbow, self).__init__("Crossbow", *args, **kwargs)


class Handgun(_ShootingWeapon):
    def __init__(self, *args, **kwargs):
        super(Handgun, self).__init__("Handgun", *args, **kwargs)


class Pistol(_ShootingWeapon):
    def __init__(self, *args, **kwargs):
        super(Pistol, self).__init__("Pistl", *args, **kwargs)


class ThrowingWeapon(_ShootingWeapon):
    def __init__(self, *args, **kwargs):
        super(ThrowingWeapon, self).__init__("Throwing Weapon", *args, **kwargs)


class BoltThrower(_ArtilleryWeapon):
    def __init__(self, *args, **kwargs):
        super(BoltThrower, self).__init__("Bolt Thrower", *args, **kwargs)


class Cannon(_ArtilleryWeapon):
    def __init__(self, *args, **kwargs):
        super(Cannon, self).__init__("Cannon", *args, **kwargs)


class Catapult(_ArtilleryWeapon):
    def __init__(self, *args, **kwargs):
        super(Catapult, self).__init__("Catapult", *args, **kwargs)


class FlameThrower(_ArtilleryWeapon):
    def __init__(self, *args, **kwargs):
        super(FlameThrower, self).__init__("Flame Thrower", *args, **kwargs)


class VolleyGun(_ArtilleryWeapon):
    def __init__(self, *args, **kwargs):
        super(VolleyGun, self).__init__("Volley Gun", *args, **kwargs)


class LightArmour(_SuitOfArmor):
    def __init__(self, *args, **kwargs):
        super(LightArmour, self).__init__("Light Armour", *args, **kwargs)


class HeavyArmour(_SuitOfArmor):
    def __init__(self, *args, **kwargs):
        super(HeavyArmour, self).__init__("Heavy Armour", *args, **kwargs)


class PlateArmour(_SuitOfArmor):
    def __init__(self, *args, **kwargs):
        super(PlateArmour, self).__init__("Plate Armour", *args, **kwargs)


class Shield(_Shield):
    def __init__(self, *args, **kwargs):
        super(Shield, self).__init__("Shield", *args, **kwargs)


class MountProtection(_MountProtection):
    def __init__(self, *args, **kwargs):
        super(MountProtection, self).__init__("Mount Protection", *args, **kwargs)


class Barding(_MountProtection):
    def __init__(self, *args, **kwargs):
        super(Barding, self).__init__("Barding", *args, **kwargs)


class InnateDefence(_InnateDefence):
    def __init__(self, *args, **kwargs):
        super(InnateDefence, self).__init__("Innate Defence", *args, **kwargs)
