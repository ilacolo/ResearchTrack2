#! /usr/bin/env python3

"""
..module: Node C: action_client node
  :platform: unix
  :synopsis: Node C: service node
  
  ..moduleauthor:: Ilaria Colomba s4829201
  

"""
  

#The aim of this second assignment is to develop a mobile robot simulator in ROS. 
#The robot has to be able to move in the desired position which is the input insert 
#by the user with the keyboard. The robot is situated in a 3D simulation environment called "Gazebo". 
#To do this, it is requested to crete a new package, in which three different nodes are implemented.

#In this part it is implemented another service node that subscribes to the robot's position 
#and velocity (using the custom message) and implements a server to retrieve the distance of 
#the robot from the target the target and the robot's average speed.

import rospy
import assignment_2_2023.msg
from assignment_2_2023.srv import GetLastTarget, GetLastTargetResponse
import actionlib
import actionlib.msg


#initialize variable to count how many goals are reached and how many goals are deleted
goal_deleted = 0
goal_reached = 0

############################################## FUNCTIONS ######################################################

def results(msg):
	"""
	This function returns the reached position
	
	Args: msg: it contains the odometry of the robot
	"""
	
	global last_target_coordinates
	
	response = GetLastTargetResponse()
	response.coordinates = last_target_coordinates
	
	return response
	print(response)

def target_callback(msg):
	"""
	This function calls back the target 
	
	Args: msg: it contains the odometry of the robot
	"""
	
	global last_target_coordinates
	last_target_coordinates = msg.data
	
############################################## MAIN ######################################################
	
def main():
	"""
	The main function to be called at the end.

	Args: None
	"""

	#initialize the node
	rospy.init_node('service_node')
	""" Initialize the node """
	
	#define the subscriber: it gets from "Odom" the position and the velocity
	sub_result = rospy.Subscriber('/reaching_goal/result', assignment_2_2023.msg.PlanningActionResult, target_callback)
	""" Define the subscriber: it gets from "Odom" the position and the velocity """
	
	#keep the node running
	rospy.spin()
	""" Keep the node running """
	

if __name__ == '__main__':
	main()
	
	

