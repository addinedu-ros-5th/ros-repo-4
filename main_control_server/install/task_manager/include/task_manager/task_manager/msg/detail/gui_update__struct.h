// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from task_manager:msg/GuiUpdate.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__MSG__DETAIL__GUI_UPDATE__STRUCT_H_
#define TASK_MANAGER__MSG__DETAIL__GUI_UPDATE__STRUCT_H_

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
// Member 'status'
// Member 'message'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/GuiUpdate in the package task_manager.
typedef struct task_manager__msg__GuiUpdate
{
  rosidl_runtime_c__String product_code;
  rosidl_runtime_c__String status;
  rosidl_runtime_c__String message;
} task_manager__msg__GuiUpdate;

// Struct for a sequence of task_manager__msg__GuiUpdate.
typedef struct task_manager__msg__GuiUpdate__Sequence
{
  task_manager__msg__GuiUpdate * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} task_manager__msg__GuiUpdate__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TASK_MANAGER__MSG__DETAIL__GUI_UPDATE__STRUCT_H_
