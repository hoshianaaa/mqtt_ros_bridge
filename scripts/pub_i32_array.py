#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *


rospy.init_node("pub_int32_array")
pub = rospy.Publisher("data", Int32MultiArray, queue_size=10)

r = rospy.Rate(10)

msg = Int32MultiArray()
for i in range(100000):
  msg.data.append(i)

while not rospy.is_shutdown():
  pub.publish(msg)
  r.sleep()
