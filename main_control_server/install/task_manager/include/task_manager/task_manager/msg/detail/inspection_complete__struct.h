// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from task_manager:msg/InspectionComplete.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__MSG__DETAIL__INSPECTION_COMPLETE__STRUCT_H_
#define TASK_MANAGER__MSG__DETAIL__INSPECTION_COMPLETE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'product_code'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/InspectionComplete in the package task_manager.
typedef struct task_manager__msg__InspectionComplete
{
  rosidl_runtime_c__String product_code;
} task_manager__msg__InspectionComplete;

// Struct for a sequence of task_manager__msg__InspectionComplete.
typedef struct task_manager__msg__InspectionComplete__Sequence
{
  task_manager__msg__InspectionComplete * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} task_manager__msg__InspectionComplete__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TASK_MANAGER__MSG__DETAIL__INSPECTION_COMPLETE__STRUCT_H_
