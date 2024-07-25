// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from minibot_interfaces:msg/LampCommand.idl
// generated code does not contain a copyright notice

#ifndef MINIBOT_INTERFACES__MSG__DETAIL__LAMP_COMMAND__TRAITS_HPP_
#define MINIBOT_INTERFACES__MSG__DETAIL__LAMP_COMMAND__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "minibot_interfaces/msg/detail/lamp_command__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace minibot_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const LampCommand & msg,
  std::ostream & out)
{
  out << "{";
  // member: l_command
  {
    out << "l_command: ";
    rosidl_generator_traits::value_to_yaml(msg.l_command, out);
    out << ", ";
  }

  // member: r_command
  {
    out << "r_command: ";
    rosidl_generator_traits::value_to_yaml(msg.r_command, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const LampCommand & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: l_command
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "l_command: ";
    rosidl_generator_traits::value_to_yaml(msg.l_command, out);
    out << "\n";
  }

  // member: r_command
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "r_command: ";
    rosidl_generator_traits::value_to_yaml(msg.r_command, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const LampCommand & msg, bool use_flow_style = false)
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
  const minibot_interfaces::msg::LampCommand & msg,
  std::ostream & out, size_t indentation = 0)
{
  minibot_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use minibot_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const minibot_interfaces::msg::LampCommand & msg)
{
  return minibot_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<minibot_interfaces::msg::LampCommand>()
{
  return "minibot_interfaces::msg::LampCommand";
}

template<>
inline const char * name<minibot_interfaces::msg::LampCommand>()
{
  return "minibot_interfaces/msg/LampCommand";
}

template<>
struct has_fixed_size<minibot_interfaces::msg::LampCommand>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<minibot_interfaces::msg::LampCommand>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<minibot_interfaces::msg::LampCommand>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MINIBOT_INTERFACES__MSG__DETAIL__LAMP_COMMAND__TRAITS_HPP_
