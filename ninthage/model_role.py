import exception


class _ModelRole(object):
    def __init__(self):
        self.role = None

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        assert isinstance(value, str), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_ROLE_NOT_STR,
                                                                extra="not a {}".format(type(value)))
        self._role = value


class Champion(object):
    def __init__(self, *args, **kwargs):
        super(Champion, self).__init__(*args, **kwargs)
        self.role = "Champion"


class Musician(object):
    def __init__(self, *args, **kwargs):
        super(Musician, self).__init__(*args, **kwargs)
        self.role = "Musician"


class StandardBearer(object):
    def __init__(self, *args, **kwargs):
        super(StandardBearer, self).__init__(*args, **kwargs)
        self.role = "Standard Bearer"
