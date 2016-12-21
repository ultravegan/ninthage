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
        super(Accurate, self).__init__("Accurate", *args, **kwargs)


class Ambush(_Skill):
    def __init__(self, *args, **kwargs):
        super(Ambush, self).__init__("Ambush", *args, **kwargs)


class Fear(_Skill):
    def __init__(self, *args, **kwargs):
        super(Fear, self).__init__("Fear", *args, **kwargs)
