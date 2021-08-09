#!/usr/bin/env python
# license removed for brevity


# Robot auto move from one point to one goal. When it reach the goal, it will stop. 
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client():

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()
    
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = -3.729
    goal.target_pose.pose.position.y = -2.0870
    goal.target_pose.pose.position.z = 0.0

    goal.target_pose.pose.orientation.w = 0.1233
    goal.target_pose.pose.orientation.z = 0.9923



    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server DOWN ;/ ")
    else:
        return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('movebaseClient')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal is EXECUTED :l ")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation DONE ")