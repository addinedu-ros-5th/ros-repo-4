// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_state:srv/UpdateDB.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_STATE__SRV__DETAIL__UPDATE_DB__BUILDER_HPP_
#define ROBOT_STATE__SRV__DETAIL__UPDATE_DB__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robot_state/srv/detail/update_db__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robot_state
{

namespace srv
{

namespace builder
{

class Init_UpdateDB_Request_robot_name
{
public:
  Init_UpdateDB_Request_robot_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_state::srv::UpdateDB_Request robot_name(::robot_state::srv::UpdateDB_Request::_robot_name_type arg)
  {
    msg_.robot_name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_state::srv::UpdateDB_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_state::srv::UpdateDB_Request>()
{
  return robot_state::srv::builder::Init_UpdateDB_Request_robot_name();
}

}  // namespace robot_state


namespace robot_state
{

namespace srv
{

namespace builder
{

class Init_UpdateDB_Response_status
{
public:
  explicit Init_UpdateDB_Response_status(::robot_state::srv::UpdateDB_Response & msg)
  : msg_(msg)
  {}
  ::robot_state::srv::UpdateDB_Response status(::robot_state::srv::UpdateDB_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_state::srv::UpdateDB_Response msg_;
};

class Init_UpdateDB_Response_battery_status
{
public:
  explicit Init_UpdateDB_Response_battery_status(::robot_state::srv::UpdateDB_Response & msg)
  : msg_(msg)
  {}
  Init_UpdateDB_Response_status battery_status(::robot_state::srv::UpdateDB_Response::_battery_status_type arg)
  {
    msg_.battery_status = std::move(arg);
    return Init_UpdateDB_Response_status(msg_);
  }

private:
  ::robot_state::srv::UpdateDB_Response msg_;
};

class Init_UpdateDB_Response_robot_name
{
public:
  Init_UpdateDB_Response_robot_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_UpdateDB_Response_battery_status robot_name(::robot_state::srv::UpdateDB_Response::_robot_name_type arg)
  {
    msg_.robot_name = std::move(arg);
    return Init_UpdateDB_Response_battery_status(msg_);
  }

private:
  ::robot_state::srv::UpdateDB_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_state::srv::UpdateDB_Response>()
{
  return robot_state::srv::builder::Init_UpdateDB_Response_robot_name();
}

}  // namespace robot_state

#endif  // ROBOT_STATE__SRV__DETAIL__UPDATE_DB__BUILDER_HPP_
