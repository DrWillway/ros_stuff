#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Int32

int_data = 0

def str_callback(msg):
    rospy.loginfo(rospy.get_caller_id() + " received %s", msg.data)
    
def int_callback(data):
    #rospy.loginfo(data)
    global int_data
    int_data = data.data
    
def simple_node():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('simple_subs', anonymous=False)

    rospy.Subscriber("str_data", String, str_callback)
    rospy.Subscriber("int_data", Int32, int_callback)

    rate = rospy.Rate(10) # 10hz

    global int_data

    while not rospy.is_shutdown():
        print(int_data)
        rate.sleep()
        #rospy.spin()

if __name__ == '__main__':
    simple_node()