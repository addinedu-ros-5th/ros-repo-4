// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from task_manager:srv/AllocatorTask.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__SRV__DETAIL__ALLOCATOR_TASK__BUILDER_HPP_
#define TASK_MANAGER__SRV__DETAIL__ALLOCATOR_TASK__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "task_manager/srv/detail/allocator_task__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace task_manager
{

namespace srv
{

namespace builder
{

class Init_AllocatorTask_Request_task_type
{
public:
  explicit Init_AllocatorTask_Request_task_type(::task_manager::srv::AllocatorTask_Request & msg)
  : msg_(msg)
  {}
  ::task_manager::srv::AllocatorTask_Request task_type(::task_manager::srv::AllocatorTask_Request::_task_type_type arg)
  {
    msg_.task_type = std::move(arg);
    return std::move(msg_);
  }

private:
  ::task_manager::srv::AllocatorTask_Request msg_;
};

class Init_AllocatorTask_Request_product_code
{
public:
  Init_AllocatorTask_Request_product_code()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AllocatorTask_Request_task_type product_code(::task_manager::srv::AllocatorTask_Request::_product_code_type arg)
  {
    msg_.product_code = std::move(arg);
    return Init_AllocatorTask_Request_task_type(msg_);
  }

private:
  ::task_manager::srv::AllocatorTask_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::task_manager::srv::AllocatorTask_Request>()
{
  return task_manager::srv::builder::Init_AllocatorTask_Request_product_code();
}

}  // namespace task_manager


namespace task_manager
{

namespace srv
{

namespace builder
{

class Init_AllocatorTask_Response_task_assignment
{
public:
  explicit Init_AllocatorTask_Response_task_assignment(::task_manager::srv::AllocatorTask_Response & msg)
  : msg_(msg)
  {}
  ::task_manager::srv::AllocatorTask_Response task_assignment(::task_manager::srv::AllocatorTask_Response::_task_assignment_type arg)
  {
    msg_.task_assignment = std::move(arg);
    return std::move(msg_);
  }

private:
  ::task_manager::srv::AllocatorTask_Response msg_;
};

class Init_AllocatorTask_Response_goal_location
{
public:
  explicit Init_AllocatorTask_Response_goal_location(::task_manager::srv::AllocatorTask_Response & msg)
  : msg_(msg)
  {}
  Init_AllocatorTask_Response_task_assignment goal_location(::task_manager::srv::AllocatorTask_Response::_goal_location_type arg)
  {
    msg_.goal_location = std::move(arg);
    return Init_AllocatorTask_Response_task_assignment(msg_);
  }

private:
  ::task_manager::srv::AllocatorTask_Response msg_;
};

class Init_AllocatorTask_Response_robot_name
{
public:
  Init_AllocatorTask_Response_robot_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AllocatorTask_Response_goal_location robot_name(::task_manager::srv::AllocatorTask_Response::_robot_name_type arg)
  {
    msg_.robot_name = std::move(arg);
    return Init_AllocatorTask_Response_goal_location(msg_);
  }

private:
  ::task_manager::srv::AllocatorTask_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::task_manager::srv::AllocatorTask_Response>()
{
  return task_manager::srv::builder::Init_AllocatorTask_Response_robot_name();
}

}  // namespace task_manager

#endif  // TASK_MANAGER__SRV__DETAIL__ALLOCATOR_TASK__BUILDER_HPP_
