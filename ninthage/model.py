#!/usr/bin/env python
"""
Module with model functionalities.
"""
import exception
import variables

__author__ = "ultravegan"


class Model(object):
    def __init__(self, name, stats, skills, model_type, role=None):
        self.name = name
        self.stats = stats
        self.skills = skills
        self.model_type = model_type
        self.role = role

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        assert isinstance(value, str), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_NAME_NOT_STR,
                                                                extra="not a {}".format(type(value)))
        self._name = value

    @property
    def stats(self):
        return self._stats

    @stats.setter
    def stats(self, value):
        assert isinstance(value, dict), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_STATS_NOT_DICT,
                                                                 extra="not a {}".format(type(value)))
        for stat in value:
            if stat not in variables.STATS:
                raise exception.ModelStatNotExistException(stat)
            if not 0 <= value[stat] <= 10:
                raise exception.ModelStatNotInRange(stat, stat.value)
        self._stats = value

    @property
    def skills(self):
        return self._skills

    @skills.setter
    def skills(self, value):
        assert isinstance(value, list), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_SKILLS_NOT_LIST,
                                                                 extra="not a {}".format(type(value)))
        for skill in value:
            if skill not in variables.SKILLS:
                raise exception.ModelSkillNotExistException(value)
        self._skills = value

    @property
    def model_type(self):
        return self._model_type

    @model_type.setter
    def model_type(self, value):
        assert isinstance(value, str), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_TYPE_NOT_STR,
                                                                extra="not a {}".format(type(value)))
        if value not in variables.MODEL_TYPE:
            raise exception.ModelTypeNotExistException(value)
        self._model_type = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        assert isinstance(value, str), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_ROLE_NOT_STR,
                                                                extra="not a {}".format(type(value)))
        if value not in variables.MODEL_ROLE:
            raise exception.ModelRoleNotExistException(value)
        self._role = value


a = Model("Chaos Warriors", {"Mv": 0, "WS": 0, "BS": 0, "St": 0, "To": 0, "Wo": 0, "In": 0, "At": 0, "Ld": 0,
                             "Sv": 0, "WSv": 0}, ["Fear"], "Monster", "Champion")
