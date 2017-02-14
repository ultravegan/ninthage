import exception
from model import *


class _Unit(object):
    def __init__(self, name, models, *args, **kwargs):
        self.name = name
        self.models = models

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        assert isinstance(value, str), "{error} {extra}".format(error=exception.ERR_MESSAGE_UNIT_NAME_NOT_STR,
                                                                extra="not a {}".format(type(value)))
        self._name = value

    @property
    def models(self):
        return self._models

    @models.setter
    def models(self, value):
        assert isinstance(value, list), "{error} {extra}".format(error=exception.ERR_MESSAGE_UNIT_MODELS_NOT_LIST,
                                                                 extra="not a {}".format(type(value)))
        for model in value:
            assert isinstance(model, Model), "{error} {extra}".format(error=exception.ERR_MESSAGE_UNIT_MODEL_NOT_MODEL,
                                                                      extra="not a {}".format(type(model)))
        self._models = value

        # def remove_model(self):


class Characters(_Unit):
    def __init__(self, *args, **kwargs):
        super(Characters, self).__init__(*args, **kwargs)


class Core(_Unit):
    def __init__(self, *args, **kwargs):
        super(Core, self).__init__(*args, **kwargs)


class Special(_Unit):
    def __init__(self, *args, **kwargs):
        super(Special, self).__init__(*args, **kwargs)


skills = [Fear(), Ambush()]
equipment = [Shield(), Halberd()]
model_role = Champion()
model_type = Monster()
model_base = ModelBaseSquare(3)
a = Model("Chaos Warriors", {"M": 0, "WS": 0, "BS": 0, "T": 0, "W": 0, "I": 0, "A": 0, "Ld": 0,
                             "Sv": 0, "WSv": 0}, skills, model_type, equipment, model_base, 10, role=model_role)

b = Core('dupa', [a])
