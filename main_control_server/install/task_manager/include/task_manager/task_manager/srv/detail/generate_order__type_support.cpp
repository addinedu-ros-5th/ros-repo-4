// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from task_manager:srv/GenerateOrder.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "task_manager/srv/detail/generate_order__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace task_manager
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

void GenerateOrder_Request_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) task_manager::srv::GenerateOrder_Request(_init);
}

void GenerateOrder_Request_fini_function(void * message_memory)
{
  auto typed_message = static_cast<task_manager::srv::GenerateOrder_Request *>(message_memory);
  typed_message->~GenerateOrder_Request();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember GenerateOrder_Request_message_member_array[1] = {
  {
    "structure_needs_at_least_one_member",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager::srv::GenerateOrder_Request, structure_needs_at_least_one_member),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers GenerateOrder_Request_message_members = {
  "task_manager::srv",  // message namespace
  "GenerateOrder_Request",  // message name
  1,  // number of fields
  sizeof(task_manager::srv::GenerateOrder_Request),
  GenerateOrder_Request_message_member_array,  // message members
  GenerateOrder_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  GenerateOrder_Request_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t GenerateOrder_Request_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &GenerateOrder_Request_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace task_manager


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<task_manager::srv::GenerateOrder_Request>()
{
  return &::task_manager::srv::rosidl_typesupport_introspection_cpp::GenerateOrder_Request_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, task_manager, srv, GenerateOrder_Request)() {
  return &::task_manager::srv::rosidl_typesupport_introspection_cpp::GenerateOrder_Request_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "array"
// already included above
// #include "cstddef"
// already included above
// #include "string"
// already included above
// #include "vector"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "task_manager/srv/detail/generate_order__struct.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/field_types.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace task_manager
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

void GenerateOrder_Response_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) task_manager::srv::GenerateOrder_Response(_init);
}

void GenerateOrder_Response_fini_function(void * message_memory)
{
  auto typed_message = static_cast<task_manager::srv::GenerateOrder_Response *>(message_memory);
  typed_message->~GenerateOrder_Response();
}

size_t size_function__GenerateOrder_Response__item_ids(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return member->size();
}

const void * get_const_function__GenerateOrder_Response__item_ids(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void * get_function__GenerateOrder_Response__item_ids(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void fetch_function__GenerateOrder_Response__item_ids(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const std::string *>(
    get_const_function__GenerateOrder_Response__item_ids(untyped_member, index));
  auto & value = *reinterpret_cast<std::string *>(untyped_value);
  value = item;
}

void assign_function__GenerateOrder_Response__item_ids(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<std::string *>(
    get_function__GenerateOrder_Response__item_ids(untyped_member, index));
  const auto & value = *reinterpret_cast<const std::string *>(untyped_value);
  item = value;
}

void resize_function__GenerateOrder_Response__item_ids(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<std::string> *>(untyped_member);
  member->resize(size);
}

size_t size_function__GenerateOrder_Response__names(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return member->size();
}

const void * get_const_function__GenerateOrder_Response__names(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void * get_function__GenerateOrder_Response__names(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void fetch_function__GenerateOrder_Response__names(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const std::string *>(
    get_const_function__GenerateOrder_Response__names(untyped_member, index));
  auto & value = *reinterpret_cast<std::string *>(untyped_value);
  value = item;
}

void assign_function__GenerateOrder_Response__names(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<std::string *>(
    get_function__GenerateOrder_Response__names(untyped_member, index));
  const auto & value = *reinterpret_cast<const std::string *>(untyped_value);
  item = value;
}

void resize_function__GenerateOrder_Response__names(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<std::string> *>(untyped_member);
  member->resize(size);
}

size_t size_function__GenerateOrder_Response__quantities(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__GenerateOrder_Response__quantities(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void * get_function__GenerateOrder_Response__quantities(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void fetch_function__GenerateOrder_Response__quantities(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const int32_t *>(
    get_const_function__GenerateOrder_Response__quantities(untyped_member, index));
  auto & value = *reinterpret_cast<int32_t *>(untyped_value);
  value = item;
}

void assign_function__GenerateOrder_Response__quantities(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<int32_t *>(
    get_function__GenerateOrder_Response__quantities(untyped_member, index));
  const auto & value = *reinterpret_cast<const int32_t *>(untyped_value);
  item = value;
}

void resize_function__GenerateOrder_Response__quantities(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  member->resize(size);
}

size_t size_function__GenerateOrder_Response__warehouses(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return member->size();
}

const void * get_const_function__GenerateOrder_Response__warehouses(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void * get_function__GenerateOrder_Response__warehouses(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void fetch_function__GenerateOrder_Response__warehouses(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const std::string *>(
    get_const_function__GenerateOrder_Response__warehouses(untyped_member, index));
  auto & value = *reinterpret_cast<std::string *>(untyped_value);
  value = item;
}

void assign_function__GenerateOrder_Response__warehouses(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<std::string *>(
    get_function__GenerateOrder_Response__warehouses(untyped_member, index));
  const auto & value = *reinterpret_cast<const std::string *>(untyped_value);
  item = value;
}

void resize_function__GenerateOrder_Response__warehouses(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<std::string> *>(untyped_member);
  member->resize(size);
}

size_t size_function__GenerateOrder_Response__racks(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return member->size();
}

const void * get_const_function__GenerateOrder_Response__racks(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void * get_function__GenerateOrder_Response__racks(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void fetch_function__GenerateOrder_Response__racks(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const std::string *>(
    get_const_function__GenerateOrder_Response__racks(untyped_member, index));
  auto & value = *reinterpret_cast<std::string *>(untyped_value);
  value = item;
}

void assign_function__GenerateOrder_Response__racks(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<std::string *>(
    get_function__GenerateOrder_Response__racks(untyped_member, index));
  const auto & value = *reinterpret_cast<const std::string *>(untyped_value);
  item = value;
}

void resize_function__GenerateOrder_Response__racks(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<std::string> *>(untyped_member);
  member->resize(size);
}

size_t size_function__GenerateOrder_Response__cells(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return member->size();
}

const void * get_const_function__GenerateOrder_Response__cells(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void * get_function__GenerateOrder_Response__cells(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void fetch_function__GenerateOrder_Response__cells(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const std::string *>(
    get_const_function__GenerateOrder_Response__cells(untyped_member, index));
  auto & value = *reinterpret_cast<std::string *>(untyped_value);
  value = item;
}

void assign_function__GenerateOrder_Response__cells(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<std::string *>(
    get_function__GenerateOrder_Response__cells(untyped_member, index));
  const auto & value = *reinterpret_cast<const std::string *>(untyped_value);
  item = value;
}

void resize_function__GenerateOrder_Response__cells(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<std::string> *>(untyped_member);
  member->resize(size);
}

size_t size_function__GenerateOrder_Response__statuses(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return member->size();
}

const void * get_const_function__GenerateOrder_Response__statuses(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void * get_function__GenerateOrder_Response__statuses(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void fetch_function__GenerateOrder_Response__statuses(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const std::string *>(
    get_const_function__GenerateOrder_Response__statuses(untyped_member, index));
  auto & value = *reinterpret_cast<std::string *>(untyped_value);
  value = item;
}

void assign_function__GenerateOrder_Response__statuses(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<std::string *>(
    get_function__GenerateOrder_Response__statuses(untyped_member, index));
  const auto & value = *reinterpret_cast<const std::string *>(untyped_value);
  item = value;
}

void resize_function__GenerateOrder_Response__statuses(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<std::string> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember GenerateOrder_Response_message_member_array[7] = {
  {
    "item_ids",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager::srv::GenerateOrder_Response, item_ids),  // bytes offset in struct
    nullptr,  // default value
    size_function__GenerateOrder_Response__item_ids,  // size() function pointer
    get_const_function__GenerateOrder_Response__item_ids,  // get_const(index) function pointer
    get_function__GenerateOrder_Response__item_ids,  // get(index) function pointer
    fetch_function__GenerateOrder_Response__item_ids,  // fetch(index, &value) function pointer
    assign_function__GenerateOrder_Response__item_ids,  // assign(index, value) function pointer
    resize_function__GenerateOrder_Response__item_ids  // resize(index) function pointer
  },
  {
    "names",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager::srv::GenerateOrder_Response, names),  // bytes offset in struct
    nullptr,  // default value
    size_function__GenerateOrder_Response__names,  // size() function pointer
    get_const_function__GenerateOrder_Response__names,  // get_const(index) function pointer
    get_function__GenerateOrder_Response__names,  // get(index) function pointer
    fetch_function__GenerateOrder_Response__names,  // fetch(index, &value) function pointer
    assign_function__GenerateOrder_Response__names,  // assign(index, value) function pointer
    resize_function__GenerateOrder_Response__names  // resize(index) function pointer
  },
  {
    "quantities",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager::srv::GenerateOrder_Response, quantities),  // bytes offset in struct
    nullptr,  // default value
    size_function__GenerateOrder_Response__quantities,  // size() function pointer
    get_const_function__GenerateOrder_Response__quantities,  // get_const(index) function pointer
    get_function__GenerateOrder_Response__quantities,  // get(index) function pointer
    fetch_function__GenerateOrder_Response__quantities,  // fetch(index, &value) function pointer
    assign_function__GenerateOrder_Response__quantities,  // assign(index, value) function pointer
    resize_function__GenerateOrder_Response__quantities  // resize(index) function pointer
  },
  {
    "warehouses",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager::srv::GenerateOrder_Response, warehouses),  // bytes offset in struct
    nullptr,  // default value
    size_function__GenerateOrder_Response__warehouses,  // size() function pointer
    get_const_function__GenerateOrder_Response__warehouses,  // get_const(index) function pointer
    get_function__GenerateOrder_Response__warehouses,  // get(index) function pointer
    fetch_function__GenerateOrder_Response__warehouses,  // fetch(index, &value) function pointer
    assign_function__GenerateOrder_Response__warehouses,  // assign(index, value) function pointer
    resize_function__GenerateOrder_Response__warehouses  // resize(index) function pointer
  },
  {
    "racks",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager::srv::GenerateOrder_Response, racks),  // bytes offset in struct
    nullptr,  // default value
    size_function__GenerateOrder_Response__racks,  // size() function pointer
    get_const_function__GenerateOrder_Response__racks,  // get_const(index) function pointer
    get_function__GenerateOrder_Response__racks,  // get(index) function pointer
    fetch_function__GenerateOrder_Response__racks,  // fetch(index, &value) function pointer
    assign_function__GenerateOrder_Response__racks,  // assign(index, value) function pointer
    resize_function__GenerateOrder_Response__racks  // resize(index) function pointer
  },
  {
    "cells",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager::srv::GenerateOrder_Response, cells),  // bytes offset in struct
    nullptr,  // default value
    size_function__GenerateOrder_Response__cells,  // size() function pointer
    get_const_function__GenerateOrder_Response__cells,  // get_const(index) function pointer
    get_function__GenerateOrder_Response__cells,  // get(index) function pointer
    fetch_function__GenerateOrder_Response__cells,  // fetch(index, &value) function pointer
    assign_function__GenerateOrder_Response__cells,  // assign(index, value) function pointer
    resize_function__GenerateOrder_Response__cells  // resize(index) function pointer
  },
  {
    "statuses",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager::srv::GenerateOrder_Response, statuses),  // bytes offset in struct
    nullptr,  // default value
    size_function__GenerateOrder_Response__statuses,  // size() function pointer
    get_const_function__GenerateOrder_Response__statuses,  // get_const(index) function pointer
    get_function__GenerateOrder_Response__statuses,  // get(index) function pointer
    fetch_function__GenerateOrder_Response__statuses,  // fetch(index, &value) function pointer
    assign_function__GenerateOrder_Response__statuses,  // assign(index, value) function pointer
    resize_function__GenerateOrder_Response__statuses  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers GenerateOrder_Response_message_members = {
  "task_manager::srv",  // message namespace
  "GenerateOrder_Response",  // message name
  7,  // number of fields
  sizeof(task_manager::srv::GenerateOrder_Response),
  GenerateOrder_Response_message_member_array,  // message members
  GenerateOrder_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  GenerateOrder_Response_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t GenerateOrder_Response_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &GenerateOrder_Response_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace task_manager


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<task_manager::srv::GenerateOrder_Response>()
{
  return &::task_manager::srv::rosidl_typesupport_introspection_cpp::GenerateOrder_Response_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, task_manager, srv, GenerateOrder_Response)() {
  return &::task_manager::srv::rosidl_typesupport_introspection_cpp::GenerateOrder_Response_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "rosidl_typesupport_introspection_cpp/visibility_control.h"
// already included above
// #include "task_manager/srv/detail/generate_order__struct.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/service_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/service_type_support_decl.hpp"

namespace task_manager
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

// this is intentionally not const to allow initialization later to prevent an initialization race
static ::rosidl_typesupport_introspection_cpp::ServiceMembers GenerateOrder_service_members = {
  "task_manager::srv",  // service namespace
  "GenerateOrder",  // service name
  // these two fields are initialized below on the first access
  // see get_service_type_support_handle<task_manager::srv::GenerateOrder>()
  nullptr,  // request message
  nullptr  // response message
};

static const rosidl_service_type_support_t GenerateOrder_service_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &GenerateOrder_service_members,
  get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace task_manager


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<task_manager::srv::GenerateOrder>()
{
  // get a handle to the value to be returned
  auto service_type_support =
    &::task_manager::srv::rosidl_typesupport_introspection_cpp::GenerateOrder_service_type_support_handle;
  // get a non-const and properly typed version of the data void *
  auto service_members = const_cast<::rosidl_typesupport_introspection_cpp::ServiceMembers *>(
    static_cast<const ::rosidl_typesupport_introspection_cpp::ServiceMembers *>(
      service_type_support->data));
  // make sure that both the request_members_ and the response_members_ are initialized
  // if they are not, initialize them
  if (
    service_members->request_members_ == nullptr ||
    service_members->response_members_ == nullptr)
  {
    // initialize the request_members_ with the static function from the external library
    service_members->request_members_ = static_cast<
      const ::rosidl_typesupport_introspection_cpp::MessageMembers *
      >(
      ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<
        ::task_manager::srv::GenerateOrder_Request
      >()->data
      );
    // initialize the response_members_ with the static function from the external library
    service_members->response_members_ = static_cast<
      const ::rosidl_typesupport_introspection_cpp::MessageMembers *
      >(
      ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<
        ::task_manager::srv::GenerateOrder_Response
      >()->data
      );
  }
  // finally return the properly initialized service_type_support handle
  return service_type_support;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, task_manager, srv, GenerateOrder)() {
  return ::rosidl_typesupport_introspection_cpp::get_service_type_support_handle<task_manager::srv::GenerateOrder>();
}

#ifdef __cplusplus
}
#endif
