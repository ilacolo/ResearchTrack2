#! /usr/bin/env python3

"""
..module: Node B: action_client node
  :platform: unix
  :synopsis: Node B: rob_pos_vel node
  
  ..moduleauthor:: Ilaria Colomba s4829201
  

"""
  

#The aim of this second assignment is to develop a mobile robot simulator in ROS. 
#The robot has to be able to move in the desired position which is the input insert 
#by the user with the keyboard. The robot is situated in a 3D simulation environment called "Gazebo". 
#To do this, it is requested to crete a new package, in which three different nodes are implemented.

# In this part it is implemented a service node that, when called, returns the coordinates of the last target sent by the user.

import rospy
import time
import math
import assignment_2_2023.msg
from assignment_2_2023.msg import pos_vel_info


#select the frequency (frequency) and the last time printed (old) information
frequency = 1.0
old = 0
""" Select the frequency and the last time printed (old) information """

############################################## FUNCTIONS ######################################################

def pos_vel_dist(msg):
	"""
	Function which compute the distance between
	the robot and the goal and also the velocity of the robot.
	
	Arg: msg(RobotMsg): it contains the coordinates of velocity of the robot

	"""
	
	global frequency
	""" gloabl variable of frequency """
	global old_time
	""" global variable of old time""" 
	
	#compute period [ms], and the time [ms]
	period = (1.0/freq) * 100
	""" Compute period: 1.0/frequency * 100 [ms] """
	now_time = time.time() * 1000
	""" Compute the time [ms]"""
	
	#if the time which is passed from the last time the function
	#can compute and print the distance and the velocity of the robot
	if now_time - old_time > period:
		des_x = rospy.get_param("des_pos_x")
		des_y = rospy.get_param("des_pos_y")
		dist = math.sqrt(pow(des_x - msg.x, 2) + pow(des_y - msg.y, 2))
		print("the goal distance is: ")
		print(dist)
		speed = math.sqrt(pow(msg.vel_x, 2) + (msgh.vel_y, 2))
		print("the average speed is: ")
		print(speed)
		""" If it is passed from the last time, the function can compute and print the distance and the velocity of the robot """
		
		#update time
		old_time = now_time
		""" Update time """

############################################## MAIN ######################################################
	
def main():
	"""
	The main function to be called at the end.

	Args: None
	"""

	global frequency
	
	#initilize the node
	rospy.init_node('rob_vel_pos')
	""" Initialize the node """
		
	#define the subscriber:
	sub_res = rospy.Subscriber('/pos_vel', pos_vel_info , pos_vel_dist)
	""" Subscriber for the robot's position and velocity """
	
	#keep the node running
	rospy.spin()
	""" Keep the node running """
	
if __name__ == "__main__":
	main()
	
