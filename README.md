# ros_stuffs

This repository contains a collection of basic ROS (Robot Operating System) examples designed for educational purposes. These examples include simple publishers, subscribers, and a basic reactive navigation controller. More examples may be added over time.

## Repository Structure

- **basic_nodes**
  - `simple_publisher.py`: A basic ROS node that publishes messages to a topic.
  - `simple_subscriber.py`: A ROS node that subscribes to a topic and logs received messages.
  - `simple_subscriber_publisher.py`: A node that subscribes to one topic and publishes to another.
  - `simple_subscribers.py`: Example of multiple subscribers in a single node.

- **reactive_nav.cpp**: 
  A basic reactive controller using laser scan data to avoid obstacles and navigate autonomously.

- **ros_service**
  - `srv/SimpleService.srv`: A custom service definition.
  - `src/callService.py`: A Python script to call the custom service.
  - `src/simpleService.py`: A service provider node.

- **turtle_controller**: 
  Includes files related to controlling a turtle in the simulated ROS turtle environment.

- **static_tf.launch**: 
  A launch file for setting up static transforms between coordinate frames.
