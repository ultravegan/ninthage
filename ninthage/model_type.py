import exception


class _ModelType(object):
    def __init__(self):
        self.type = None

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        assert isinstance(value, str), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_TYPE_NOT_STR,
                                                                extra="not a {}".format(type(value)))
        self._type = value


class Infantry(_ModelType):
    def __init__(self, *args, **kwargs):
        super(Infantry, self).__init__(*args, *kwargs)
        self.type = "Infantry"


class WarBeast(_ModelType):
    def __init__(self, *args, **kwargs):
        super(WarBeast, self).__init__(*args, **kwargs)
        self.type = "War Beast"


class Cavalry(_ModelType):
    def __init__(self, *args, **kwargs):
        super(Cavalry, self).__init__(*args, **kwargs)
        self.type = "Cavalry"


class MonstrousInfantry(_ModelType):
    def __init__(self, *args, **kwargs):
        super(MonstrousInfantry, self).__init__(*args, **kwargs)
        self.type = "Monstrous Infantry"


class MonstrousBeast(_ModelType):
    def __init__(self, *args, **kwargs):
        super(MonstrousBeast, self).__init__(*args, **kwargs)
        self.type = "Monstrous Beast"


class MonstrousCavalry(_ModelType):
    def __init__(self, *args, **kwargs):
        super(MonstrousCavalry, self).__init__(*args, **kwargs)
        self.type = "Monstrous Cavalry"


class Chariot(_ModelType):
    def __init__(self, *args, **kwargs):
        super(Chariot, self).__init__(*args, **kwargs)
        self.type = "Chariot"


class Monster(_ModelType):
    def __init__(self, *args, **kwargs):
        super(Monster, self).__init__(*args, **kwargs)
        self.type = "Monster"


class RiddenMonster(_ModelType):
    def __init__(self, *args, **kwargs):
        super(RiddenMonster, self).__init__(*args, **kwargs)
        self.type = "Ridden Monster"


class Swarm(_ModelType):
    def __init__(self, *args, **kwargs):
        super(Swarm, self).__init__(*args, **kwargs)
        self.type = "Swarm"


class WarMachine(_ModelType):
    def __init__(self, *args, **kwargs):
        super(WarMachine, self).__init__(*args, **kwargs)
        self.type = "War Machine"
