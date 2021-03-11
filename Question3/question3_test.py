import unittest
import full_name

class Test_Names(unittest.TestCase):
    def test_correct_name(self):
        """
        This tests correct or 'vanilla' executions of the full_name.name function.
        This ensures the test works as desired with good inputs.
        """
        self.assertEqual(full_name.name("Peter","Bloch"),"Peter Bloch")
        self.assertEqual(full_name.name("Clark","Kent"),"Clark Kent")
        return

    def test_value_errors(self):
        """
        This test checks to ensure that code is not executed when a bad input is inserted.
        We do not wish to see single name responses anywhere because otherwise there is no use for the program,
        and the user should be notified there is something wrong.
        """
        #Check for blank first/last names
        with self.assertRaises(ValueError):
            full_name.name("John","")
            full_name.name("","Pig")

    def test_type_errors(self):
        """
        This test ensures that all arguments that are passed are of the correct type.
        We check for number of inputs and type, so that numbers are not added to strings, 
        which may cause a runtime error later on...
        """
        #Check for the type errors raised from incorrect usage of the function
        with self.assertRaises(TypeError):
            full_name.name()
            full_name.name(5,"hello")
            full_name.name("Peter",69)


if __name__ == "__main__":
    unittest.main()