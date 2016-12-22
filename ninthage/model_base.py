__all__ = ["_ModelBase", "ModelBaseRectangle", "ModelBaseRound", "ModelBaseSquare"]
import exception


class _ModelBase(object):
    def __init__(self, *args, **kwargs):
        self.base_type = ''

    @property
    def base_type(self):
        return self._base_type

    @base_type.setter
    def base_type(self, value):
        assert isinstance(value, str), "{error} {extra}".format(
            error=exception.ERR_MESSAGE_MODEL_BASE_TYPE_NOT_BASE,
            extra="not a {}".format(type(value)))
        self._base_type = value


class ModelBaseRectangle(_ModelBase):
    def __init__(self, length, width, *args, **kwargs):
        super(ModelBaseRectangle, self).__init__(*args, **kwargs)
        self.base_type = 'Rectangle'
        self.length = length
        self.width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        assert isinstance(value, int), "{error} {extra}".format(
            error=exception.ERR_MESSAGE_MODEL_BASE_LENGTH_NOT_UNSIGNED_INT,
            extra="not a {}".format(type(value)))
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        assert isinstance(value, int), "{error} {extra}".format(
            error=exception.ERR_MESSAGE_MODEL_BASE_WIDTH_NOT_UNSIGNED_INT,
            extra="not a {}".format(type(value)))
        self._width = value


class ModelBaseSquare(ModelBaseRectangle):
    def __init__(self, side_size, *args, **kwargs):
        super(ModelBaseSquare, self).__init__(side_size, side_size, *args, **kwargs)
        self.base_type = 'Square'


class ModelBaseRound(_ModelBase):
    def __init__(self, radius, *args, **kwargs):
        super(ModelBaseRound, self).__init__(*args, **kwargs)
        self.base_type = 'Round'
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        assert isinstance(value, int), "{error} {extra}".format(
            error=exception.ERR_MESSAGE_MODEL_BASE_RADIUS_NOT_UNSIGNED_INT,
            extra="not a {}".format(type(value)))
        self._radius = value
