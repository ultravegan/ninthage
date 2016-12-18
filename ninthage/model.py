#!/usr/bin/env python
"""
Module with model functionalities.
"""
import exception
import variables

__author__ = "ultravegan"


class Model(object):
    def __init__(self, name, stats, skills, model_type, role=None):
        """

        :param name: str
        :param stats: dict
        :param skills: list
        :param model_type: str
        :param role: str
        """
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
                print stat
                raise exception.ModelStatNotExistException(stat)
            if not (0 <= value[stat] <= 10) or value[stat] == '-':
                raise exception.ModelStatNotInRange(stat, value[stat])
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

    @property
    def movement(self):
        return self._stats['M']

    @movement.setter
    def movement(self, value):
        assert isinstance(value, int), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_STAT_VALUE_NOT_INT,
                                                                extra="not a {}".format(type(value)))
        self._stats['M'] = value

    @property
    def weapon_skill(self):
        return self._stats['WS']

    @weapon_skill.setter
    def weapon_skill(self, value):
        assert isinstance(value, int), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_STAT_VALUE_NOT_INT,
                                                                extra="not a {}".format(type(value)))
        self._stats['WS'] = value

    @property
    def ballistic_skill(self):
        return self._stats['BS']

    @ballistic_skill.setter
    def ballistic_skill(self, value):
        assert isinstance(value, int), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_STAT_VALUE_NOT_INT,
                                                                extra="not a {}".format(type(value)))
        self._stats['BS'] = value

    @property
    def strength(self):
        return self._stats['S']

    @strength.setter
    def strength(self, value):
        assert isinstance(value, int), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_STAT_VALUE_NOT_INT,
                                                                extra="not a {}".format(type(value)))
        self._stats['S'] = value

    @property
    def toughness(self):
        return self._stats['T']

    @toughness.setter
    def toughness(self, value):
        assert isinstance(value, int), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_STAT_VALUE_NOT_INT,
                                                                extra="not a {}".format(type(value)))
        self._stats['T'] = value

    @property
    def wounds(self):
        return self._stats['W']

    @wounds.setter
    def wounds(self, value):
        assert isinstance(value, int), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_STAT_VALUE_NOT_INT,
                                                                extra="not a {}".format(type(value)))
        self._stats['W'] = value

    @property
    def initiative(self):
        return self._stats['I']

    @initiative.setter
    def initiative(self, value):
        assert isinstance(value, int), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_STAT_VALUE_NOT_INT,
                                                                extra="not a {}".format(type(value)))
        self._stats['I'] = value

    @property
    def attacks(self):
        return self._stats['A']

    @attacks.setter
    def attacks(self, value):
        assert isinstance(value, int), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_STAT_VALUE_NOT_INT,
                                                                extra="not a {}".format(type(value)))
        self._stats['A'] = value

    @property
    def leadership(self):
        return self._stats['Ld']

    @leadership.setter
    def leadership(self, value):
        assert isinstance(value, int), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_STAT_VALUE_NOT_INT,
                                                                extra="not a {}".format(type(value)))
        self._stats['Ld'] = value

    @property
    def save(self):
        return self._stats['Sv']

    @save.setter
    def save(self, value):
        assert isinstance(value, int), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_STAT_VALUE_NOT_INT,
                                                                extra="not a {}".format(type(value)))
        self._stats['Sv'] = value

    @property
    def ward_save(self):
        return self._stats['WSv']

    @ward_save.setter
    def ward_save(self, value):
        assert isinstance(value, int), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_STAT_VALUE_NOT_INT,
                                                                extra="not a {}".format(type(value)))
        self._stats['WSv'] = value

    def add_skills(self, *args):
        for skill in args:
            assert isinstance(skill, str), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_SKILL_NOT_STR,
                                                                    extra="not a {}".format(type(skill)))
            if skill not in variables.SKILLS:
                raise exception.ModelSkillNotExistException(skill)
            if skill in self.skills:
                continue
            self.skills.append(skill)

    def remove_skills(self, *args):
        for skill in args:
            assert isinstance(skill, str), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_SKILL_NOT_STR,
                                                                    extra="not a {}".format(type(skill)))
            if skill not in variables.SKILLS:
                raise exception.ModelSkillNotExistException(skill)
            if skill not in self.skills:
                raise exception.ModelSkillNotInModelSkills(skill)
            self.skills.remove(skill)

    def change_stat(self, stat, value):
        assert isinstance(stat, str), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_STAT_NOT_STR,
                                                               extra="not a {}".format(type(stat)))
        assert isinstance(value, int), "{error} {extra}".format(error=exception.ERR_MESSAGE_MODEL_STAT_VALUE_NOT_INT,
                                                                extra="not a {}".format(type(value)))
        if stat not in variables.STATS:
            raise exception.ModelStatNotExistException(stat)
        if not (0 <= value <= 10) or value == '-':
            raise exception.ModelStatNotInRange(stat, value)
        self.stats[stat] = value


a = Model("Chaos Warriors", {"M": 0, "WS": 0, "BS": 0, "T": 0, "W": 0, "I": 0, "A": 0, "Ld": 0,
                             "Sv": 0, "WSv": 0}, ["Fear"], "Monster", "Champion")
