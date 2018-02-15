# Unittest for task_02 - reading and summing numbers from a file.
import task_02
import unittest
import os

class CheckTask(unittest.TestCase):

    def test_correct_totals(self):
        """ Test total() on randomly generated sample files """
        root, dirs, files = next(os.walk("test_cases"))
        totals = [task_02.total(os.path.join(root, file)) for file in files]
        self.assertEqual(totals, [224273, 5462, 509244])


if __name__ == '__main__':
    unittest.main()
