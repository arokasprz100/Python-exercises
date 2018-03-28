import numpy as np

class Plane (object):
	def __init__ (self):
		self.angle = 0
	
	def NewAngle (self):
		self.angle = np.random.normal(0.0, 90.0)

	def Angle (self):
		return self.angle
	
	def TurbulationFix (self):
		self.angle = np.absolute(self.angle) - 60.0
		print ('Turbulation fixed, new angle is {}'.format(self.angle))


if __name__ == "__main__":
	plane = Plane()


	print('Plane takes off!')

	while True:
		plane.NewAngle()
		angle = plane.Angle()
		print ('Current status is {} degrees'.format(angle))
		if  np.absolute(angle) > 30.0:
			print ('It s turbulation!')
			plane.TurbulationFix()
		exit = input ('When you want to land press "Q"')
		if exit == 'Q':
			break