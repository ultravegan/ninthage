__all__ = ["ERR_MESSAGE_MODEL_NAME_NOT_STR", "ERR_MESSAGE_MODEL_ROLE_NOT_STR", "ERR_MESSAGE_MODEL_SKILLS_NOT_LIST",
           "ERR_MESSAGE_MODEL_STATS_NOT_DICT", "ERR_MESSAGE_MODEL_TYPE_NOT_STR", "ModelRoleNotExistException",
           "ModelSkillNotExistException", "ModelStatNotExistException", "ModelTypeNotExistException",
           "ModelStatNotInRange", "ModelSkillNotInModelSkills", "ERR_MESSAGE_MODEL_SKILL_NOT_STR",
           "ERR_MESSAGE_MODEL_STAT_NOT_STR", "ERR_MESSAGE_TERRAIN_FEATURE_X_SIZE_NOT_UNSIGNED_INT",
           "ERR_MESSAGE_TERRAIN_FEATURE_Y_SIZE_NOT_UNSIGNED_INT",
           "ERR_MESSAGE_TERRAIN_FEATURE_TYPE_NOT_STRING"]  # model.py errors
ERR_MESSAGE_MODEL_NAME_NOT_STR = "Model name has to be string"
ERR_MESSAGE_MODEL_STATS_NOT_DICT = "Model stats has to be dictionary"
ERR_MESSAGE_MODEL_SKILLS_NOT_LIST = "Model skills has to be list"
ERR_MESSAGE_MODEL_TYPE_NOT_STR = "Model type has to be string"
ERR_MESSAGE_MODEL_ROLE_NOT_STR = "Model role has to be string"
ERR_MESSAGE_MODEL_SKILL_NOT_STR = "Model skill has to be string"
ERR_MESSAGE_MODEL_STAT_NOT_STR = "Skill has to be string"
ERR_MESSAGE_MODEL_STAT_VALUE_NOT_INT = "Skill value has to be int"
ERR_MESSAGE_TERRAIN_FEATURE_X_SIZE_NOT_UNSIGNED_INT = "has to be unsigned int"
ERR_MESSAGE_TERRAIN_FEATURE_Y_SIZE_NOT_UNSIGNED_INT = "has to be unsigned int"
ERR_MESSAGE_TERRAIN_FEATURE_TYPE_NOT_STRING = "has to be string"


class ModelStatNotExistException(Exception):
    def __init__(self, stat):
        self.stat = stat

    def __str__(self):
        return 'Stat {stat} does not exists'.format(stat=self.stat)


class ModelSkillNotExistException(Exception):
    def __init__(self, skill):
        self.skill = skill

    def __str__(self):
        return 'Skill {skill} does not exists'.format(skill=self.skill)


class ModelTypeNotExistException(Exception):
    def __init__(self, model_type):
        self.type = model_type

    def __str__(self):
        return 'Type {type} does not exists'.format(type=self.type)


class ModelRoleNotExistsException(Exception):
    def __init__(self, role):
        self.role = role

    def __str__(self):
        return 'Role {role} does not exists'.format(role=self.role)


class ModelStatNotInRange(Exception):
    def __init__(self, stat, value):
        self.stat = stat
        self.value = value

    def __str__(self):
        return 'Stat {stat} value: {value{ is not in range [0,10]'.format(stat=self.stat, value=value)


class ModelSkillNotInModelSkills(Exception):
    def __init__(self, skill):
        self.skill = skill

    def __str__(self):
        return 'Model does not have {skill} skill'.format(skill=self.skill)
