#!/usr/bin/env python
# license removed for brevity

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client():

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    # Sequence
    goal_seq = [-3.729 , -2.0870 , 0.0,
                -3.815 ,  2.6960 , 0.0,
                 3.006 ,  6.0145 , 0.0,
                 4.405 ,  0.1893 , 0.0,
                 4.418 , -4.6819 , 0.0,
                -3.729 , -2.0870 , 0.0]
    
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    for i in range(0,6):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()

        goal.target_pose.pose.position.x = goal_seq[0+i*3]
        goal.target_pose.pose.position.y = goal_seq[1+i*3]
        goal.target_pose.pose.position.z = goal_seq[2+i*3]

        goal.target_pose.pose.orientation.w = 0.1233
        goal.target_pose.pose.orientation.z = 0.9923

        client.send_goal(goal)
        wait = client.wait_for_result()
        if not wait:
            rospy.logerr("Action server DOWN ;/ ")
        else:
            print("A Goal is Executed")
    return 1
if __name__ == '__main__':
    try:
        rospy.init_node('movebaseClient')
        result = movebase_client()
        if result:
            rospy.loginfo("All Goals EXECUTED!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation DONE ")