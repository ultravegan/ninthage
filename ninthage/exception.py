__all__ = ["ERR_MESSAGE_MODEL_NAME_NOT_STR", "ERR_MESSAGE_MODEL_ROLE_NOT_STR", "ERR_MESSAGE_MODEL_SKILLS_NOT_LIST",
           "ERR_MESSAGE_MODEL_STATS_NOT_DICT", "ERR_MESSAGE_MODEL_TYPE_NOT_STR", "ModelRoleNotExistException",
           "ModelSkillNotExistException", "ModelStatNotExistException", "ModelTypeNotExistException",
           "ModelStatNotInRange", "ModelSkillNotInModelSkills", "ERR_MESSAGE_MODEL_STAT_NOT_STR",
           "ERR_MESSAGE_MODEL_STAT_VALUE_NOT_INT", "ERR_MESSAGE_MODEL_SKILL_NOT_SKILL", "ModelSkillAlreadyInSkills",
           "ModelSkillNotInSkills", "ERR_MESSAGE_MODEL_EQUIPMENT_NOT_EQUIPMENT", "ModelEquipmentAlreadyExistException",
           "ERR_MESSAGE_MODEL_EQUIPMENT_NOT_STR", "ERR_MESSAGE_MODEL_SKILL_NOT_STR",
           "ERR_MESSAGE_MODEL_TYPE_NOT_MODEL_TYPE", "ERR_MESSAGE_MODEL_ROLE_NOT_MODEL_ROLE",
           "ERR_MESSAGE_MODEL_BASE_NOT_MODEL_BASE", "ERR_MESSAGE_MODEL_BASE_TYPE_NOT_BASE",
           "ERR_MESSAGE_MODEL_BASE_LENGTH_NOT_UNSIGNED_INT", "ERR_MESSAGE_MODEL_BASE_WIDTH_NOT_UNSIGNED_INT",
           "ERR_MESSAGE_MODEL_BASE_RADIUS_NOT_UNSIGNED_INT", "ERR_MESSAGE_UNIT_NAME_NOT_STR"]

# model.py errors
ERR_MESSAGE_MODEL_NAME_NOT_STR = "Model name has to be string"
ERR_MESSAGE_MODEL_STATS_NOT_DICT = "Model stats has to be dictionary"
ERR_MESSAGE_MODEL_SKILLS_NOT_LIST = "Model skills has to be list"
ERR_MESSAGE_MODEL_TYPE_NOT_STR = "Model type has to be string"
ERR_MESSAGE_MODEL_ROLE_NOT_STR = "Model role has to be string"
ERR_MESSAGE_MODEL_STAT_NOT_STR = "Skill has to be string"
ERR_MESSAGE_MODEL_STAT_VALUE_NOT_INT = "Skill value has to be int"
ERR_MESSAGE_MODEL_EQUIPMENT_NOT_LIST = 'Model equipments have to be list'
ERR_MESSAGE_MODEL_EQUIPMENT_NOT_EQUIPMENT = 'Model equipments has to be _Equipment object'
ERR_MESSAGE_MODEL_SKILL_NOT_SKILL = 'Model skill has to be _Skill object'
ERR_MESSAGE_MODEL_EQUIPMENT_NOT_STR = 'Mode equipment has to be string'
ERR_MESSAGE_MODEL_SKILL_NOT_STR = 'Model skill has to be string'
ERR_MESSAGE_MODEL_TYPE_NOT_MODEL_TYPE = 'Model type has to be _ModelType object'
ERR_MESSAGE_MODEL_ROLE_NOT_MODEL_ROLE = 'Model role has to be _ModelRole object'
ERR_MESSAGE_MODEL_BASE_NOT_MODEL_BASE = 'Model base has to be _ModeBase object'
ERR_MESSAGE_MODEL_BASE_TYPE_NOT_BASE = 'Model base name has to be string'
ERR_MESSAGE_MODEL_BASE_LENGTH_NOT_UNSIGNED_INT = 'Model base length has to be unsigned int'
ERR_MESSAGE_MODEL_BASE_WIDTH_NOT_UNSIGNED_INT = 'Model base width has to be int unsigned int'
ERR_MESSAGE_MODEL_BASE_RADIUS_NOT_UNSIGNED_INT = 'Model base radius has to be unsigned int'
ERR_MESSAGE_UNIT_NAME_NOT_STR = 'Unit name has to be string'


class ModelStatNotExistException(Exception):
    def __init__(self, stat):
        self.stat = stat

    def __str__(self):
        return 'Stat {stat} does not exists'.format(stat=self.stat)


class ModelEquipmentNotExistException(Exception):
    def __init__(self, equip):
        self.equip = equip

    def __str__(self):
        return 'Equipment {equip} does not exists'.format(equip=self.equip)


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
        return 'Stat {stat} value: {value} is not in range [0,10]'.format(stat=self.stat, value=self.value)


class ModelSkillNotInModelSkills(Exception):
    def __init__(self, skill):
        self.skill = skill

    def __str__(self):
        return 'Model does not have {skill} skill'.format(skill=self.skill)


class ModelEquipmentNotInModelEquipment(Exception):
    def __init__(self, equip):
        self.equip = equip

    def __str__(self):
        return 'Model does not have {equip} equip'.format(equip=self.equip)


class ModelSkillAlreadyInSkills(Exception):
    def __init__(self, skill):
        self.skill = skill

    def __str__(self):
        return 'Model has {skill} already'.format(skill=self.skill)


class ModelSkillNotInSkills(Exception):
    def __init__(self, skill):
        self.skill = skill

    def __str__(self):
        return 'Model doesnt have {skill}, cannot remove it'.format(skill=self.skill)


class ModelEquipmentAlreadyExistException(Exception):
    def __init__(self, equip):
        self.equip = equip

    def __str__(self):
        return 'Model already has {equip} equipment'.format(equip=self.equip)
