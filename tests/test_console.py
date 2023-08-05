#!/usr/bin/python3
"""test for console"""
import unittest
from io import StringIO
import pep8
import sys
import os
import json
import console
import tests
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """this will test the console"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.consol = HBNBCommand()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.consol

    def tearDown(self):
        """Remove temporary file (file.json) created as a result"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_console(self):
        """Pep8 console.py"""

        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_emptyline(self):
        """Test emptyline method"""
        cmd = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as fake_output:
            cmd.emptyline()
            output = fake_output.getvalue().strip()
            self.assertEqual(output, "")

    def test_do_quit(self):
        """Test do_quit method"""
        cmd = HBNBCommand()
        with self.assertRaises(SystemExit) as cm:
            cmd.do_quit("quit")
            self.assertEqual(cm.exception.code, None)

    def test_do_create(self):
        """Test do_create method"""
        cmd = HBNBCommand()
        cmd = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as fake_output:
            cmd.do_create("")
            output = fake_output.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

            cmd.do_create("FakeModel")
            output = fake_output.getvalue().strip()
            self.assertTrue("** class doesn't exist **" in output)

    def test_show(self):
        """Test show command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show")
            self.assertEqual(
                    "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show asdfsdrfs")
            self.assertEqual(
                    "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show BaseModel")
            self.assertEqual(
                    "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show BaseModel abcd-123")
            self.assertEqual(
                    "** no instance found **\n", f.getvalue())

    def test_do_destroy(self):
        """Test do_destroy method"""
        cmd = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as fake_output:
            cmd.do_destroy("")
            output = fake_output.getvalue().strip()                                    
            self.assertEqual(output, "** class name missing **")
            cmd.do_destroy("FakeModel")
            output = fake_output.getvalue().strip()
            self.assertTrue("** class doesn't exist **" in output)

    def test_help_destroy(self):
        """Test help_destroy method"""
        cmd = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as fake_output:
            cmd.help_destroy()
            output = fake_output.getvalue().strip()
            self.assertEqual(output, "Destroys an individual instance of a "
                             "class\n[Usage]: destroy <className> <objectId>")

    def test_do_update(self):
        """Test do_update method"""
        cmd = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as fake_output:
            cmd.do_update("")
            output = fake_output.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

            cmd.do_update("FakeModel")
            output = fake_output.getvalue().strip()
            self.assertTrue("** class doesn't exist **" in output)


if __name__ == "__main__":
    unittest.main()
