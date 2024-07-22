// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from task_manager:msg/StartInspection.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__MSG__DETAIL__START_INSPECTION__BUILDER_HPP_
#define TASK_MANAGER__MSG__DETAIL__START_INSPECTION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "task_manager/msg/detail/start_inspection__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace task_manager
{

namespace msg
{

namespace builder
{

class Init_StartInspection_signal
{
public:
  Init_StartInspection_signal()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::task_manager::msg::StartInspection signal(::task_manager::msg::StartInspection::_signal_type arg)
  {
    msg_.signal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::task_manager::msg::StartInspection msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::task_manager::msg::StartInspection>()
{
  return task_manager::msg::builder::Init_StartInspection_signal();
}

}  // namespace task_manager

#endif  // TASK_MANAGER__MSG__DETAIL__START_INSPECTION__BUILDER_HPP_
