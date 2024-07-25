// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from task_manager:msg/DbUpdate.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__MSG__DETAIL__DB_UPDATE__BUILDER_HPP_
#define TASK_MANAGER__MSG__DETAIL__DB_UPDATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "task_manager/msg/detail/db_update__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace task_manager
{

namespace msg
{

namespace builder
{

class Init_DbUpdate_status
{
public:
  Init_DbUpdate_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::task_manager::msg::DbUpdate status(::task_manager::msg::DbUpdate::_status_type arg)
  {
    msg_.status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::task_manager::msg::DbUpdate msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::task_manager::msg::DbUpdate>()
{
  return task_manager::msg::builder::Init_DbUpdate_status();
}

}  // namespace task_manager

#endif  // TASK_MANAGER__MSG__DETAIL__DB_UPDATE__BUILDER_HPP_
