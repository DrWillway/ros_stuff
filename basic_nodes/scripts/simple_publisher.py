#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool 

def simple_node():

    rospy.init_node('simple_pub', anonymous=False)
    rospy.loginfo("simple_pub initialized")

    pub = rospy.Publisher('bool_data', Bool, queue_size=10) # can be any name

    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():

        pub.publish(True)

        rate.sleep()


if __name__ == '__main__':
    simple_node()