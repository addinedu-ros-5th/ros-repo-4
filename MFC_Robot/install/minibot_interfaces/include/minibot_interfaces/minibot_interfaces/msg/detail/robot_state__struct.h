// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from minibot_interfaces:msg/RobotState.idl
// generated code does not contain a copyright notice

#ifndef MINIBOT_INTERFACES__MSG__DETAIL__ROBOT_STATE__STRUCT_H_
#define MINIBOT_INTERFACES__MSG__DETAIL__ROBOT_STATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

/// Struct defined in msg/RobotState in the package minibot_interfaces.
typedef struct minibot_interfaces__msg__RobotState
{
  std_msgs__msg__Header header;
  bool enable_motor;
  uint8_t left_lamp;
  uint8_t right_lamp;
} minibot_interfaces__msg__RobotState;

// Struct for a sequence of minibot_interfaces__msg__RobotState.
typedef struct minibot_interfaces__msg__RobotState__Sequence
{
  minibot_interfaces__msg__RobotState * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} minibot_interfaces__msg__RobotState__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MINIBOT_INTERFACES__MSG__DETAIL__ROBOT_STATE__STRUCT_H_
