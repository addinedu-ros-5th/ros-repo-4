// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robot_state:action/RobotTask.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_STATE__ACTION__DETAIL__ROBOT_TASK__STRUCT_H_
#define ROBOT_STATE__ACTION__DETAIL__ROBOT_TASK__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in action/RobotTask in the package robot_state.
typedef struct robot_state__action__RobotTask_Goal
{
  float pos_x;
  float pos_y;
  float orientation_z;
  float orientation_w;
} robot_state__action__RobotTask_Goal;

// Struct for a sequence of robot_state__action__RobotTask_Goal.
typedef struct robot_state__action__RobotTask_Goal__Sequence
{
  robot_state__action__RobotTask_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_state__action__RobotTask_Goal__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'robot_name'
// Member 'goal_location'
#include "rosidl_runtime_c/string.h"

/// Struct defined in action/RobotTask in the package robot_state.
typedef struct robot_state__action__RobotTask_Result
{
  rosidl_runtime_c__String robot_name;
  rosidl_runtime_c__String goal_location;
} robot_state__action__RobotTask_Result;

// Struct for a sequence of robot_state__action__RobotTask_Result.
typedef struct robot_state__action__RobotTask_Result__Sequence
{
  robot_state__action__RobotTask_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_state__action__RobotTask_Result__Sequence;


// Constants defined in the message

/// Struct defined in action/RobotTask in the package robot_state.
typedef struct robot_state__action__RobotTask_Feedback
{
  float remained_dist;
} robot_state__action__RobotTask_Feedback;

// Struct for a sequence of robot_state__action__RobotTask_Feedback.
typedef struct robot_state__action__RobotTask_Feedback__Sequence
{
  robot_state__action__RobotTask_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_state__action__RobotTask_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "robot_state/action/detail/robot_task__struct.h"

/// Struct defined in action/RobotTask in the package robot_state.
typedef struct robot_state__action__RobotTask_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  robot_state__action__RobotTask_Goal goal;
} robot_state__action__RobotTask_SendGoal_Request;

// Struct for a sequence of robot_state__action__RobotTask_SendGoal_Request.
typedef struct robot_state__action__RobotTask_SendGoal_Request__Sequence
{
  robot_state__action__RobotTask_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_state__action__RobotTask_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/RobotTask in the package robot_state.
typedef struct robot_state__action__RobotTask_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} robot_state__action__RobotTask_SendGoal_Response;

// Struct for a sequence of robot_state__action__RobotTask_SendGoal_Response.
typedef struct robot_state__action__RobotTask_SendGoal_Response__Sequence
{
  robot_state__action__RobotTask_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_state__action__RobotTask_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/RobotTask in the package robot_state.
typedef struct robot_state__action__RobotTask_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} robot_state__action__RobotTask_GetResult_Request;

// Struct for a sequence of robot_state__action__RobotTask_GetResult_Request.
typedef struct robot_state__action__RobotTask_GetResult_Request__Sequence
{
  robot_state__action__RobotTask_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_state__action__RobotTask_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "robot_state/action/detail/robot_task__struct.h"

/// Struct defined in action/RobotTask in the package robot_state.
typedef struct robot_state__action__RobotTask_GetResult_Response
{
  int8_t status;
  robot_state__action__RobotTask_Result result;
} robot_state__action__RobotTask_GetResult_Response;

// Struct for a sequence of robot_state__action__RobotTask_GetResult_Response.
typedef struct robot_state__action__RobotTask_GetResult_Response__Sequence
{
  robot_state__action__RobotTask_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_state__action__RobotTask_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "robot_state/action/detail/robot_task__struct.h"

/// Struct defined in action/RobotTask in the package robot_state.
typedef struct robot_state__action__RobotTask_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  robot_state__action__RobotTask_Feedback feedback;
} robot_state__action__RobotTask_FeedbackMessage;

// Struct for a sequence of robot_state__action__RobotTask_FeedbackMessage.
typedef struct robot_state__action__RobotTask_FeedbackMessage__Sequence
{
  robot_state__action__RobotTask_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_state__action__RobotTask_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOT_STATE__ACTION__DETAIL__ROBOT_TASK__STRUCT_H_
