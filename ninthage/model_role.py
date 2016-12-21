import exception

__all__ = ["_ModelRole", "Champion", "Musician", "StandardBearer"]


class _ModelRole(object):
    def __init__(self):
        self.name = ''

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        assert isinstance(value, str), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_ROLE_NOT_STR,
                                                                extra="not a {}".format(type(value)))
        self._name = value


class Champion(_ModelRole):
    def __init__(self, *args, **kwargs):
        super(Champion, self).__init__(*args, **kwargs)
        self.name = "Champion"


class Musician(_ModelRole):
    def __init__(self, *args, **kwargs):
        super(Musician, self).__init__(*args, **kwargs)
        self.name = "Musician"


class StandardBearer(_ModelRole):
    def __init__(self, *args, **kwargs):
        super(StandardBearer, self).__init__(*args, **kwargs)
        self.name = "Standard Bearer"
