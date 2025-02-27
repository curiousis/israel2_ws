#! /usr/bin/python3


import rospy
from std_msgs.msg import String


def callback(msg):
    message = f"republish message {msg}"
    pub.publish(message)


rospy.init_node("talker_listener")

pub = rospy.Publisher("simple_pub_sub", String)

rospy.Subscriber("simple_pub", String, callback)

rospy.spin()
