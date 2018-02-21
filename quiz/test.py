# Self-check for lists/files quiz
import unittest, os
from lists_files import *

class CheckListFileQuiz(unittest.TestCase):

    def test_schedule(self):
        self.assertEqual(last_period, "Physical Education")
        self.assertEqual(pre_lunch, ["Algebra", "Physics", "Study Hall", "English", "Arabic"])
        self.assertEqual(a_courses, ["Algebra", "Arabic"])

    def test_file(self):
        assert os.path.exists('my_schedule.txt')


if __name__ == '__main__':
    unittest.main()
