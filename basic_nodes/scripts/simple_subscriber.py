#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo(msg)

def simple_node():

    rospy.init_node('simple_sub', anonymous=False)
    sub_string = rospy.Subscriber('str_data', String, callback)

    rospy.spin() # if working with Subscriber only spin() is enough to start the node

    #rate = rospy.Rate(10) # 10hz

    #while not rospy.is_shutdown():
    #    rate.sleep()


if __name__ == '__main__':
    simple_node()