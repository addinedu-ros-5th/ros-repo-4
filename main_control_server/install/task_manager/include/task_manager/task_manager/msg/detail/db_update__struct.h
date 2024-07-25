// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from task_manager:msg/DbUpdate.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__MSG__DETAIL__DB_UPDATE__STRUCT_H_
#define TASK_MANAGER__MSG__DETAIL__DB_UPDATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'status'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/DbUpdate in the package task_manager.
typedef struct task_manager__msg__DbUpdate
{
  rosidl_runtime_c__String status;
} task_manager__msg__DbUpdate;

// Struct for a sequence of task_manager__msg__DbUpdate.
typedef struct task_manager__msg__DbUpdate__Sequence
{
  task_manager__msg__DbUpdate * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} task_manager__msg__DbUpdate__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TASK_MANAGER__MSG__DETAIL__DB_UPDATE__STRUCT_H_
