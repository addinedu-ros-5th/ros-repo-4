// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from task_manager:srv/AllocatorTask.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__SRV__DETAIL__ALLOCATOR_TASK__TRAITS_HPP_
#define TASK_MANAGER__SRV__DETAIL__ALLOCATOR_TASK__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "task_manager/srv/detail/allocator_task__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace task_manager
{

namespace srv
{

inline void to_flow_style_yaml(
  const AllocatorTask_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: product_code
  {
    out << "product_code: ";
    rosidl_generator_traits::value_to_yaml(msg.product_code, out);
    out << ", ";
  }

  // member: task_type
  {
    out << "task_type: ";
    rosidl_generator_traits::value_to_yaml(msg.task_type, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AllocatorTask_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: product_code
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "product_code: ";
    rosidl_generator_traits::value_to_yaml(msg.product_code, out);
    out << "\n";
  }

  // member: task_type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "task_type: ";
    rosidl_generator_traits::value_to_yaml(msg.task_type, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AllocatorTask_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace task_manager

namespace rosidl_generator_traits
{

[[deprecated("use task_manager::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const task_manager::srv::AllocatorTask_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  task_manager::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use task_manager::srv::to_yaml() instead")]]
inline std::string to_yaml(const task_manager::srv::AllocatorTask_Request & msg)
{
  return task_manager::srv::to_yaml(msg);
}

template<>
inline const char * data_type<task_manager::srv::AllocatorTask_Request>()
{
  return "task_manager::srv::AllocatorTask_Request";
}

template<>
inline const char * name<task_manager::srv::AllocatorTask_Request>()
{
  return "task_manager/srv/AllocatorTask_Request";
}

template<>
struct has_fixed_size<task_manager::srv::AllocatorTask_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<task_manager::srv::AllocatorTask_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<task_manager::srv::AllocatorTask_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace task_manager
{

namespace srv
{

inline void to_flow_style_yaml(
  const AllocatorTask_Response & msg,
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
    out << ", ";
  }

  // member: task_assignment
  {
    out << "task_assignment: ";
    rosidl_generator_traits::value_to_yaml(msg.task_assignment, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AllocatorTask_Response & msg,
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

  // member: task_assignment
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "task_assignment: ";
    rosidl_generator_traits::value_to_yaml(msg.task_assignment, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AllocatorTask_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace task_manager

namespace rosidl_generator_traits
{

[[deprecated("use task_manager::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const task_manager::srv::AllocatorTask_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  task_manager::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use task_manager::srv::to_yaml() instead")]]
inline std::string to_yaml(const task_manager::srv::AllocatorTask_Response & msg)
{
  return task_manager::srv::to_yaml(msg);
}

template<>
inline const char * data_type<task_manager::srv::AllocatorTask_Response>()
{
  return "task_manager::srv::AllocatorTask_Response";
}

template<>
inline const char * name<task_manager::srv::AllocatorTask_Response>()
{
  return "task_manager/srv/AllocatorTask_Response";
}

template<>
struct has_fixed_size<task_manager::srv::AllocatorTask_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<task_manager::srv::AllocatorTask_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<task_manager::srv::AllocatorTask_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<task_manager::srv::AllocatorTask>()
{
  return "task_manager::srv::AllocatorTask";
}

template<>
inline const char * name<task_manager::srv::AllocatorTask>()
{
  return "task_manager/srv/AllocatorTask";
}

template<>
struct has_fixed_size<task_manager::srv::AllocatorTask>
  : std::integral_constant<
    bool,
    has_fixed_size<task_manager::srv::AllocatorTask_Request>::value &&
    has_fixed_size<task_manager::srv::AllocatorTask_Response>::value
  >
{
};

template<>
struct has_bounded_size<task_manager::srv::AllocatorTask>
  : std::integral_constant<
    bool,
    has_bounded_size<task_manager::srv::AllocatorTask_Request>::value &&
    has_bounded_size<task_manager::srv::AllocatorTask_Response>::value
  >
{
};

template<>
struct is_service<task_manager::srv::AllocatorTask>
  : std::true_type
{
};

template<>
struct is_service_request<task_manager::srv::AllocatorTask_Request>
  : std::true_type
{
};

template<>
struct is_service_response<task_manager::srv::AllocatorTask_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // TASK_MANAGER__SRV__DETAIL__ALLOCATOR_TASK__TRAITS_HPP_
