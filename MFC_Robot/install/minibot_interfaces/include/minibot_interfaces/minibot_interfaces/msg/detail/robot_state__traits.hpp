// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from minibot_interfaces:msg/RobotState.idl
// generated code does not contain a copyright notice

#ifndef MINIBOT_INTERFACES__MSG__DETAIL__ROBOT_STATE__TRAITS_HPP_
#define MINIBOT_INTERFACES__MSG__DETAIL__ROBOT_STATE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "minibot_interfaces/msg/detail/robot_state__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace minibot_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const RobotState & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: enable_motor
  {
    out << "enable_motor: ";
    rosidl_generator_traits::value_to_yaml(msg.enable_motor, out);
    out << ", ";
  }

  // member: left_lamp
  {
    out << "left_lamp: ";
    rosidl_generator_traits::value_to_yaml(msg.left_lamp, out);
    out << ", ";
  }

  // member: right_lamp
  {
    out << "right_lamp: ";
    rosidl_generator_traits::value_to_yaml(msg.right_lamp, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotState & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: enable_motor
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "enable_motor: ";
    rosidl_generator_traits::value_to_yaml(msg.enable_motor, out);
    out << "\n";
  }

  // member: left_lamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "left_lamp: ";
    rosidl_generator_traits::value_to_yaml(msg.left_lamp, out);
    out << "\n";
  }

  // member: right_lamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "right_lamp: ";
    rosidl_generator_traits::value_to_yaml(msg.right_lamp, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotState & msg, bool use_flow_style = false)
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

}  // namespace minibot_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use minibot_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const minibot_interfaces::msg::RobotState & msg,
  std::ostream & out, size_t indentation = 0)
{
  minibot_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use minibot_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const minibot_interfaces::msg::RobotState & msg)
{
  return minibot_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<minibot_interfaces::msg::RobotState>()
{
  return "minibot_interfaces::msg::RobotState";
}

template<>
inline const char * name<minibot_interfaces::msg::RobotState>()
{
  return "minibot_interfaces/msg/RobotState";
}

template<>
struct has_fixed_size<minibot_interfaces::msg::RobotState>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<minibot_interfaces::msg::RobotState>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<minibot_interfaces::msg::RobotState>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MINIBOT_INTERFACES__MSG__DETAIL__ROBOT_STATE__TRAITS_HPP_
