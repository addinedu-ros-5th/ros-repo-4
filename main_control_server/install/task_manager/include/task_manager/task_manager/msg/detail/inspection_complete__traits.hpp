// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from task_manager:msg/InspectionComplete.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__MSG__DETAIL__INSPECTION_COMPLETE__TRAITS_HPP_
#define TASK_MANAGER__MSG__DETAIL__INSPECTION_COMPLETE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "task_manager/msg/detail/inspection_complete__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace task_manager
{

namespace msg
{

inline void to_flow_style_yaml(
  const InspectionComplete & msg,
  std::ostream & out)
{
  out << "{";
  // member: product_code
  {
    out << "product_code: ";
    rosidl_generator_traits::value_to_yaml(msg.product_code, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const InspectionComplete & msg,
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
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const InspectionComplete & msg, bool use_flow_style = false)
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
  const task_manager::msg::InspectionComplete & msg,
  std::ostream & out, size_t indentation = 0)
{
  task_manager::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use task_manager::msg::to_yaml() instead")]]
inline std::string to_yaml(const task_manager::msg::InspectionComplete & msg)
{
  return task_manager::msg::to_yaml(msg);
}

template<>
inline const char * data_type<task_manager::msg::InspectionComplete>()
{
  return "task_manager::msg::InspectionComplete";
}

template<>
inline const char * name<task_manager::msg::InspectionComplete>()
{
  return "task_manager/msg/InspectionComplete";
}

template<>
struct has_fixed_size<task_manager::msg::InspectionComplete>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<task_manager::msg::InspectionComplete>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<task_manager::msg::InspectionComplete>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TASK_MANAGER__MSG__DETAIL__INSPECTION_COMPLETE__TRAITS_HPP_
