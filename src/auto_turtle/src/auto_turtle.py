#! /usr/bin/python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import random

rospy.init_node("auto_turtle")


def callback(msg):
    vel_msg = Twist()
    if msg.x > 10:
        vel_msg.linear.x = -2.1
        vel_msg.angular.z = 0

    elif msg.x < 1:
        vel_msg.linear.x = -2.1
        vel_msg.angular.z = 0

    elif msg.y > 10:
        vel_msg.linear.x = -2.1
        vel_msg.angular.z = 0

    elif msg.y < 1:
        vel_msg.linear.x = -2.1
        vel_msg.angular.z = 0
    else:
        vel_msg.linear.x = random.randint(0, 2)
        vel_msg.angular.z = random.randint(-2, 2)
    velocity_publisher.publish(vel_msg)


velocity_publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=1)
rospy.Subscriber("/turtle1/pose", Pose, callback)


while not rospy.is_shutdown():
    rospy.spin()  # to keep it running as long as messages are being given
