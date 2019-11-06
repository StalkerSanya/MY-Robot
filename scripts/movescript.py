#!/usr/bin/env python
import rospy
import math

from std_msgs.msg import Float64
from math import sin,cos,atan2,sqrt,fabs


#Define a RRBot joint positions publisher for joint controllers.
def my_robot_joint_positions_publisher():

	#Initiate node for controlling joint1 and joint2 positions.
	rospy.init_node('control_robot_joint_positions_node', anonymous=True)

	#Define publishers for each joint position controller commands.
	pub1 = rospy.Publisher('/crobot/joint1_position_controller/command', Float64, queue_size=10)
	pub2 = rospy.Publisher('/crobot/joint2_position_controller/command', Float64, queue_size=10)
	pub3 = rospy.Publisher('/crobot/joint3_position_controller/command', Float64, queue_size=10)
	pub4 = rospy.Publisher('/crobot/joint4_position_controller/command', Float64, queue_size=10)
	pub5 = rospy.Publisher('/crobot/joint5_position_controller/command', Float64, queue_size=10)
	pub6 = rospy.Publisher('/crobot/joint6_position_controller/command', Float64, queue_size=10)
	pub7 = rospy.Publisher('/crobot/joint7_position_controller/command', Float64, queue_size=10)
	pub8 = rospy.Publisher('/crobot/joint8_position_controller/command', Float64, queue_size=10)
	

	rate = rospy.Rate(100) #10 Hz

	#While loop to have joints follow a certain position, while rospy is not shutdown.
	i = 0
	while not rospy.is_shutdown():

		#Have each joint follow a sine movement of sin(i/100).	
		sine_movement = sin(i/100.)

		pub1.publish(sine_movement)
		pub2.publish(sine_movement)
		pub3.publish(sine_movement)
		pub4.publish(sine_movement)

		#Have each joint follow a sine movement of cos(i/10)/2.
		sine_movement = cos(i/10.)/2

		#Publish the same sine movement to each joint.
		pub5.publish(sine_movement)
		pub6.publish(sine_movement)
		pub7.publish(sine_movement)
		pub8.publish(sine_movement)
		

		i = i+1 #increment i

		rate.sleep() #sleep for rest of rospy.Rate(10)


#Main section of code that will continuously run unless rospy receives interuption (ie CTRL+C)
if __name__ == '__main__':
	try: my_robot_joint_positions_publisher()
	except rospy.ROSInterruptException: pass