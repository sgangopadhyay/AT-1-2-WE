import unittest  # test runner
import suman  # importing the suman.py


class Test_SumanFile(unittest.TestCase):

    def test_guvi(self):
        self.assertEqual(suman.guvi(10, 20), 30)

    def test_cube(self):
        self.assertEqual(suman.cube(3), 27)

    def test_cube_greater(self):
        self.assertGreater(suman.cube(4), 540)

    def test_upper(self):
        self.assertEqual(suman.Suman().name_upper('suman'), 'SUMAN')


if __name__ == '__main__':
    unittest.main()
