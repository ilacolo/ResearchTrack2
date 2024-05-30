#! /usr/bin/env python3


"""
.. module:: action_client
   :platform: unix
   :synopsis: Node A: action_client node
  
.. moduleauthor:: Ilaria Colomba <s4829201>

In this part, the node A is implemented. It acts as an action client, allowing the user to set 
a target (x, y) or to cancel it. It uses the feedback/status of the action server to determine 
when the target has been reached. The node also publishes the robot position and velocity as 
a custom message (x, v, vel_x, vel_z), relying on the values published on the topic /odom.
To do that three different functions are implemented.

Subscribes to: 
    /odom
Publishes to:
    /pos_vel
"""

import rospy
import actionlib
import actionlib.msg
import assignment_2_2023.msg
from std_srvs.srv import*
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Twist
from assignment_2_2023.msg import pos_vel_info


def pos_and_vel(msg):
	"""
	Callback function to publish position and velocity of the robot taken from */odom*. It gest the position, the linear velocity and the angular velocity of the robot from the msg. 
	Then it creates the custm message and it assigns the parameters of the costum message. At the end it publishes the costum message. 
	
	Args: msg(Odometry): Contains the odometry of the robot
	"""
	
	global pub
	
	#get the position and the velocity
	pos = msg.pose.pose.position
	
	vel = msg.twist.twist.linear

	vel_ang = msg.twist.twist.angular

	#custome message
	info_pos_vel = pos_vel_info()
	
	#assign the parameters of the custume message
	info_pos_vel.x = pos.x
	info_pos_vel.y = pos.y
	info_pos_vel.v_x = vel.x
	info_pos_vel.v_y = vel.z

	#publish the custum message
	pub.publish(info_pos_vel)

def target():

	"""
	Function which allows to obtain the the x and the y target position, desired by the user. 
	It also allows to cancel the target position. It obtains the 'x' and the 'y' target position by the user asking him/her to insert the desired value. 
	Then it Create the goal position that the robot has to reach. It also sends the goal to the server, waiting for the server to be ready. After that, it asks the user 
	to eventually delete the desired position, otherwise it will be reached". If the user want to delete the goal, the comunication is sent to the server, 
	otherwise the goal is reached.
	
	Args: none 
	"""
	rospy.sleep(3)

	#Obtain the x and y target position by the user
	x = float (input ("INSERT THE X DERIRED POSITION: "))
	y = float (input ("INSERT THE Y DERIRED POSITION: "))
	
	#Goal message with the position that the robot has to reach
	goal = assignment_2_2023.msg.PlanningGoal()
	goal.target_pose.pose.position.x = x
	goal.target_pose.pose.position.y = y
	
	#action client
	client = actionlib.SimpleActionClient('/reaching_goal', assignment_2_2023.msg.PlanningAction)

	#wait for the server to be ready
	client.wait_for_server()
	
	#Send the goal to the client
	delete_value = input("In order to delete the target position, print 'd', otherwhise print a letter or a number: " )
	
	if (delete_value == 'D'):
    		#if (delete_value == "D"):
		client.cancel_goal()
		print("The goal is deleted")

		#else:
		#	print("The value is not correct, try again")
	else:
		client.send_goal(goal)

		print("The target position is always the same")
		print("Target sent to the server")
		

def main():
	"""
	The main function to be called at the end. In this part of the code the node is initialized. Then it defines the publisher: it sends a message with position and velocity. And it defines the 		subscriber: it gets from "Odom" the position and the velocity. At the end it calls the function target()

	Args: None
	"""

	#initialize the node
	rospy.init_node('action_client')
	
	global pub
		
	#define the publisher: it sends a message with position and velocity
	pub = rospy.Publisher("/pos_vel", pos_vel_info, queue_size=1)
	
	#define the subscriber: it gets from "Odom" the position and the velocity
	sub = rospy.Subscriber("/Odom", Odometry, pos_and_vel)

	#calling the function
	target()

if __name__ == '__main__':
	main()
	
	
	
	
	
