#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0
x = 0

def cb(message):
    global n
    n = message.data*2

def db(message2):
    global x
    x = message2.data*(-2)

rospy.init_node('twice')
sub = rospy.Subscriber('count_up', Int32, cb)
sub = rospy.Subscriber('three', Int32, db)
pub = rospy.Publisher('twice', Int32, queue_size=1)
rate = rospy.Rate(2)
while not rospy.is_shutdown():
    pub.publish(n)
    pub.publish(x)
    rate.sleep()
