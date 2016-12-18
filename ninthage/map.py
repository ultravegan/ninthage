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
    def x(self):
        return self._x_size

    @property
    def y(self):
        return self._y_size

    @property
    def type(self):
        return self._type

    @x.setter
    def x(self, value):
        name.setter

        def name(self, value):
            assert isinstance(value, int), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_NAME_NOT_STR,
                                                                    extra="not a {}".format(type(value)))
            self._name = value
        self._name = value


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
print a._terrain_features[1].x
print a._terrain_features[1].y
print a._terrain_features[1].type