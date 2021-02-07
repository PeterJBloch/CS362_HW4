import unittest
import full_name

class Test_Names(unittest.TestCase):
    def test_correct_name(self):
        self.assertEqual(full_name.name("Peter","Bloch"),"Peter Bloch")
        self.assertEqual(full_name.name("Clark","Kent"),"Clark Kent")
        return

    def test_value_errors(self):
        #Check for blank first/last names
        with self.assertRaises(ValueError):
            full_name.name("John","")
            full_name.name("","Pig")

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            full_name.name()
            full_name.name(5,"hello")
            full_name.name("Peter",69)


if __name__ == "__main__":
    unittest.main()