__all__ = ["_ModelBase", "ModelBaseRectangle", "ModelBaseRound", "ModelBaseSquare"]


class _ModelBase(object):
    pass


class ModelBaseSquare(object):
    def __init__(self, *args, **kwargs):
        super(ModelBaseSquare, self).__init__(*args, **kwargs)


class ModelBaseRectangle(object):
    def __init__(self, *args, **kwargs):
        super(ModelBaseRectangle, self).__init__(*args, **kwargs)


class ModelBaseRound(object):
    def __init__(self, *args, **kwargs):
        super(ModelBaseRound, self).__init__(*args, **kwargs)
