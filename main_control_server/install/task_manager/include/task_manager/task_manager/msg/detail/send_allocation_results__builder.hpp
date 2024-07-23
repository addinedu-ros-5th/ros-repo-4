// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from task_manager:msg/SendAllocationResults.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__MSG__DETAIL__SEND_ALLOCATION_RESULTS__BUILDER_HPP_
#define TASK_MANAGER__MSG__DETAIL__SEND_ALLOCATION_RESULTS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "task_manager/msg/detail/send_allocation_results__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace task_manager
{

namespace msg
{

namespace builder
{

class Init_SendAllocationResults_task_assignment
{
public:
  explicit Init_SendAllocationResults_task_assignment(::task_manager::msg::SendAllocationResults & msg)
  : msg_(msg)
  {}
  ::task_manager::msg::SendAllocationResults task_assignment(::task_manager::msg::SendAllocationResults::_task_assignment_type arg)
  {
    msg_.task_assignment = std::move(arg);
    return std::move(msg_);
  }

private:
  ::task_manager::msg::SendAllocationResults msg_;
};

class Init_SendAllocationResults_goal_location
{
public:
  explicit Init_SendAllocationResults_goal_location(::task_manager::msg::SendAllocationResults & msg)
  : msg_(msg)
  {}
  Init_SendAllocationResults_task_assignment goal_location(::task_manager::msg::SendAllocationResults::_goal_location_type arg)
  {
    msg_.goal_location = std::move(arg);
    return Init_SendAllocationResults_task_assignment(msg_);
  }

private:
  ::task_manager::msg::SendAllocationResults msg_;
};

class Init_SendAllocationResults_robot_name
{
public:
  Init_SendAllocationResults_robot_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SendAllocationResults_goal_location robot_name(::task_manager::msg::SendAllocationResults::_robot_name_type arg)
  {
    msg_.robot_name = std::move(arg);
    return Init_SendAllocationResults_goal_location(msg_);
  }

private:
  ::task_manager::msg::SendAllocationResults msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::task_manager::msg::SendAllocationResults>()
{
  return task_manager::msg::builder::Init_SendAllocationResults_robot_name();
}

}  // namespace task_manager

#endif  // TASK_MANAGER__MSG__DETAIL__SEND_ALLOCATION_RESULTS__BUILDER_HPP_
