// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from task_manager:msg/SendAllocationResults.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__MSG__DETAIL__SEND_ALLOCATION_RESULTS__TRAITS_HPP_
#define TASK_MANAGER__MSG__DETAIL__SEND_ALLOCATION_RESULTS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "task_manager/msg/detail/send_allocation_results__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace task_manager
{

namespace msg
{

inline void to_flow_style_yaml(
  const SendAllocationResults & msg,
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
  const SendAllocationResults & msg,
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

inline std::string to_yaml(const SendAllocationResults & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace task_manager

namespace rosidl_generator_traits
{

[[deprecated("use task_manager::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const task_manager::msg::SendAllocationResults & msg,
  std::ostream & out, size_t indentation = 0)
{
  task_manager::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use task_manager::msg::to_yaml() instead")]]
inline std::string to_yaml(const task_manager::msg::SendAllocationResults & msg)
{
  return task_manager::msg::to_yaml(msg);
}

template<>
inline const char * data_type<task_manager::msg::SendAllocationResults>()
{
  return "task_manager::msg::SendAllocationResults";
}

template<>
inline const char * name<task_manager::msg::SendAllocationResults>()
{
  return "task_manager/msg/SendAllocationResults";
}

template<>
struct has_fixed_size<task_manager::msg::SendAllocationResults>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<task_manager::msg::SendAllocationResults>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<task_manager::msg::SendAllocationResults>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TASK_MANAGER__MSG__DETAIL__SEND_ALLOCATION_RESULTS__TRAITS_HPP_
