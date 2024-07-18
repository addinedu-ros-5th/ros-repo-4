// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from task_manager:srv/GenerateOrder.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__SRV__DETAIL__GENERATE_ORDER__BUILDER_HPP_
#define TASK_MANAGER__SRV__DETAIL__GENERATE_ORDER__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "task_manager/srv/detail/generate_order__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace task_manager
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::task_manager::srv::GenerateOrder_Request>()
{
  return ::task_manager::srv::GenerateOrder_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace task_manager


namespace task_manager
{

namespace srv
{

namespace builder
{

class Init_GenerateOrder_Response_statuses
{
public:
  explicit Init_GenerateOrder_Response_statuses(::task_manager::srv::GenerateOrder_Response & msg)
  : msg_(msg)
  {}
  ::task_manager::srv::GenerateOrder_Response statuses(::task_manager::srv::GenerateOrder_Response::_statuses_type arg)
  {
    msg_.statuses = std::move(arg);
    return std::move(msg_);
  }

private:
  ::task_manager::srv::GenerateOrder_Response msg_;
};

class Init_GenerateOrder_Response_cells
{
public:
  explicit Init_GenerateOrder_Response_cells(::task_manager::srv::GenerateOrder_Response & msg)
  : msg_(msg)
  {}
  Init_GenerateOrder_Response_statuses cells(::task_manager::srv::GenerateOrder_Response::_cells_type arg)
  {
    msg_.cells = std::move(arg);
    return Init_GenerateOrder_Response_statuses(msg_);
  }

private:
  ::task_manager::srv::GenerateOrder_Response msg_;
};

class Init_GenerateOrder_Response_racks
{
public:
  explicit Init_GenerateOrder_Response_racks(::task_manager::srv::GenerateOrder_Response & msg)
  : msg_(msg)
  {}
  Init_GenerateOrder_Response_cells racks(::task_manager::srv::GenerateOrder_Response::_racks_type arg)
  {
    msg_.racks = std::move(arg);
    return Init_GenerateOrder_Response_cells(msg_);
  }

private:
  ::task_manager::srv::GenerateOrder_Response msg_;
};

class Init_GenerateOrder_Response_warehouses
{
public:
  explicit Init_GenerateOrder_Response_warehouses(::task_manager::srv::GenerateOrder_Response & msg)
  : msg_(msg)
  {}
  Init_GenerateOrder_Response_racks warehouses(::task_manager::srv::GenerateOrder_Response::_warehouses_type arg)
  {
    msg_.warehouses = std::move(arg);
    return Init_GenerateOrder_Response_racks(msg_);
  }

private:
  ::task_manager::srv::GenerateOrder_Response msg_;
};

class Init_GenerateOrder_Response_quantities
{
public:
  explicit Init_GenerateOrder_Response_quantities(::task_manager::srv::GenerateOrder_Response & msg)
  : msg_(msg)
  {}
  Init_GenerateOrder_Response_warehouses quantities(::task_manager::srv::GenerateOrder_Response::_quantities_type arg)
  {
    msg_.quantities = std::move(arg);
    return Init_GenerateOrder_Response_warehouses(msg_);
  }

private:
  ::task_manager::srv::GenerateOrder_Response msg_;
};

class Init_GenerateOrder_Response_names
{
public:
  explicit Init_GenerateOrder_Response_names(::task_manager::srv::GenerateOrder_Response & msg)
  : msg_(msg)
  {}
  Init_GenerateOrder_Response_quantities names(::task_manager::srv::GenerateOrder_Response::_names_type arg)
  {
    msg_.names = std::move(arg);
    return Init_GenerateOrder_Response_quantities(msg_);
  }

private:
  ::task_manager::srv::GenerateOrder_Response msg_;
};

class Init_GenerateOrder_Response_item_ids
{
public:
  Init_GenerateOrder_Response_item_ids()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GenerateOrder_Response_names item_ids(::task_manager::srv::GenerateOrder_Response::_item_ids_type arg)
  {
    msg_.item_ids = std::move(arg);
    return Init_GenerateOrder_Response_names(msg_);
  }

private:
  ::task_manager::srv::GenerateOrder_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::task_manager::srv::GenerateOrder_Response>()
{
  return task_manager::srv::builder::Init_GenerateOrder_Response_item_ids();
}

}  // namespace task_manager

#endif  // TASK_MANAGER__SRV__DETAIL__GENERATE_ORDER__BUILDER_HPP_
