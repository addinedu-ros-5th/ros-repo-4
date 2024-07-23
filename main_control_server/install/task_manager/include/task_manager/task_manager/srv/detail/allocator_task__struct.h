// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from task_manager:srv/AllocatorTask.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__SRV__DETAIL__ALLOCATOR_TASK__STRUCT_H_
#define TASK_MANAGER__SRV__DETAIL__ALLOCATOR_TASK__STRUCT_H_

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
// Member 'task_type'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/AllocatorTask in the package task_manager.
typedef struct task_manager__srv__AllocatorTask_Request
{
  rosidl_runtime_c__String product_code;
  rosidl_runtime_c__String task_type;
} task_manager__srv__AllocatorTask_Request;

// Struct for a sequence of task_manager__srv__AllocatorTask_Request.
typedef struct task_manager__srv__AllocatorTask_Request__Sequence
{
  task_manager__srv__AllocatorTask_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} task_manager__srv__AllocatorTask_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'robot_name'
// Member 'goal_location'
// Member 'task_assignment'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in srv/AllocatorTask in the package task_manager.
typedef struct task_manager__srv__AllocatorTask_Response
{
  rosidl_runtime_c__String robot_name;
  rosidl_runtime_c__String goal_location;
  rosidl_runtime_c__String task_assignment;
} task_manager__srv__AllocatorTask_Response;

// Struct for a sequence of task_manager__srv__AllocatorTask_Response.
typedef struct task_manager__srv__AllocatorTask_Response__Sequence
{
  task_manager__srv__AllocatorTask_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} task_manager__srv__AllocatorTask_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TASK_MANAGER__SRV__DETAIL__ALLOCATOR_TASK__STRUCT_H_
