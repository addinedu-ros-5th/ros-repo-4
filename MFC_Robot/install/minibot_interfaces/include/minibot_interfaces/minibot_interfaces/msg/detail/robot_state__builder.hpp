// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from minibot_interfaces:msg/RobotState.idl
// generated code does not contain a copyright notice

#ifndef MINIBOT_INTERFACES__MSG__DETAIL__ROBOT_STATE__BUILDER_HPP_
#define MINIBOT_INTERFACES__MSG__DETAIL__ROBOT_STATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "minibot_interfaces/msg/detail/robot_state__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace minibot_interfaces
{

namespace msg
{

namespace builder
{

class Init_RobotState_right_lamp
{
public:
  explicit Init_RobotState_right_lamp(::minibot_interfaces::msg::RobotState & msg)
  : msg_(msg)
  {}
  ::minibot_interfaces::msg::RobotState right_lamp(::minibot_interfaces::msg::RobotState::_right_lamp_type arg)
  {
    msg_.right_lamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::minibot_interfaces::msg::RobotState msg_;
};

class Init_RobotState_left_lamp
{
public:
  explicit Init_RobotState_left_lamp(::minibot_interfaces::msg::RobotState & msg)
  : msg_(msg)
  {}
  Init_RobotState_right_lamp left_lamp(::minibot_interfaces::msg::RobotState::_left_lamp_type arg)
  {
    msg_.left_lamp = std::move(arg);
    return Init_RobotState_right_lamp(msg_);
  }

private:
  ::minibot_interfaces::msg::RobotState msg_;
};

class Init_RobotState_enable_motor
{
public:
  explicit Init_RobotState_enable_motor(::minibot_interfaces::msg::RobotState & msg)
  : msg_(msg)
  {}
  Init_RobotState_left_lamp enable_motor(::minibot_interfaces::msg::RobotState::_enable_motor_type arg)
  {
    msg_.enable_motor = std::move(arg);
    return Init_RobotState_left_lamp(msg_);
  }

private:
  ::minibot_interfaces::msg::RobotState msg_;
};

class Init_RobotState_header
{
public:
  Init_RobotState_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotState_enable_motor header(::minibot_interfaces::msg::RobotState::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_RobotState_enable_motor(msg_);
  }

private:
  ::minibot_interfaces::msg::RobotState msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::minibot_interfaces::msg::RobotState>()
{
  return minibot_interfaces::msg::builder::Init_RobotState_header();
}

}  // namespace minibot_interfaces

#endif  // MINIBOT_INTERFACES__MSG__DETAIL__ROBOT_STATE__BUILDER_HPP_
