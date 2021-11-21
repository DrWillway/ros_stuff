#!/usr/bin/env python
 
import rospy
#we need SimpleService for the first message type,
#and the SimpleServiceResponse from the second message type from the  SimpleService.srv file
from ros_service.srv import SimpleService, SimpleServiceResponse
 
def turn_on_off(mess):
 if mess.onezero==1:
    return  SimpleServiceResponse('ON')
 else:
    return  SimpleServiceResponse('OFF')
 
 
rospy.init_node('service_respond')
 
service=rospy.Service('service_example',SimpleService,turn_on_off)
 
rospy.spin()
