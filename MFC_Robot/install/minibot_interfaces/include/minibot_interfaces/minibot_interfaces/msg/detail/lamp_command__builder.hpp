// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from minibot_interfaces:msg/LampCommand.idl
// generated code does not contain a copyright notice

#ifndef MINIBOT_INTERFACES__MSG__DETAIL__LAMP_COMMAND__BUILDER_HPP_
#define MINIBOT_INTERFACES__MSG__DETAIL__LAMP_COMMAND__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "minibot_interfaces/msg/detail/lamp_command__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace minibot_interfaces
{

namespace msg
{

namespace builder
{

class Init_LampCommand_r_command
{
public:
  explicit Init_LampCommand_r_command(::minibot_interfaces::msg::LampCommand & msg)
  : msg_(msg)
  {}
  ::minibot_interfaces::msg::LampCommand r_command(::minibot_interfaces::msg::LampCommand::_r_command_type arg)
  {
    msg_.r_command = std::move(arg);
    return std::move(msg_);
  }

private:
  ::minibot_interfaces::msg::LampCommand msg_;
};

class Init_LampCommand_l_command
{
public:
  Init_LampCommand_l_command()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LampCommand_r_command l_command(::minibot_interfaces::msg::LampCommand::_l_command_type arg)
  {
    msg_.l_command = std::move(arg);
    return Init_LampCommand_r_command(msg_);
  }

private:
  ::minibot_interfaces::msg::LampCommand msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::minibot_interfaces::msg::LampCommand>()
{
  return minibot_interfaces::msg::builder::Init_LampCommand_l_command();
}

}  // namespace minibot_interfaces

#endif  // MINIBOT_INTERFACES__MSG__DETAIL__LAMP_COMMAND__BUILDER_HPP_
