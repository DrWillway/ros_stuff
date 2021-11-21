#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Bool

var = False

def bool_callback(msg):
    global var
    var = msg.data
    
def simple_node():
    rospy.init_node('simple_sub_pub', anonymous=False)

    rospy.Subscriber("bool_data", Bool, bool_callback)
    pub = rospy.Publisher("str_data", String, queue_size=10)

    rate = rospy.Rate(10) # speed of the while node

    global var

    while not rospy.is_shutdown():
        if var:
            pub.publish("On")
        else:
            pub.publish("False")
            
        rate.sleep()

if __name__ == '__main__':
    simple_node()