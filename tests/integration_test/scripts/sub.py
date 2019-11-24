#!/usr/bin/env python
import rospy

from control_msgs.msg import JointControllerState



def check_joint5(msg):
	assert abs(msg.set_point-msg.process_value) < 0.01, "joint 5 failed"
	print('joint 5 passed test')


def check_joint6(msg):
	assert abs(msg.set_point-msg.process_value) < 0.01, "joint 6 failed"
	print('joint 6 passed test')
	

def check_joint7(msg):
	assert abs(msg.set_point-msg.process_value) < 0.01, "joint 7 failed"
	print('joint 7 passed test')

def check_joint8(msg):
	assert abs(msg.set_point-msg.process_value) < 0.01, "joint 8 failed"
	print('joint 8 passed test')

def my_robot_joint_positions_subscriber():
	counter = 0
	rospy.init_node('image_listener')

	wheel1_topic = '/crobot/joint5_position_controller/state'
	wheel2_topic = '/crobot/joint6_position_controller/state'
	wheel3_topic = '/crobot/joint7_position_controller/state'
	wheel4_topic = '/crobot/joint8_position_controller/state'

	rospy.Subscriber(wheel1_topic,JointControllerState,check_joint5)
	rospy.Subscriber(wheel2_topic,JointControllerState,check_joint6)
	rospy.Subscriber(wheel3_topic,JointControllerState,check_joint7)
	rospy.Subscriber(wheel4_topic,JointControllerState,check_joint8)


	rospy.spin()


if __name__ == '__main__':
	my_robot_joint_positions_subscriber()