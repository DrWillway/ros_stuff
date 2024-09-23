# ros_stuffs

This repository contains a collection of basic ROS (Robot Operating System) examples designed for educational purposes. These examples include simple publishers, subscribers, services, actions.

### Create python package

```
cd ros2_ws/src && ros2 pkg create my_python_pkg --build-type ament_python 

cd ~/ros2_ws/src/my_python_pkg/my_python_pkg/

touch my_python_node.py
```

Now that we have a Python file, we need to add an entry point in the setup.py file.

```
entry_points={
    'console_scripts': [
        'any_name = my_python_pkg.my_python_node:main'
    ],
},
```

### Create interfaces (msg/srv) package

```
ros2 pkg create --build-type ament_cmake my_interfaces

cd ~/ros2_ws/src/my_interfaces && mkdir msg srv

cd srv && touch Test.srv
```

Create service definition (input and return) in Test.srv
```
string data
---
bool success
```

Add dependencies to CMakeLists.txt:
```
find_package(std_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/Test.srv"
  DEPENDENCIES std_msgs # Add packages that above messages depend on
)
```

Add dependencies to package.xml:
```
<depend>std_msgs</depend>
<buildtool_depend>rosidl_default_generators</buildtool_depend>
<exec_depend>rosidl_default_runtime</exec_depend>
<member_of_group>rosidl_interface_packages</member_of_group>
```