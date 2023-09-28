cmake_minimum_required(VERSION 3.8)
project(my_bot)

# set(THIS_PACKAGE_INCLUDE_DEPENDS
#   hardware_interface
#   pluginlib
#   rclcpp
#   rclcpp_lifecycle
# )

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()


# find_package(ament_cmake REQUIRED)
# foreach(Dependency IN ITEMS ${THIS_PACKAGE_INCLUDE_DEPENDS})
#   find_package(${Dependency} REQUIRED)
# endforeach()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
find_package(urdf REQUIRED)

# # COMPILE
# add_library(mpu6050_hardware_interface SHARED
#   src/mpu6050_hardware_interface.cpp
#   src/mpu6050_lib.cpp
# )

# target_include_directories(mpu6050_hardware_interface PRIVATE	include)

# ament_target_dependencies(mpu6050_hardware_interface ${THIS_PACKAGE_INCLUDE_DEPENDS})

# # Link i2c library to mpu6050_hardware_interface target
# target_link_libraries(mpu6050_hardware_interface i2c)

# # Export hardware plugin
# pluginlib_export_plugin_description_file(hardware_interface mpu6050_hardware.xml)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()


# INSTALL
# install(
#   DIRECTORY include/
#   DESTINATION include/mpu6050_hardware_interface
# )
# install(
#   TARGETS mpu6050_hardware_interface
#   DESTINATION share/${PROJECT_NAME}
#   RUNTIME DESTINATION lib
#   LIBRARY DESTINATION lib/${PROJECT_NAME}
# )

install(
  DIRECTORY config description launch meshes include src
  DESTINATION share/${PROJECT_NAME}
)


# # EXPORTS
# ament_export_libraries(mpu6050_hardware_interface)

# include_directories(include)

# # Create Cpp executable
# add_executable(mpu6050_offsets src/mpu6050_lib.cpp src/mpu6050_offsets.cpp)

# # Install Cpp executables
# install(TARGETS
#   DESTINATION lib/${PROJECT_NAME}
# )

# # Link i2c to mpu6050_offsets
# target_link_libraries(mpu6050_offsets i2c)

ament_package()
