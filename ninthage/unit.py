import exception


class _Unit(object):
    def __init__(self, name, models, *args, **kwargs):
        self.name = name
        self.models = models

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        assert isinstance(value, str), "{error} {extra}".format(error=exception.ERR_MESSAGE_UNIT_NAME_NOT_STR,
                                                                extra="not a {}".format(type(value)))
        self.name = value


class Characters(_Unit):
    def __init__(self, *args, **kwargs):
        super(Characters, self).__init__(*args, **kwargs)


class Core(_Unit):
    def __init__(self, *args, **kwargs):
        super(Core, self).__init__(*args, **kwargs)


class Special(_Unit):
    def __init__(self, *args, **kwargs):
        super(Special, self).__init__(*args, **kwargs)
