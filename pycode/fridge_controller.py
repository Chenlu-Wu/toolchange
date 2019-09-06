#! /usr/bin/env python
import rospy
from std_msgs.msg import Bool


class fridge_control:
	def __init__(self):
		rospy.init_node('fridge_controller')
		rospy.Subscriber('/fridge', Bool, self.fridge_callback)
		rospy.spin()



	def fridge_callback(self, data):	
		if (data.data == True):
			self.open_fridge()

		else:
			self.close_fridge()


	def open_fridge(self):
		#Please write fridge open code here
		pass


	def close_fridge(self):
		#Please write fridge close code here
		pass


if __name__=='__main__':
    try:
        fridge = fridge_control()

    except rospy.ROSInterruptException: pass