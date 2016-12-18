import exception


class TerrainFeature(object):
    terrains = ['impassable', 'hill', 'forest', 'field', 'water', 'wall', 'ruins', 'building']

    def __init__(self, x, y, type):
        """

        :param x:
        :param y:
        :param type:
        """
        self._x_size = x
        self._y_size = y
        if type not in self.terrains:
            raise Exception('{type} is not a TerrainFeature')
        self._type = type

    @property
    def x_size(self):
        return self._x_size

    @property
    def y_size(self):
        return self._y_size

    @property
    def type(self):
        return self._type

    @x_size.setter
    def x_size(self, value):
        assert value > 0 and isinstance(value, int), "x_size {error} {extra}".format(
            error=exception.ERR_MESSAGE_TERRAIN_FEATURE_X_SIZE_NOT_UNSIGNED_INT,
            extra="not a {}".format(type(value)))
        self._x_size = value

    @y_size.setter
    def y_size(self, value):
        assert value > 0 and isinstance(value, int), "y_size {error} {extra}".format(
            error=exception.ERR_MESSAGE_TERRAIN_FEATURE_Y_SIZE_NOT_UNSIGNED_INT,
            extra="not a {}".format(type(value)))
        self._y_size = value

    @type.setter
    def type(self, value):
        assert isinstance(value, str), "type {error} {extra}".format(
            error=exception.ERR_MESSAGE_TERRAIN_FEATURE_TYPE_NOT_STRING,
            extra="not a {}".format(type(value)))
        self._type = value


class Map(object):
    def __init__(self, x=72, y=48):
        self._x_size = x
        self._y_size = y
        self._terrain_features = []

    def set_terrain_features(self, x, y, terrain_type):
        self._terrain_features.append(TerrainFeature(x, y, terrain_type))

    @property
    def terrain_features(self):
        return self._terrain_features


a = Map()
gorka = TerrainFeature(60, 20, 'hill')
jeziorko = TerrainFeature(100, 100, 'water')
pole = TerrainFeature(200, 200, 'field')

a.set_terrain_features(0, 0, 'hill')
a.set_terrain_features(100, 100, 'water')
a.set_terrain_features(200, 200, 'field')
a._terrain_features[1].type = -1
print a._terrain_features[1].x_size
print a._terrain_features[1].y_size
print a._terrain_features[1].type
