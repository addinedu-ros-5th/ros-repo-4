// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robot_state:srv/UpdateDB.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_STATE__SRV__DETAIL__UPDATE_DB__STRUCT_H_
#define ROBOT_STATE__SRV__DETAIL__UPDATE_DB__STRUCT_H_

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
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/UpdateDB in the package robot_state.
typedef struct robot_state__srv__UpdateDB_Request
{
  rosidl_runtime_c__String robot_name;
} robot_state__srv__UpdateDB_Request;

// Struct for a sequence of robot_state__srv__UpdateDB_Request.
typedef struct robot_state__srv__UpdateDB_Request__Sequence
{
  robot_state__srv__UpdateDB_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_state__srv__UpdateDB_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'robot_name'
// Member 'battery_status'
// Member 'status'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in srv/UpdateDB in the package robot_state.
typedef struct robot_state__srv__UpdateDB_Response
{
  rosidl_runtime_c__String robot_name;
  rosidl_runtime_c__String battery_status;
  rosidl_runtime_c__String status;
} robot_state__srv__UpdateDB_Response;

// Struct for a sequence of robot_state__srv__UpdateDB_Response.
typedef struct robot_state__srv__UpdateDB_Response__Sequence
{
  robot_state__srv__UpdateDB_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_state__srv__UpdateDB_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOT_STATE__SRV__DETAIL__UPDATE_DB__STRUCT_H_
