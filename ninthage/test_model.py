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
                           {"M": 0, "WS": 0, "BS": 0, "S": 0, "T": 0, "W": 0, "I": 0, "A": 0, "Ld": 0, "Sv": 0,
                            "WSv": 0}, ["Fear"], "Monster", "Champion")

    def testModelGetName(self):
        self.testModelExist()
        self.assertEqual(self.model.name, "Chaos Warriors", "cannot get name from model")

    def testModelGetStats(self):
        self.testModelExist()
        self.assertEqual(self.model.stats,
                         {"M": 0, "WS": 0, "BS": 0, "S": 0, "T": 0, "W": 0, "I": 0, "A": 0, "Ld": 0, "Sv": 0,
                          "WSv": 0}, "cannot get stats from model")

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


if __name__ == "__main__":
    unittest.main()
