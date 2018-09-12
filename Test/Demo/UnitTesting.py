import unittest


class UnitTesting(unittest.TestCase):

    def test_case_1(self):
        print("This is execution of test case 1")
        result = 1
        self.assertEquals(result, 1)


if __name__ == '__main__':
    unittest.main()