# -*- coding: utf-8 -*-
"""
Model class tests.
"""
import unittest
from model import Model

__author__ = "ultravegan"


class TestModel(unittest.TestCase):
    def testModelExist(self):
        model = Model("Name", {"dict": 1}, ["skill"], "type", "role")

    def testGetModelName(self):
        model = Model("Name", {"dict": 1}, ["skill"], "type", "role")
        self.assertEqual(model.name, "Name", "cannot get name from model")

    def testGetModelStats(self):
        model = Model("Name", {"dict": 1}, ["skill"], "type", "role")
        self.assertEqual(model.stats, {"dict": 1}, "cannot get stats from model")

    def testGetModelSkills(self):
        model = Model("Name", {"dict": 1}, ["skill"], "type", "role")
        self.assertEqual(model.skills, ["skill"], "cannot get skills from model")

    def testGetModelType(self):
        model = Model("Name", {"dict": 1}, ["skill"], "type", "role")
        self.assertEqual(model.model_type, "type", "cannot get type from model")

    def testGetModelRole(self):
        model = Model("Name", {"dict": 1}, ["skill"], "type", "role")
        self.assertEqual(model.role, "role", "cannot get role from model")

    def testSetModelName(self):
        model = Model("Name", {"dict": 1}, ["skill"], "type", "role")
        model.name = "Name2"
        self.assertEqual(model.name, "Name2", "cannot set model name")

    def testSetModelStats(self):
        model = Model("Name", {"dict": 1}, ["skill"], "type", "role")
        model.stats = {"dict": 2}
        self.assertEqual(model.stats, {"dict": 2}, "cannot get stats from model")

    def testSetModelSkills(self):
        model = Model("Name", {"dict": 1}, ["skill"], "type", "role")
        model.skills = ["skill2"]
        self.assertEqual(model.skills, ["skill2"], "cannot get skills from model")

    def testSetModelType(self):
        model = Model("Name", {"dict": 1}, ["skill"], "type", "role")
        model.model_type = "type2"
        self.assertEqual(model.model_type, "type2", "cannot get type from model")

    def testSetModelRole(self):
        model = Model("Name", {"dict": 1}, ["skill"], "type", "role")
        model.role = "role2"
        self.assertEqual(model.role, "role2", "cannot get role from model")


if __name__ == "__main__":
    unittest.main()
