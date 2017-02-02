#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def mes_function(message):
    rospy.loginfo("%s",message.data) #受信したmessageを表示

if __name__=='__main__':
    rospy.init_node('homework_sub')
    sub = rospy.Subscriber('mes', String, mes_function)
    rospy.spin() #無限ループしながら受信を待つ
