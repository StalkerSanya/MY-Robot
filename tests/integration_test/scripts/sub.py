#!/usr/bin/env python
import rospy

from control_msgs.msg import JointControllerState



def check_joint5(msg):
	if abs(msg.set_point-msg.process_value) < 0.01:
		print('joint 5 passed test')
	else:
		print("failed")


def check_joint6(msg):
	if abs(msg.set_point-msg.process_value) < 0.01:
		print('joint 6 passed test')
	else:
		print("failed")

def check_joint7(msg):
	if abs(msg.set_point-msg.process_value) < 0.01:
		print('joint 7 passed test')
	else:
		print("failed")

def check_joint8(msg):
	if abs(msg.set_point-msg.process_value) < 0.01:
		print('joint 8 passed test')
	else:
		print("failed")

def my_robot_joint_positions_subscriber():
	counter = 0
	rospy.init_node('image_listener')

	#topics for each leg

	wheel1_topic = '/crobot/joint5_position_controller/state'
	wheel2_topic = '/crobot/joint6_position_controller/state'
	wheel3_topic = '/crobot/joint7_position_controller/state'
	wheel4_topic = '/crobot/joint8_position_controller/state'

	#2 subscribers for 2 legs

	rospy.Subscriber(wheel1_topic,JointControllerState,check_joint5)
	rospy.Subscriber(wheel2_topic,JointControllerState,check_joint6)
	rospy.Subscriber(wheel3_topic,JointControllerState,check_joint7)
	rospy.Subscriber(wheel4_topic,JointControllerState,check_joint8)


	rospy.spin()


if __name__ == '__main__':
	my_robot_joint_positions_subscriber()