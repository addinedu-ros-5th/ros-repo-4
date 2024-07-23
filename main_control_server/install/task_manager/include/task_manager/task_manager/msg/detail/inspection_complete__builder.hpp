// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from task_manager:msg/InspectionComplete.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__MSG__DETAIL__INSPECTION_COMPLETE__BUILDER_HPP_
#define TASK_MANAGER__MSG__DETAIL__INSPECTION_COMPLETE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "task_manager/msg/detail/inspection_complete__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace task_manager
{

namespace msg
{

namespace builder
{

class Init_InspectionComplete_product_code
{
public:
  Init_InspectionComplete_product_code()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::task_manager::msg::InspectionComplete product_code(::task_manager::msg::InspectionComplete::_product_code_type arg)
  {
    msg_.product_code = std::move(arg);
    return std::move(msg_);
  }

private:
  ::task_manager::msg::InspectionComplete msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::task_manager::msg::InspectionComplete>()
{
  return task_manager::msg::builder::Init_InspectionComplete_product_code();
}

}  // namespace task_manager

#endif  // TASK_MANAGER__MSG__DETAIL__INSPECTION_COMPLETE__BUILDER_HPP_
