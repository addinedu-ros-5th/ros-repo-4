// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from task_manager:msg/GuiUpdate.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__MSG__DETAIL__GUI_UPDATE__BUILDER_HPP_
#define TASK_MANAGER__MSG__DETAIL__GUI_UPDATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "task_manager/msg/detail/gui_update__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace task_manager
{

namespace msg
{

namespace builder
{

class Init_GuiUpdate_message
{
public:
  explicit Init_GuiUpdate_message(::task_manager::msg::GuiUpdate & msg)
  : msg_(msg)
  {}
  ::task_manager::msg::GuiUpdate message(::task_manager::msg::GuiUpdate::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::task_manager::msg::GuiUpdate msg_;
};

class Init_GuiUpdate_status
{
public:
  explicit Init_GuiUpdate_status(::task_manager::msg::GuiUpdate & msg)
  : msg_(msg)
  {}
  Init_GuiUpdate_message status(::task_manager::msg::GuiUpdate::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_GuiUpdate_message(msg_);
  }

private:
  ::task_manager::msg::GuiUpdate msg_;
};

class Init_GuiUpdate_product_code
{
public:
  Init_GuiUpdate_product_code()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GuiUpdate_status product_code(::task_manager::msg::GuiUpdate::_product_code_type arg)
  {
    msg_.product_code = std::move(arg);
    return Init_GuiUpdate_status(msg_);
  }

private:
  ::task_manager::msg::GuiUpdate msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::task_manager::msg::GuiUpdate>()
{
  return task_manager::msg::builder::Init_GuiUpdate_product_code();
}

}  // namespace task_manager

#endif  // TASK_MANAGER__MSG__DETAIL__GUI_UPDATE__BUILDER_HPP_
