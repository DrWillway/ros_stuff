#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from ros_service.srv import SimpleService, SimpleServiceResponse
 
def on_off(state):
    rospy.wait_for_service('service_example')
    try:
        service_example = rospy.ServiceProxy('service_example', SimpleService)
        resp1 = service_example(state)
        return resp1.turn
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [int state]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        state = int(sys.argv[1])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s"%(state))
    print("State is %s"%(state, on_off(state)))
