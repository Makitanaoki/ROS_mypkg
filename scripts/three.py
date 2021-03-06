#!/usr/bin/env python3

#Copyright (C) 2021 Naoki Makita, Ryuichi Ueda

import rospy
from std_msgs.msg import Int32

rospy.init_node('three')
pub = rospy.Publisher('three', Int32, queue_size=1)
rate = rospy.Rate(1)
n = 0
while not rospy.is_shutdown():
    n -= 1
    pub.publish(n)
    rate.sleep()
