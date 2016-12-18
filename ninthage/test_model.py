# -*- coding: utf-8 -*-
"""
Model class tests.
"""
import unittest

from model import Model

__author__ = "ultravegan"


class TestModel(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.model = None

    def testModelExist(self):
        self.model = Model("Chaos Warriors",
                           {"M": 0, "WS": 1, "BS": 2, "S": 3, "T": 4, "W": 5, "I": 6, "A": 7, "Ld": 8, "Sv": 9,
                            "WSv": 10}, ["Fear"], "Monster", "Champion")

    def testModelGetName(self):
        self.testModelExist()
        self.assertEqual(self.model.name, "Chaos Warriors", "cannot get name from model")

    def testModelGetStats(self):
        self.testModelExist()
        self.assertEqual(self.model.stats,
                         {"M": 0, "WS": 1, "BS": 2, "S": 3, "T": 4, "W": 5, "I": 6, "A": 7, "Ld": 8, "Sv": 9,
                          "WSv": 10}, "cannot get stats from model")

    def testModelGetSkills(self):
        self.testModelExist()
        self.assertEqual(self.model.skills, ["Fear"], "cannot get skills from model")

    def testModelGetType(self):
        self.testModelExist()
        self.assertEqual(self.model.model_type, "Monster", "cannot get type from model")

    def testModelGetRole(self):
        self.testModelExist()
        self.assertEqual(self.model.role, "Champion", "cannot get role from model")

    def testModelSetName(self):
        self.testModelExist()
        self.model.name = "Name2"
        self.assertEqual(self.model.name, "Name2", "cannot set model name")

    def testModelSetStats(self):
        self.testModelExist()
        self.model.stats = {"M": 0, "WS": 1, "BS": 0, "S": 0, "T": 0, "W": 0, "I": 0, "A": 0, "Ld": 0, "Sv": 0,
                            "WSv": 0}
        self.assertEqual(self.model.stats,
                         {"M": 0, "WS": 1, "BS": 0, "S": 0, "T": 0, "W": 0, "I": 0, "A": 0, "Ld": 0, "Sv": 0,
                          "WSv": 0}, "cannot get stats from model")

    def testModelSetSkills(self):
        self.testModelExist()
        self.model.skills = ["Ambush"]
        self.assertEqual(self.model.skills, ["Ambush"], "cannot get skills from model")

    def testModelSetType(self):
        self.testModelExist()
        self.model.model_type = "Infantry"
        self.assertEqual(self.model.model_type, "Infantry", "cannot get type from model")

    def testModelSetRole(self):
        self.testModelExist()
        self.model.role = "Musician"
        self.assertEqual(self.model.role, "Musician", "cannot get role from model")

    def testModelAddSkill(self):
        self.testModelExist()
        self.model.add_skills("Ambush")
        self.assertEqual(self.model.skills, ["Fear", "Ambush"], "cannot add skill to model")

    def testModelRemoveSkill(self):
        self.testModelExist()
        self.model.remove_skills("Fear")
        self.assertEqual(self.model.skills, [], "cannot remove models skill")

    def testModelChangeStat(self):
        self.testModelExist()
        self.model.change_stat("M", 3)

    def testModelGetMovement(self):
        self.testModelExist()
        self.assertEqual(self.model.movement, 0, "cannot get movement from model")

    def testModelGetWeaponSkill(self):
        self.testModelExist()
        self.assertEqual(self.model.weapon_skill, 1, "cannot get weapon skill from model")

    def testModelBallisticSkill(self):
        self.testModelExist()
        self.assertEqual(self.model.ballistic_skill, 2, "cannot get ballistic skill from model")

    def testModelGetStrength(self):
        self.testModelExist()
        self.assertEqual(self.model.strength, 3, "cannot get strength from model")

    def testModelGetToughness(self):
        self.testModelExist()
        self.assertEqual(self.model.toughness, 4, "cannot get toughness from model")

    def testModelGetWounds(self):
        self.testModelExist()
        self.assertEqual(self.model.wounds, 5, "cannot get wounds from model")

    def testModelGetInitiative(self):
        self.testModelExist()
        self.assertEqual(self.model.initiative, 6, "cannot get initiative from model")

    def testModelGetAttacks(self):
        self.testModelExist()
        self.assertEqual(self.model.attacks, 7, "cannot get attacks from model")

    def testModelGetLeadership(self):
        self.testModelExist()
        self.assertEqual(self.model.leadership, 8, "cannot get leadership from model")

    def testModelGetSave(self):
        self.testModelExist()
        self.assertEqual(self.model.save, 9, "cannot get save from model")

    def testModelGetWardSave(self):
        self.testModelExist()
        self.assertEqual(self.model.ward_save, 10, "cannot get ward save from model")

    def testModelSetMovement(self):
        self.testModelExist()
        self.model.movement = 10
        self.assertEqual(self.model.movement, 10, "cannot set models movement")

    def testModelSetWeaponSkill(self):
        self.testModelExist()
        self.model.weapon_skill = 9
        self.assertEqual(self.model.weapon_skill, 9, "cannot set models movement")

    def testModelSetBallisticSkill(self):
        self.testModelExist()
        self.model.ballistic_skill = 8
        self.assertEqual(self.model.ballistic_skill, 8, "cannot set models ballistic skill")

    def testModelSetStrength(self):
        self.testModelExist()
        self.model.strength = 7
        self.assertEqual(self.model.strength, 7, "cannot set models strength")

    def testModelSetToughness(self):
        self.testModelExist()
        self.model.toughness = 6
        self.assertEqual(self.model.toughness, 6, "cannot set models toughness")

    def testModelSetWounds(self):
        self.testModelExist()
        self.model.wounds = 5
        self.assertEqual(self.model.wounds, 5, "cannot set models wounds")

    def testModelSetInitiative(self):
        self.testModelExist()
        self.model.initiative = 4
        self.assertEqual(self.model.initiative, 4, "cannot set models initiative")

    def testModelSetAttacks(self):
        self.testModelExist()
        self.model.attacks = 3
        self.assertEqual(self.model.attacks, 3, "cannot set models attacks")

    def testModelSetLeadership(self):
        self.testModelExist()
        self.model.leadership = 2
        self.assertEqual(self.model.leadership, 2, "cannot set models leadership")

    def testModelSetSave(self):
        self.testModelExist()
        self.model.save = 1
        self.assertEqual(self.model.save, 1, "cannot set models save")

    def testModelSetWardSave(self):
        self.testModelExist()
        self.model.ward_save = 0
        self.assertEqual(self.model.ward_save, 0, "cannot set models attacks")


if __name__ == "__main__":
    unittest.main()
