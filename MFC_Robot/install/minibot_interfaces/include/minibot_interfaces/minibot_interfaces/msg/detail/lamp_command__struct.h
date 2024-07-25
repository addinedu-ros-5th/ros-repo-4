// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from minibot_interfaces:msg/LampCommand.idl
// generated code does not contain a copyright notice

#ifndef MINIBOT_INTERFACES__MSG__DETAIL__LAMP_COMMAND__STRUCT_H_
#define MINIBOT_INTERFACES__MSG__DETAIL__LAMP_COMMAND__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/LampCommand in the package minibot_interfaces.
typedef struct minibot_interfaces__msg__LampCommand
{
  uint8_t l_command;
  uint8_t r_command;
} minibot_interfaces__msg__LampCommand;

// Struct for a sequence of minibot_interfaces__msg__LampCommand.
typedef struct minibot_interfaces__msg__LampCommand__Sequence
{
  minibot_interfaces__msg__LampCommand * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} minibot_interfaces__msg__LampCommand__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MINIBOT_INTERFACES__MSG__DETAIL__LAMP_COMMAND__STRUCT_H_
