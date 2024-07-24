// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from robot_state:action/RobotTask.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_STATE__ACTION__DETAIL__ROBOT_TASK__TRAITS_HPP_
#define ROBOT_STATE__ACTION__DETAIL__ROBOT_TASK__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "robot_state/action/detail/robot_task__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace robot_state
{

namespace action
{

inline void to_flow_style_yaml(
  const RobotTask_Goal & msg,
  std::ostream & out)
{
  out << "{";
  // member: pos_x
  {
    out << "pos_x: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_x, out);
    out << ", ";
  }

  // member: pos_y
  {
    out << "pos_y: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_y, out);
    out << ", ";
  }

  // member: orientation_z
  {
    out << "orientation_z: ";
    rosidl_generator_traits::value_to_yaml(msg.orientation_z, out);
    out << ", ";
  }

  // member: orientation_w
  {
    out << "orientation_w: ";
    rosidl_generator_traits::value_to_yaml(msg.orientation_w, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotTask_Goal & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: pos_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pos_x: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_x, out);
    out << "\n";
  }

  // member: pos_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pos_y: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_y, out);
    out << "\n";
  }

  // member: orientation_z
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "orientation_z: ";
    rosidl_generator_traits::value_to_yaml(msg.orientation_z, out);
    out << "\n";
  }

  // member: orientation_w
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "orientation_w: ";
    rosidl_generator_traits::value_to_yaml(msg.orientation_w, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotTask_Goal & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace robot_state

namespace rosidl_generator_traits
{

[[deprecated("use robot_state::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robot_state::action::RobotTask_Goal & msg,
  std::ostream & out, size_t indentation = 0)
{
  robot_state::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robot_state::action::to_yaml() instead")]]
inline std::string to_yaml(const robot_state::action::RobotTask_Goal & msg)
{
  return robot_state::action::to_yaml(msg);
}

template<>
inline const char * data_type<robot_state::action::RobotTask_Goal>()
{
  return "robot_state::action::RobotTask_Goal";
}

template<>
inline const char * name<robot_state::action::RobotTask_Goal>()
{
  return "robot_state/action/RobotTask_Goal";
}

template<>
struct has_fixed_size<robot_state::action::RobotTask_Goal>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<robot_state::action::RobotTask_Goal>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<robot_state::action::RobotTask_Goal>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace robot_state
{

namespace action
{

inline void to_flow_style_yaml(
  const RobotTask_Result & msg,
  std::ostream & out)
{
  out << "{";
  // member: robot_name
  {
    out << "robot_name: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_name, out);
    out << ", ";
  }

  // member: goal_location
  {
    out << "goal_location: ";
    rosidl_generator_traits::value_to_yaml(msg.goal_location, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotTask_Result & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: robot_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "robot_name: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_name, out);
    out << "\n";
  }

  // member: goal_location
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_location: ";
    rosidl_generator_traits::value_to_yaml(msg.goal_location, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotTask_Result & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace robot_state

namespace rosidl_generator_traits
{

[[deprecated("use robot_state::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robot_state::action::RobotTask_Result & msg,
  std::ostream & out, size_t indentation = 0)
{
  robot_state::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robot_state::action::to_yaml() instead")]]
inline std::string to_yaml(const robot_state::action::RobotTask_Result & msg)
{
  return robot_state::action::to_yaml(msg);
}

template<>
inline const char * data_type<robot_state::action::RobotTask_Result>()
{
  return "robot_state::action::RobotTask_Result";
}

template<>
inline const char * name<robot_state::action::RobotTask_Result>()
{
  return "robot_state/action/RobotTask_Result";
}

template<>
struct has_fixed_size<robot_state::action::RobotTask_Result>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<robot_state::action::RobotTask_Result>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<robot_state::action::RobotTask_Result>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace robot_state
{

namespace action
{

inline void to_flow_style_yaml(
  const RobotTask_Feedback & msg,
  std::ostream & out)
{
  out << "{";
  // member: remained_dist
  {
    out << "remained_dist: ";
    rosidl_generator_traits::value_to_yaml(msg.remained_dist, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotTask_Feedback & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: remained_dist
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "remained_dist: ";
    rosidl_generator_traits::value_to_yaml(msg.remained_dist, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotTask_Feedback & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace robot_state

namespace rosidl_generator_traits
{

[[deprecated("use robot_state::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robot_state::action::RobotTask_Feedback & msg,
  std::ostream & out, size_t indentation = 0)
{
  robot_state::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robot_state::action::to_yaml() instead")]]
inline std::string to_yaml(const robot_state::action::RobotTask_Feedback & msg)
{
  return robot_state::action::to_yaml(msg);
}

template<>
inline const char * data_type<robot_state::action::RobotTask_Feedback>()
{
  return "robot_state::action::RobotTask_Feedback";
}

template<>
inline const char * name<robot_state::action::RobotTask_Feedback>()
{
  return "robot_state/action/RobotTask_Feedback";
}

template<>
struct has_fixed_size<robot_state::action::RobotTask_Feedback>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<robot_state::action::RobotTask_Feedback>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<robot_state::action::RobotTask_Feedback>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'goal'
#include "robot_state/action/detail/robot_task__traits.hpp"

namespace robot_state
{

namespace action
{

inline void to_flow_style_yaml(
  const RobotTask_SendGoal_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal_id
  {
    out << "goal_id: ";
    to_flow_style_yaml(msg.goal_id, out);
    out << ", ";
  }

  // member: goal
  {
    out << "goal: ";
    to_flow_style_yaml(msg.goal, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotTask_SendGoal_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_block_style_yaml(msg.goal_id, out, indentation + 2);
  }

  // member: goal
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal:\n";
    to_block_style_yaml(msg.goal, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotTask_SendGoal_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace robot_state

namespace rosidl_generator_traits
{

[[deprecated("use robot_state::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robot_state::action::RobotTask_SendGoal_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  robot_state::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robot_state::action::to_yaml() instead")]]
inline std::string to_yaml(const robot_state::action::RobotTask_SendGoal_Request & msg)
{
  return robot_state::action::to_yaml(msg);
}

template<>
inline const char * data_type<robot_state::action::RobotTask_SendGoal_Request>()
{
  return "robot_state::action::RobotTask_SendGoal_Request";
}

template<>
inline const char * name<robot_state::action::RobotTask_SendGoal_Request>()
{
  return "robot_state/action/RobotTask_SendGoal_Request";
}

template<>
struct has_fixed_size<robot_state::action::RobotTask_SendGoal_Request>
  : std::integral_constant<bool, has_fixed_size<robot_state::action::RobotTask_Goal>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<robot_state::action::RobotTask_SendGoal_Request>
  : std::integral_constant<bool, has_bounded_size<robot_state::action::RobotTask_Goal>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<robot_state::action::RobotTask_SendGoal_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace robot_state
{

namespace action
{

inline void to_flow_style_yaml(
  const RobotTask_SendGoal_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: accepted
  {
    out << "accepted: ";
    rosidl_generator_traits::value_to_yaml(msg.accepted, out);
    out << ", ";
  }

  // member: stamp
  {
    out << "stamp: ";
    to_flow_style_yaml(msg.stamp, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotTask_SendGoal_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: accepted
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "accepted: ";
    rosidl_generator_traits::value_to_yaml(msg.accepted, out);
    out << "\n";
  }

  // member: stamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "stamp:\n";
    to_block_style_yaml(msg.stamp, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotTask_SendGoal_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace robot_state

namespace rosidl_generator_traits
{

[[deprecated("use robot_state::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robot_state::action::RobotTask_SendGoal_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  robot_state::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robot_state::action::to_yaml() instead")]]
inline std::string to_yaml(const robot_state::action::RobotTask_SendGoal_Response & msg)
{
  return robot_state::action::to_yaml(msg);
}

template<>
inline const char * data_type<robot_state::action::RobotTask_SendGoal_Response>()
{
  return "robot_state::action::RobotTask_SendGoal_Response";
}

template<>
inline const char * name<robot_state::action::RobotTask_SendGoal_Response>()
{
  return "robot_state/action/RobotTask_SendGoal_Response";
}

template<>
struct has_fixed_size<robot_state::action::RobotTask_SendGoal_Response>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct has_bounded_size<robot_state::action::RobotTask_SendGoal_Response>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct is_message<robot_state::action::RobotTask_SendGoal_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<robot_state::action::RobotTask_SendGoal>()
{
  return "robot_state::action::RobotTask_SendGoal";
}

template<>
inline const char * name<robot_state::action::RobotTask_SendGoal>()
{
  return "robot_state/action/RobotTask_SendGoal";
}

template<>
struct has_fixed_size<robot_state::action::RobotTask_SendGoal>
  : std::integral_constant<
    bool,
    has_fixed_size<robot_state::action::RobotTask_SendGoal_Request>::value &&
    has_fixed_size<robot_state::action::RobotTask_SendGoal_Response>::value
  >
{
};

template<>
struct has_bounded_size<robot_state::action::RobotTask_SendGoal>
  : std::integral_constant<
    bool,
    has_bounded_size<robot_state::action::RobotTask_SendGoal_Request>::value &&
    has_bounded_size<robot_state::action::RobotTask_SendGoal_Response>::value
  >
{
};

template<>
struct is_service<robot_state::action::RobotTask_SendGoal>
  : std::true_type
{
};

template<>
struct is_service_request<robot_state::action::RobotTask_SendGoal_Request>
  : std::true_type
{
};

template<>
struct is_service_response<robot_state::action::RobotTask_SendGoal_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"

namespace robot_state
{

namespace action
{

inline void to_flow_style_yaml(
  const RobotTask_GetResult_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal_id
  {
    out << "goal_id: ";
    to_flow_style_yaml(msg.goal_id, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotTask_GetResult_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_block_style_yaml(msg.goal_id, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotTask_GetResult_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace robot_state

namespace rosidl_generator_traits
{

[[deprecated("use robot_state::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robot_state::action::RobotTask_GetResult_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  robot_state::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robot_state::action::to_yaml() instead")]]
inline std::string to_yaml(const robot_state::action::RobotTask_GetResult_Request & msg)
{
  return robot_state::action::to_yaml(msg);
}

template<>
inline const char * data_type<robot_state::action::RobotTask_GetResult_Request>()
{
  return "robot_state::action::RobotTask_GetResult_Request";
}

template<>
inline const char * name<robot_state::action::RobotTask_GetResult_Request>()
{
  return "robot_state/action/RobotTask_GetResult_Request";
}

template<>
struct has_fixed_size<robot_state::action::RobotTask_GetResult_Request>
  : std::integral_constant<bool, has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<robot_state::action::RobotTask_GetResult_Request>
  : std::integral_constant<bool, has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<robot_state::action::RobotTask_GetResult_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'result'
// already included above
// #include "robot_state/action/detail/robot_task__traits.hpp"

namespace robot_state
{

namespace action
{

inline void to_flow_style_yaml(
  const RobotTask_GetResult_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: status
  {
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << ", ";
  }

  // member: result
  {
    out << "result: ";
    to_flow_style_yaml(msg.result, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotTask_GetResult_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << "\n";
  }

  // member: result
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "result:\n";
    to_block_style_yaml(msg.result, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotTask_GetResult_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace robot_state

namespace rosidl_generator_traits
{

[[deprecated("use robot_state::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robot_state::action::RobotTask_GetResult_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  robot_state::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robot_state::action::to_yaml() instead")]]
inline std::string to_yaml(const robot_state::action::RobotTask_GetResult_Response & msg)
{
  return robot_state::action::to_yaml(msg);
}

template<>
inline const char * data_type<robot_state::action::RobotTask_GetResult_Response>()
{
  return "robot_state::action::RobotTask_GetResult_Response";
}

template<>
inline const char * name<robot_state::action::RobotTask_GetResult_Response>()
{
  return "robot_state/action/RobotTask_GetResult_Response";
}

template<>
struct has_fixed_size<robot_state::action::RobotTask_GetResult_Response>
  : std::integral_constant<bool, has_fixed_size<robot_state::action::RobotTask_Result>::value> {};

template<>
struct has_bounded_size<robot_state::action::RobotTask_GetResult_Response>
  : std::integral_constant<bool, has_bounded_size<robot_state::action::RobotTask_Result>::value> {};

template<>
struct is_message<robot_state::action::RobotTask_GetResult_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<robot_state::action::RobotTask_GetResult>()
{
  return "robot_state::action::RobotTask_GetResult";
}

template<>
inline const char * name<robot_state::action::RobotTask_GetResult>()
{
  return "robot_state/action/RobotTask_GetResult";
}

template<>
struct has_fixed_size<robot_state::action::RobotTask_GetResult>
  : std::integral_constant<
    bool,
    has_fixed_size<robot_state::action::RobotTask_GetResult_Request>::value &&
    has_fixed_size<robot_state::action::RobotTask_GetResult_Response>::value
  >
{
};

template<>
struct has_bounded_size<robot_state::action::RobotTask_GetResult>
  : std::integral_constant<
    bool,
    has_bounded_size<robot_state::action::RobotTask_GetResult_Request>::value &&
    has_bounded_size<robot_state::action::RobotTask_GetResult_Response>::value
  >
{
};

template<>
struct is_service<robot_state::action::RobotTask_GetResult>
  : std::true_type
{
};

template<>
struct is_service_request<robot_state::action::RobotTask_GetResult_Request>
  : std::true_type
{
};

template<>
struct is_service_response<robot_state::action::RobotTask_GetResult_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'feedback'
// already included above
// #include "robot_state/action/detail/robot_task__traits.hpp"

namespace robot_state
{

namespace action
{

inline void to_flow_style_yaml(
  const RobotTask_FeedbackMessage & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal_id
  {
    out << "goal_id: ";
    to_flow_style_yaml(msg.goal_id, out);
    out << ", ";
  }

  // member: feedback
  {
    out << "feedback: ";
    to_flow_style_yaml(msg.feedback, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotTask_FeedbackMessage & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_block_style_yaml(msg.goal_id, out, indentation + 2);
  }

  // member: feedback
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "feedback:\n";
    to_block_style_yaml(msg.feedback, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotTask_FeedbackMessage & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace robot_state

namespace rosidl_generator_traits
{

[[deprecated("use robot_state::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robot_state::action::RobotTask_FeedbackMessage & msg,
  std::ostream & out, size_t indentation = 0)
{
  robot_state::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robot_state::action::to_yaml() instead")]]
inline std::string to_yaml(const robot_state::action::RobotTask_FeedbackMessage & msg)
{
  return robot_state::action::to_yaml(msg);
}

template<>
inline const char * data_type<robot_state::action::RobotTask_FeedbackMessage>()
{
  return "robot_state::action::RobotTask_FeedbackMessage";
}

template<>
inline const char * name<robot_state::action::RobotTask_FeedbackMessage>()
{
  return "robot_state/action/RobotTask_FeedbackMessage";
}

template<>
struct has_fixed_size<robot_state::action::RobotTask_FeedbackMessage>
  : std::integral_constant<bool, has_fixed_size<robot_state::action::RobotTask_Feedback>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<robot_state::action::RobotTask_FeedbackMessage>
  : std::integral_constant<bool, has_bounded_size<robot_state::action::RobotTask_Feedback>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<robot_state::action::RobotTask_FeedbackMessage>
  : std::true_type {};

}  // namespace rosidl_generator_traits


namespace rosidl_generator_traits
{

template<>
struct is_action<robot_state::action::RobotTask>
  : std::true_type
{
};

template<>
struct is_action_goal<robot_state::action::RobotTask_Goal>
  : std::true_type
{
};

template<>
struct is_action_result<robot_state::action::RobotTask_Result>
  : std::true_type
{
};

template<>
struct is_action_feedback<robot_state::action::RobotTask_Feedback>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits


#endif  // ROBOT_STATE__ACTION__DETAIL__ROBOT_TASK__TRAITS_HPP_
