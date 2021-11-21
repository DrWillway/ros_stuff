#!/usr/bin/env python
# license removed for brevity

import rospy
from geometry_msgs.msg import Twist

class GoForward():
    def __init__(self):
        # initiliaze
        rospy.init_node('GoForward', anonymous=False)

        # tell user how to stop TurtleBot
        rospy.loginfo("To stop TurtleBot CTRL + C")

        rospy.on_shutdown(self.shutdown)

        self.cmd_vel = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

        #TurtleBot will stop if we don't keep telling it to move.  How often should we tell it to move? 10 HZ
        r = rospy.Rate(10)

        move_cmd = Twist()
        move_cmd.linear.x = 0.2

        move_cmd.angular.z = 0

        while not rospy.is_shutdown():
            self.cmd_vel.publish(move_cmd)
            r.sleep()
                        
        
    def shutdown(self):
        # stop turtlebot
        rospy.loginfo("Stop TurtleBot")
        self.cmd_vel.publish(Twist())

        rospy.sleep(1)
 
if __name__ == '__main__':
    try:
        GoForward()
    except:
        rospy.loginfo("GoForward node terminated.")