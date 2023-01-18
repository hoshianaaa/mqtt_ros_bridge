#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *


rospy.init_node("pub_float64_array")
pub = rospy.Publisher("data", Float64MultiArray, queue_size=10)

r = rospy.Rate(10)

msg = Float64MultiArray()
for i in range(100000):
  msg.data.append(3)

while not rospy.is_shutdown():
  pub.publish(msg)
  r.sleep()
