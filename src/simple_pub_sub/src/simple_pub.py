#! /usr/bin/python3
import rospy
from std_msgs.msg import String


rospy.init_node("talker")

pub = rospy.Publisher("simple_pub", String)

rate = rospy.Rate(1)  # one message per sec to be sent


while not rospy.is_shutdown():
    hello_string = "hello world! from ROS publisher"

    pub.publish(hello_string)

    rate.sleep()
