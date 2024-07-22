// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from task_manager:msg/StartInspection.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__MSG__DETAIL__START_INSPECTION__TRAITS_HPP_
#define TASK_MANAGER__MSG__DETAIL__START_INSPECTION__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "task_manager/msg/detail/start_inspection__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace task_manager
{

namespace msg
{

inline void to_flow_style_yaml(
  const StartInspection & msg,
  std::ostream & out)
{
  out << "{";
  // member: signal
  {
    out << "signal: ";
    rosidl_generator_traits::value_to_yaml(msg.signal, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const StartInspection & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: signal
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "signal: ";
    rosidl_generator_traits::value_to_yaml(msg.signal, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const StartInspection & msg, bool use_flow_style = false)
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
  const task_manager::msg::StartInspection & msg,
  std::ostream & out, size_t indentation = 0)
{
  task_manager::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use task_manager::msg::to_yaml() instead")]]
inline std::string to_yaml(const task_manager::msg::StartInspection & msg)
{
  return task_manager::msg::to_yaml(msg);
}

template<>
inline const char * data_type<task_manager::msg::StartInspection>()
{
  return "task_manager::msg::StartInspection";
}

template<>
inline const char * name<task_manager::msg::StartInspection>()
{
  return "task_manager/msg/StartInspection";
}

template<>
struct has_fixed_size<task_manager::msg::StartInspection>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<task_manager::msg::StartInspection>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<task_manager::msg::StartInspection>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TASK_MANAGER__MSG__DETAIL__START_INSPECTION__TRAITS_HPP_
