// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from task_manager:msg/SendAllocationResults.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__MSG__DETAIL__SEND_ALLOCATION_RESULTS__STRUCT_H_
#define TASK_MANAGER__MSG__DETAIL__SEND_ALLOCATION_RESULTS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'robot_name'
// Member 'goal_location'
// Member 'task_assignment'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/SendAllocationResults in the package task_manager.
typedef struct task_manager__msg__SendAllocationResults
{
  /// Robo1
  rosidl_runtime_c__String robot_name;
  /// I1
  rosidl_runtime_c__String goal_location;
  /// 입고
  rosidl_runtime_c__String task_assignment;
} task_manager__msg__SendAllocationResults;

// Struct for a sequence of task_manager__msg__SendAllocationResults.
typedef struct task_manager__msg__SendAllocationResults__Sequence
{
  task_manager__msg__SendAllocationResults * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} task_manager__msg__SendAllocationResults__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TASK_MANAGER__MSG__DETAIL__SEND_ALLOCATION_RESULTS__STRUCT_H_
