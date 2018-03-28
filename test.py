import unittest
from task import Plane

# https://github.com/karmazynow-a/kol1_gr2/blob/master/task.py

 
class TestPlaneMethoda(unittest.TestCase):

	def test_Angle(self): 
		new_plane = Plane()
		new_plane.NewAngle()
		self.assertIn(new_plane.Angle(), range(0, 360))
		