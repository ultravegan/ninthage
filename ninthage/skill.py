__all__ = ["_Skill", "Ambush", "Fear", "Accurate"]


class _Skill(object):
    def __init__(self, name, *args, **kwargs):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class Accurate(_Skill):
    def __init__(self, *args, **kwargs):
        super(Accurate, self).__init__("Accurate", *args, **kwargs)


class Ambush(_Skill):
    def __init__(self, *args, **kwargs):
        super(Ambush, self).__init__("Ambush", *args, **kwargs)


class AreaAttack(_Skill):
    def __init__(self, *args, **kwargs):
        super(AreaAttack, self).__init__("AreaAttack", *args, **kwargs)


class ArmourPiercing(_Skill):
    def __init__(self, *args, **kwargs):
        super(ArmourPiercing, self).__init__("ArmourPiercing", *args, **kwargs)


class BreathWeapon(_Skill):
    def __init__(self, *args, **kwargs):
        super(BreathWeapon, self).__init__("BreathWeapon", *args, **kwargs)


class CannotMarch(_Skill):
    def __init__(self, *args, **kwargs):
        super(CannotMarch, self).__init__("CannotMarch", *args, **kwargs)


class Channel(_Skill):
    def __init__(self, *args, **kwargs):
        super(Channel, self).__init__("Channel", *args, **kwargs)


class CrushAttack(_Skill):
    def __init__(self, *args, **kwargs):
        super(CrushAttack, self).__init__("CrushAttack", *args, **kwargs)


class DaemonicInstability(_Skill):
    def __init__(self, *args, **kwargs):
        super(DaemonicInstability, self).__init__("DaemonicInstability", *args, **kwargs)


class DevastatingCharge(_Skill):
    def __init__(self, *args, **kwargs):
        super(DevastatingCharge, self).__init__("DevastatingCharge", *args, **kwargs)


class Distracting(_Skill):
    def __init__(self, *args, **kwargs):
        super(Distracting, self).__init__("Distracting", *args, **kwargs)


class DivineAttacks(_Skill):
    def __init__(self, *args, **kwargs):
        super(DivineAttacks, self).__init__("DivineAttacks", *args, **kwargs)


class Engineer(_Skill):
    def __init__(self, *args, **kwargs):
        super(Engineer, self).__init__("Engineer", *args, **kwargs)


class Ethereal(_Skill):
    def __init__(self, *args, **kwargs):
        super(Ethereal, self).__init__("Ethereal", *args, **kwargs)


class FastCavalry(_Skill):
    def __init__(self, *args, **kwargs):
        super(FastCavalry, self).__init__("FastCavalry", *args, **kwargs)


class Fear(_Skill):
    def __init__(self, *args, **kwargs):
        super(Fear, self).__init__("Fear", *args, **kwargs)


class FightinExtraRank(_Skill):
    def __init__(self, *args, **kwargs):
        super(FightinExtraRank, self).__init__("FightinExtraRank", *args, **kwargs)


class Fireborn(_Skill):
    def __init__(self, *args, **kwargs):
        super(Fireborn, self).__init__("Fireborn", *args, **kwargs)


class FlamingAttacks(_Skill):
    def __init__(self, *args, **kwargs):
        super(FlamingAttacks, self).__init__("FlamingAttacks", *args, **kwargs)


class Flammable(_Skill):
    def __init__(self, *args, **kwargs):
        super(Flammable, self).__init__("Flammable", *args, **kwargs)


class Fly(_Skill):
    def __init__(self, *args, **kwargs):
        super(Fly, self).__init__("Fly", *args, **kwargs)


class Frenzy(_Skill):
    def __init__(self, *args, **kwargs):
        super(Frenzy, self).__init__("Frenzy", *args, **kwargs)


class GrindingAttacks(_Skill):
    def __init__(self, *args, **kwargs):
        super(GrindingAttacks, self).__init__("GrindingAttacks", *args, **kwargs)


class HardTarget(_Skill):
    def __init__(self, *args, **kwargs):
        super(HardTarget, self).__init__("HardTarget", *args, **kwargs)


class Hatred(_Skill):
    def __init__(self, *args, **kwargs):
        super(Hatred, self).__init__("Hatred", *args, **kwargs)


class Hellfire(_Skill):
    def __init__(self, *args, **kwargs):
        super(Hellfire, self).__init__("Hellfire", *args, **kwargs)


class HoldYourGround(_Skill):
    def __init__(self, *args, **kwargs):
        super(HoldYourGround, self).__init__("HoldYourGround", *args, **kwargs)


class ImmunetoPsychology(_Skill):
    def __init__(self, *args, **kwargs):
        super(ImmunetoPsychology, self).__init__("ImmunetoPsychology", *args, **kwargs)


class ImpactHits(_Skill):
    def __init__(self, *args, **kwargs):
        super(ImpactHits, self).__init__("ImpactHits", *args, **kwargs)


class Insignificant(_Skill):
    def __init__(self, *args, **kwargs):
        super(Insignificant, self).__init__("Insignificant", *args, **kwargs)


class InspiringPresence(_Skill):
    def __init__(self, *args, **kwargs):
        super(InspiringPresence, self).__init__("InspiringPresence", *args, **kwargs)


class LethalStrike(_Skill):
    def __init__(self, *args, **kwargs):
        super(LethalStrike, self).__init__("LethalStrike", *args, **kwargs)


class LightTroops(_Skill):
    def __init__(self, *args, **kwargs):
        super(LightTroops, self).__init__("LightTroops", *args, **kwargs)


class LightningAttack(_Skill):
    def __init__(self, *args, **kwargs):
        super(LightningAttack, self).__init__("LightningAttack", *args, **kwargs)


class LightningReflexes(_Skill):
    def __init__(self, *args, **kwargs):
        super(LightningReflexes, self).__init__("LightningReflexes", *args, **kwargs)
