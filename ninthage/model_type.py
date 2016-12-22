import exception

__all__ = ["_ModelType", "Infantry", "WarBeast", "Cavalry", "Monster", "MonstrousBeast", "MonstrousCavalry",
           "MonstrousInfantry", "RiddenMonster", "Chariot", "WarMachine", "Swarm"]


class _ModelType(object):
    def __init__(self, *args, **kwargs):
        self.name = ''

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        assert isinstance(value, str), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_TYPE_NOT_STR,
                                                                extra="not a {}".format(type(value)))
        self._name = value


class Infantry(_ModelType):
    def __init__(self, *args, **kwargs):
        super(Infantry, self).__init__(*args, **kwargs)
        self.name = "Infantry"


class WarBeast(_ModelType):
    def __init__(self, *args, **kwargs):
        super(WarBeast, self).__init__(*args, **kwargs)
        self.name = "War Beast"


class Cavalry(_ModelType):
    def __init__(self, *args, **kwargs):
        super(Cavalry, self).__init__(*args, **kwargs)
        self.name = "Cavalry"


class MonstrousInfantry(_ModelType):
    def __init__(self, *args, **kwargs):
        super(MonstrousInfantry, self).__init__(*args, **kwargs)
        self.name = "Monstrous Infantry"


class MonstrousBeast(_ModelType):
    def __init__(self, *args, **kwargs):
        super(MonstrousBeast, self).__init__(*args, **kwargs)
        self.name = "Monstrous Beast"


class MonstrousCavalry(_ModelType):
    def __init__(self, *args, **kwargs):
        super(MonstrousCavalry, self).__init__(*args, **kwargs)
        self.name = "Monstrous Cavalry"


class Chariot(_ModelType):
    def __init__(self, *args, **kwargs):
        super(Chariot, self).__init__(*args, **kwargs)
        self.name = "Chariot"


class Monster(_ModelType):
    def __init__(self, *args, **kwargs):
        super(Monster, self).__init__(*args, **kwargs)
        self.name = "Monster"


class RiddenMonster(_ModelType):
    def __init__(self, *args, **kwargs):
        super(RiddenMonster, self).__init__(*args, **kwargs)
        self.name = "Ridden Monster"


class Swarm(_ModelType):
    def __init__(self, *args, **kwargs):
        super(Swarm, self).__init__(*args, **kwargs)
        self.name = "Swarm"


class WarMachine(_ModelType):
    def __init__(self, *args, **kwargs):
        super(WarMachine, self).__init__(*args, **kwargs)
        self.name = "War Machine"
