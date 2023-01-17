#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *


rospy.init_node("pub_float32_array")
pub = rospy.Publisher("data", Float32MultiArray, queue_size=10)

r = rospy.Rate(10)

msg = Float32MultiArray()
for i in range(100000):
  msg.data.append(3)

while not rospy.is_shutdown():
  pub.publish(msg)
  r.sleep()
