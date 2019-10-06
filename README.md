INSTRUCTION OF LAUNCH:
If you want to see my robot in gazebo you need to create new folder(package) 
in foler "name_workspase"/src/ ,for example,"robot-gazebo". After you need to download from my repository in created
new folder("robot-gazebo") such as folder and files: "launch" , "urdf" , "CMakeLists.txt" and "package.xml".
Then you need to open console and enter comands in you workspace: 
1)source devel/setup.bash
2)catkin_make
3)roslaunch "name_package" begin.launch  "(for example: roslaunch robot_gazebo begin.launch )"

ROBOT DISCRIPTION: robot-platform with 4 wheels and base (big cylinder) each of wheels attached to 2 links. Together 2 links 
can rotate and so my robot can move around center of base. Also he can turn using small radius of turning.
