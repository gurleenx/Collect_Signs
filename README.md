# Collect-signs
Task1:-

You are the project head of an amazon development team working on a robot-based packaging solution for the assistance of humans. 
The task for the robot is to visit all special locations in the warehouse avoiding static obstacles
and returning to the initial position(0,0). 
If the robot can't visit all special location return the maximum count of 
special locations it can visit also return the path the robot took to reach special locations. 
An image is given as input which contains a grid of dimension  (m_row*n_col). 
Further, the grid can only have three possible values in them  (-,+, empty). 
Static obstacles denoted by "-" and special locations by "+" and nothing denoted by blank space

The robot can go from 1 cell to others in any of the four primary directions (up, down, east, west)

m_row,n_col<100

#######################################################################################################################
The python code makes an excellent use of template matching, recurssion and backtracking to find the shorted path possible 
in collecting all the plus points that can be collected in a grid of no go zones and way paths.
It makes use of OpenCV, numpy and matplotlib libraries.
