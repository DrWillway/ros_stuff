#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist, Pose, Vector3
from turtlesim.msg import Pose

from scipy.spatial import distance
import math 

class goalControl:
    def __init__(self):

        cmd_topic = rospy.get_param('~cmd_topic', "/turtle1/cmd_vel")
        odom_topic = rospy.get_param('~odom_topic', "/turtle1/pose")
        goal_topic = rospy.get_param('~goal_topic',  "/turtle1/goal")

        # Publisher
        self.cmd_pub = rospy.Publisher(cmd_topic, Twist, queue_size = 1)
        self.robot_pose = [0,0]
        self.robot_theta = 0.0
        self.robot_speed = Twist()

        #Subscribers
        rospy.Subscriber(odom_topic, Pose, self.odom_callback)
        rospy.Subscriber(goal_topic, Vector3, self.goal_callback)

    def odom_callback(self, msg):
        print(msg)
        self.robot_pose[0] = msg.x
        self.robot_pose[1] = msg.y
        self.robot_theta = msg.theta

    def move_to_goal(self, coords, reach_goal_accuracy):
        if coords != None:
            dist = distance.euclidean(coords, self.robot_pose)
            if(dist > reach_goal_accuracy): 
                x = coords[0]
                y = coords[1]

                inc_x = x - self.robot_pose[0]
                inc_y = y - self.robot_pose[1]
            
                rot = math.atan2(inc_y, inc_x) * 180/3.14
            
                if (rot<0):
                    rot = 360 + rot
                    
                ang = self.robot_theta * 180/3.14
                angR = rot - ang

                if (abs(angR) > 180):
                    angR = angR - (angR/abs(angR))*360

                if angR > 20:
                    self.robot_speed.linear.x = 0.0
                    self.robot_speed.angular.z = 0.8
                elif angR < -20:
                    self.robot_speed.linear.x = 0.0
                    self.robot_speed.angular.z = -0.8
                else:
                    self.robot_speed.linear.x = 0.6
                    self.robot_speed.angular.z = angR/10.0 
            else:
                self.robot_speed.linear.x = 0.0
                self.robot_speed.angular.z = 0.0

            self.cmd_pub.publish(self.robot_speed)

    def goal_callback(self, msg):
        goal = [msg.x,msg.y]
        reach_goal_accuracy = msg.z
        self.move_to_goal(goal,reach_goal_accuracy)

    def main(self):
        rate_val = rospy.get_param('~rate', 10.0)
        rate = rospy.Rate(rate_val)
        try:
            rospy.spin()
        except KeyboardInterrupt:
            print("Shutting down")

if __name__ == '__main__':
    rospy.init_node('goal_control')
    try:
        goal_control = goalControl()
        goal_control.main()
    except rospy.ROSInterruptException: pass
