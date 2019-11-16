#!/usr/bin/env python
import rospy

from std_msgs.msg import Float64



def my_robot_joint_positions_publisher():

	#Initiate node for controlling joint1 and joint2 positions.
	rospy.init_node('control_robot_joint_positions_node', anonymous=True)
	#Define publishers for each joint position controller commands.
	pub1 = rospy.Publisher('/crobot/joint5_position_controller/command', Float64, queue_size=10)
	pub2 = rospy.Publisher('/crobot/joint6_position_controller/command', Float64, queue_size=10)
	pub3 = rospy.Publisher('/crobot/joint7_position_controller/command', Float64, queue_size=10)
	pub4 = rospy.Publisher('/crobot/joint8_position_controller/command', Float64, queue_size=10)
	rate = rospy.Rate(10) #10 Hz
		
	while not rospy.is_shutdown():
		#Have each joint follow a sine movement of sin(i/100).
		pos1 = 30*3.142/180
		pos2 = 40*3.142/180
		pos3 = -10*3.142/180
		pos4 = -20*3.142/180

		pub1.publish(pos1)
		pub2.publish(pos2)
		pub3.publish(pos3)
		pub4.publish(pos4)
		rate.sleep() #sle	
if __name__ == '__main__':
	my_robot_joint_positions_publisher()