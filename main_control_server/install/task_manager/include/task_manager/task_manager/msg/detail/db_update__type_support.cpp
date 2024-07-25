// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from task_manager:msg/DbUpdate.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "task_manager/msg/detail/db_update__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace task_manager
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void DbUpdate_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) task_manager::msg::DbUpdate(_init);
}

void DbUpdate_fini_function(void * message_memory)
{
  auto typed_message = static_cast<task_manager::msg::DbUpdate *>(message_memory);
  typed_message->~DbUpdate();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember DbUpdate_message_member_array[1] = {
  {
    "status",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager::msg::DbUpdate, status),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers DbUpdate_message_members = {
  "task_manager::msg",  // message namespace
  "DbUpdate",  // message name
  1,  // number of fields
  sizeof(task_manager::msg::DbUpdate),
  DbUpdate_message_member_array,  // message members
  DbUpdate_init_function,  // function to initialize message memory (memory has to be allocated)
  DbUpdate_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t DbUpdate_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &DbUpdate_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace task_manager


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<task_manager::msg::DbUpdate>()
{
  return &::task_manager::msg::rosidl_typesupport_introspection_cpp::DbUpdate_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, task_manager, msg, DbUpdate)() {
  return &::task_manager::msg::rosidl_typesupport_introspection_cpp::DbUpdate_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
