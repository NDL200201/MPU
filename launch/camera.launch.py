import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    param_config = os.path.join(
        get_package_share_directory('my_bot'), 'config', 'param.yaml')

    return LaunchDescription([

        Node(
            package='realsense2_camera',
            executable='realsense2_camera_node',
            output='screen',
            namespace='camera',
            parameters=[{
                'image_size': [640,480],
                'time_per_frame': [1, 6],
                'camera_frame_id': 'camera_depth_frame'
                }]
    ),
        Node(
            package='depthimage_to_laserscan',
            executable='depthimage_to_laserscan_node',
            name='depthimage_to_laserscan',
            remappings=[('depth', '/camera/depth/image_rect_raw'),
                        ('depth_camera_info', '/camera/depth/camera_info'),
                        ('scan', '/rgbd_scan')],
            parameters=[param_config])
    ])