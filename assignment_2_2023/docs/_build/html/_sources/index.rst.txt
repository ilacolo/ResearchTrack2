.. Node A: action_client_node documentation master file, created by
   sphinx-quickstart on Fri May 24 19:31:30 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Node A: action_client_node's documentation!
======================================================

This is the documentation of the node A implemented for the 2nd assignment.


.. toctree::
   :maxdepth: 2
   :caption: Contents:


Assignment_2_2023 documentation
*****************************************

The aim of this second assignment is to develop a mobile robot simulator in ROS. 
The robot has to be able to move to the desired position which is input by the user with the keyboard. 
The robot is situated in a 3D simulation environment called "Gazebo". 
To do this, it is requested to create a new package, in which three different nodes are implemented.
A node A that implements an action client, allowing the user to set a target (x, y) or to cancel it. Try to use the feedback/status of the action server to k now then the target has been reached. The node also publishes the robot position and velocity as a custom message (x,v,vel_x,vel_z), by relying on the values published on the topic/odom.
A service node B that, when called, returns the coordinates of the last target sent by the user.
Another service node C that subscribes to the robot's position and velocity (using the custom message) and implements a server to retrieve the distance of the robot from the target the target and the robot's average speed.

Action_client node
==================

.. automodule:: scripts.action_client
   :members:
   


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

