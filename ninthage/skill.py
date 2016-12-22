__all__ = ["_Skill", "Ambush", "Fear", "Accurate"]


class _Skill(object):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class Accurate(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Accurate, self).__init__("Accurate", *args, **kwargs)


class Ambush(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Ambush, self).__init__("Ambush", *args, **kwargs)


class Area Attack(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Area
        Attack, self).__init__("Area Attack", *args, **kwargs)


class Armour Piercing(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Armour
        Piercing, self).__init__("Armour Piercing", *args, **kwargs)


class Breath Weapon(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Breath
        Weapon, self).__init__("Breath Weapon", *args, **kwargs)


class Cannot March(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Cannot
        March, self).__init__("Cannot March", *args, **kwargs)


class Channel(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Channel, self).__init__("Channel", *args, **kwargs)


class Crush Attack(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Crush
        Attack, self).__init__("Crush Attack", *args, **kwargs)


class Daemonic Instability(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Daemonic
        Instability, self).__init__("Daemonic Instability", *args, **kwargs)


class Devastating Charge(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Devastating
        Charge, self).__init__("Devastating Charge", *args, **kwargs)


class Distracting(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Distracting, self).__init__("Distracting", *args, **kwargs)


class Divine Attacks(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Divine
        Attacks, self).__init__("Divine Attacks", *args, **kwargs)


class Engineer(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Engineer, self).__init__("Engineer", *args, **kwargs)


class Ethereal(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Ethereal, self).__init__("Ethereal", *args, **kwargs)


class Fast Cavalry(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Fast
        Cavalry, self).__init__("Fast Cavalry", *args, **kwargs)


class Fear(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Fear, self).__init__("Fear", *args, **kwargs)


class Fight in Extra Rank(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Fight in Extra
        Rank, self).__init__("Fight in Extra Rank", *args, **kwargs)


class Fireborn(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Fireborn, self).__init__("Fireborn", *args, **kwargs)


class Flaming Attacks(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Flaming
        Attacks, self).__init__("Flaming Attacks", *args, **kwargs)


class Flammable(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Flammable, self).__init__("Flammable", *args, **kwargs)


class Fly(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Fly, self).__init__("Fly", *args, **kwargs)


class Frenzy(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Frenzy, self).__init__("Frenzy", *args, **kwargs)


class Grinding Attacks(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Grinding
        Attacks, self).__init__("Grinding Attacks", *args, **kwargs)


class Hard Target(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Hard
        Target, self).__init__("Hard Target", *args, **kwargs)


class Hatred(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Hatred, self).__init__("Hatred", *args, **kwargs)


class Hellfire(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Hellfire, self).__init__("Hellfire", *args, **kwargs)


class Hold Your Ground(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Hold
        Your
        Ground, self).__init__("Hold Your Ground", *args, **kwargs)


class Immune to Psychology(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Immune
        to
        Psychology, self).__init__("Immune to Psychology", *args, **kwargs)


class Impact Hits(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Impact
        Hits, self).__init__("Impact Hits", *args, **kwargs)


class Insignificant(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Insignificant, self).__init__("Insignificant", *args, **kwargs)


class Inspiring Presence(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Inspiring
        Presence, self).__init__("Inspiring Presence", *args, **kwargs)


class Lethal Strike(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Lethal
        Strike, self).__init__("Lethal Strike", *args, **kwargs)


class Light Troops(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Light
        Troops, self).__init__("Light Troops", *args, **kwargs)


class Lightning Attack(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Lightning
        Attack, self).__init__("Lightning Attack", *args, **kwargs)


class Lightning Reflexes(_Skill):
    def __init__(self, *args, **kwargs):
        supersuper(Lightning
        Reflexes, self).__init__("Lightning Reflexes", *args, **kwargs)
