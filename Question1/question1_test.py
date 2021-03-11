import cube_volume
import unittest
import math

class Cube_Volume_Testing(unittest.TestCase):
    def test_regular(self):
        """
        This test checks whether the code functions correctly and produces the correct volume
        given a series of dimensions. Nothing fancy here.
        """
        self.assertEqual(cube_volume.cube_volume(3,4,5),60)
        self.assertEqual(cube_volume.cube_volume(1,1,1),1)

    def test_negatives(self):
        """
        This test checks an edge case of negative numbers to ensure that negative
        numbers are output properly by multiplication, and doesn't always output a "real" value
        """
        self.assertEqual(cube_volume.cube_volume(10,10,-10),-1000)
        self.assertLess(cube_volume.cube_volume(100,100,-1),0)

    def test_odd(self):
        """
        This test ensures that weird numbers from other libraries work in multiplication.
        It also checks the failed case of imaginary numbers or words so that there aren't bad inputs available.
        """
        #Testing weird pi-case numbers computed from other libraries
        self.assertEqual(cube_volume.cube_volume(1,1,math.pi),math.pi)

        #Testing failed cases:
        #The imaginary numbers
        with self.assertRaises(ValueError):
            cube_volume.cube_volume(math.sqrt(-1),math.sqrt(-1),-1)
        
        #Non-number values
        with self.assertRaises(TypeError):
            cube_volume.cube_volume("five",1,2)


if __name__ == "__main__":
    unittest.main()