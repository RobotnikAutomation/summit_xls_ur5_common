#!/usr/bin/env python

# Software License Agreement (BSD License)
#
# Copyright (c) 2015, Robotnik
# All rights reserved.
#

"""@package docstring
Package to publish the Robotiq position to ROS joint_states
"""

import roslib; roslib.load_manifest('robotiq_c_model_control')
import rospy
from sensor_msgs.msg import JointState as JointStateRobotiqC
from std_msgs.msg import String
from robotiq_c_model_control.msg import _CModel_robot_input as inputMsg

joint_states_pub = rospy.Publisher('/joint_states', JointStateRobotiqC, queue_size='5')

def readStatus(status):
    """read the status string and process it by the statusInterpreter function."""
    statusInterpreter(status)

def CModelStatusPublisher():
    """Initialize the node and subscribe to the CModelRobotInput topic."""
    rospy.init_node('CModelStatusPublisher')
    rospy.Subscriber("CModelRobotInput", inputMsg.CModel_robot_input, readStatus)
#    joint_states_pub = rospy.Publisher('/joint_states', JointStateRobotiqC, queue_size='5')
    rospy.spin()

def statusInterpreter(status):
    """Generate a string according to the current value of the status variables."""
    #status.gACT 0=reset 1=activation
    #gGTO 0=standby 1=go to pos request
    #gSTA 0=reset or autorelease 1=activation in progress 3=activation completed
    #if(status.gSTA == 3):
    #    output += 'Activation is completed\n'
    #gOBJ 0=fingers in motion 1=fingers stopped due to contact while openning
    #     2=fingers stopped due to contact closing 3=fingers are at requested pos
    #gFLT 0=no fault, 1= ...
    #gPR  requested position for the Gripper
    #gPO  real position of Fingers
    #output = 'gPO = ' + str(status.gPO / 255.0 * 0.86) + ': '
    #output += 'Position of Fingers: ' + str(status.gPO) + '\n'
    #gCU  current of fingers value * 10 [mA]
    msg = JointStateRobotiqC()
    msg.name = ['robotiq_85_left_knuckle_joint']
    msg.position = [status.gPO / 255.0 * 0.86]
    msg.velocity = []
    msg.effort = []
    msg.header.stamp = rospy.Time.now()
    msg.header.frame_id = 'base_link'
    joint_states_pub.publish(msg)

#    return output
    
if __name__ == '__main__':
    CModelStatusPublisher()

