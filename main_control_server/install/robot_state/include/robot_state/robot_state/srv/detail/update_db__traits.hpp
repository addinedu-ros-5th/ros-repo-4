// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from robot_state:srv/UpdateDB.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_STATE__SRV__DETAIL__UPDATE_DB__TRAITS_HPP_
#define ROBOT_STATE__SRV__DETAIL__UPDATE_DB__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "robot_state/srv/detail/update_db__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace robot_state
{

namespace srv
{

inline void to_flow_style_yaml(
  const UpdateDB_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: robot_name
  {
    out << "robot_name: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_name, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const UpdateDB_Request & msg,
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
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const UpdateDB_Request & msg, bool use_flow_style = false)
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

}  // namespace robot_state

namespace rosidl_generator_traits
{

[[deprecated("use robot_state::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robot_state::srv::UpdateDB_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  robot_state::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robot_state::srv::to_yaml() instead")]]
inline std::string to_yaml(const robot_state::srv::UpdateDB_Request & msg)
{
  return robot_state::srv::to_yaml(msg);
}

template<>
inline const char * data_type<robot_state::srv::UpdateDB_Request>()
{
  return "robot_state::srv::UpdateDB_Request";
}

template<>
inline const char * name<robot_state::srv::UpdateDB_Request>()
{
  return "robot_state/srv/UpdateDB_Request";
}

template<>
struct has_fixed_size<robot_state::srv::UpdateDB_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<robot_state::srv::UpdateDB_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<robot_state::srv::UpdateDB_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace robot_state
{

namespace srv
{

inline void to_flow_style_yaml(
  const UpdateDB_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: robot_name
  {
    out << "robot_name: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_name, out);
    out << ", ";
  }

  // member: battery_status
  {
    out << "battery_status: ";
    rosidl_generator_traits::value_to_yaml(msg.battery_status, out);
    out << ", ";
  }

  // member: status
  {
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const UpdateDB_Response & msg,
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

  // member: battery_status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "battery_status: ";
    rosidl_generator_traits::value_to_yaml(msg.battery_status, out);
    out << "\n";
  }

  // member: status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const UpdateDB_Response & msg, bool use_flow_style = false)
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

}  // namespace robot_state

namespace rosidl_generator_traits
{

[[deprecated("use robot_state::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robot_state::srv::UpdateDB_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  robot_state::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robot_state::srv::to_yaml() instead")]]
inline std::string to_yaml(const robot_state::srv::UpdateDB_Response & msg)
{
  return robot_state::srv::to_yaml(msg);
}

template<>
inline const char * data_type<robot_state::srv::UpdateDB_Response>()
{
  return "robot_state::srv::UpdateDB_Response";
}

template<>
inline const char * name<robot_state::srv::UpdateDB_Response>()
{
  return "robot_state/srv/UpdateDB_Response";
}

template<>
struct has_fixed_size<robot_state::srv::UpdateDB_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<robot_state::srv::UpdateDB_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<robot_state::srv::UpdateDB_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<robot_state::srv::UpdateDB>()
{
  return "robot_state::srv::UpdateDB";
}

template<>
inline const char * name<robot_state::srv::UpdateDB>()
{
  return "robot_state/srv/UpdateDB";
}

template<>
struct has_fixed_size<robot_state::srv::UpdateDB>
  : std::integral_constant<
    bool,
    has_fixed_size<robot_state::srv::UpdateDB_Request>::value &&
    has_fixed_size<robot_state::srv::UpdateDB_Response>::value
  >
{
};

template<>
struct has_bounded_size<robot_state::srv::UpdateDB>
  : std::integral_constant<
    bool,
    has_bounded_size<robot_state::srv::UpdateDB_Request>::value &&
    has_bounded_size<robot_state::srv::UpdateDB_Response>::value
  >
{
};

template<>
struct is_service<robot_state::srv::UpdateDB>
  : std::true_type
{
};

template<>
struct is_service_request<robot_state::srv::UpdateDB_Request>
  : std::true_type
{
};

template<>
struct is_service_response<robot_state::srv::UpdateDB_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // ROBOT_STATE__SRV__DETAIL__UPDATE_DB__TRAITS_HPP_
