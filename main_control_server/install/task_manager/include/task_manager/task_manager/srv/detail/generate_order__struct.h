// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from task_manager:srv/GenerateOrder.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__SRV__DETAIL__GENERATE_ORDER__STRUCT_H_
#define TASK_MANAGER__SRV__DETAIL__GENERATE_ORDER__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/GenerateOrder in the package task_manager.
typedef struct task_manager__srv__GenerateOrder_Request
{
  uint8_t structure_needs_at_least_one_member;
} task_manager__srv__GenerateOrder_Request;

// Struct for a sequence of task_manager__srv__GenerateOrder_Request.
typedef struct task_manager__srv__GenerateOrder_Request__Sequence
{
  task_manager__srv__GenerateOrder_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} task_manager__srv__GenerateOrder_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'item_ids'
// Member 'names'
// Member 'warehouses'
// Member 'racks'
// Member 'cells'
// Member 'statuses'
#include "rosidl_runtime_c/string.h"
// Member 'quantities'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/GenerateOrder in the package task_manager.
typedef struct task_manager__srv__GenerateOrder_Response
{
  rosidl_runtime_c__String__Sequence item_ids;
  rosidl_runtime_c__String__Sequence names;
  rosidl_runtime_c__int32__Sequence quantities;
  rosidl_runtime_c__String__Sequence warehouses;
  rosidl_runtime_c__String__Sequence racks;
  rosidl_runtime_c__String__Sequence cells;
  rosidl_runtime_c__String__Sequence statuses;
} task_manager__srv__GenerateOrder_Response;

// Struct for a sequence of task_manager__srv__GenerateOrder_Response.
typedef struct task_manager__srv__GenerateOrder_Response__Sequence
{
  task_manager__srv__GenerateOrder_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} task_manager__srv__GenerateOrder_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TASK_MANAGER__SRV__DETAIL__GENERATE_ORDER__STRUCT_H_
