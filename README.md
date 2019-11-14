# MY FIRST ROBOT

## INSTRUCTION OF LAUNCH
If you want to see my robot in gazebo you need to download from my repository package(folder) "my_robot_gazebo" in folder "src" which is located in your workspace. Then you need to open console and enter comands in your workspace:
```
source devel/setup.bash
catkin_make
roslaunch my_robot_gazebo xacro.launch 
```

## ROBOT DESCRIPTION 
Robot-platform with 4 wheels and base (big cylinder) each of wheels attached to 2 links. Together 2 links can rotate and so my robot can move around center of base. Also he can turn using small radius of turning.

## SCREENS OF MY ROBOT IN GAZEBO
- location: /MY-Robot/screens_robot/

View from one side 
![screenshot of sample](https://github.com/StalkerSanya/MY-Robot/blob/master/screens_robot/Screenshot%20robot_gazebo2.jpg)

View from another side
![screenshot of sample](https://github.com/StalkerSanya/MY-Robot/blob/master/screens_robot/Screenshot_robot_gazebo1.jpg)  

## ROBOT CONTROL
Control of robot launches by launch "xacro.launch". So "xacro.launch" create node which opens file "movesctript.py" for control.

Video below shows movemaent of each joint:
 - link to video: https://www.youtube.com/watch?v=6L06_kYmk1I

## SENSOR CAMERA
For moving wheel with camera and create 5 pictures you can launch "xacro.launch", which launches 2 node for launching 2 scripts with publisher and subscriber. 

- Location 5 pictures from camera: /MY-Robot/screens_robot/

Video below shows that all work:
 - link to video: https://youtu.be/D4T99M6cHCM