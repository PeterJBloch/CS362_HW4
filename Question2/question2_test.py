import list_element_average
import unittest

class List_Averaging(unittest.TestCase):
    def test_regular_lists(self):
        """
        This unit test ensures that the code works with normal lists. This is
        a 'vanilla' execution of the list_element_average function.
        """
        self.assertEqual(list_element_average.list_average([3,5,7]),5)
        self.assertEqual(list_element_average.list_average([-10,10]),0)

    def test_bad_lists(self):
        """
        This unit test checks for bad cases and ensures that a Syntax or Type error
        is raised where appropriate. This is our 'fringe' or 'bad' input checker test.
        """
        #Testing an empty list:
        with self.assertRaises(SyntaxError):
            list_element_average.list_average([])
        
        with self.assertRaises(TypeError):
            list_element_average.list_average()

if __name__ == "__main__":
    unittest.main()