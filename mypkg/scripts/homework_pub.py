#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

if __name__=='__main__':
    rospy.init_node('homework_pub')
    pub = rospy.Publisher('mes', String, queue_size=50)
    #rate = rospy.Rate(10)
    while not rospy.is_shutdown(): #終了処理がされるまで無限ループ
        mes = String()
        input_key = None
        print "comand ->" 
        input_key = raw_input()
        if input_key == "tennki":
            mes.data = "空見りゃ分かるだろ。"
        elif input_key == "unnsei":
            mes.data = "君の人生はその日の運勢で左右されてしまうのかい?"
        elif input_key == "uedasennsei":
            mes.data = '素晴らしい先生だと常々思っております。'
        #mes.data = "ros homework"
        pub.publish(mes)
        #rate.sleep()
