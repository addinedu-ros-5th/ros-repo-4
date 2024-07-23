// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from task_manager:msg/StartInspection.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "task_manager/msg/detail/start_inspection__rosidl_typesupport_introspection_c.h"
#include "task_manager/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "task_manager/msg/detail/start_inspection__functions.h"
#include "task_manager/msg/detail/start_inspection__struct.h"


// Include directives for member types
// Member `product_code`
// Member `product_name`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void task_manager__msg__StartInspection__rosidl_typesupport_introspection_c__StartInspection_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  task_manager__msg__StartInspection__init(message_memory);
}

void task_manager__msg__StartInspection__rosidl_typesupport_introspection_c__StartInspection_fini_function(void * message_memory)
{
  task_manager__msg__StartInspection__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember task_manager__msg__StartInspection__rosidl_typesupport_introspection_c__StartInspection_message_member_array[2] = {
  {
    "product_code",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager__msg__StartInspection, product_code),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "product_name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager__msg__StartInspection, product_name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers task_manager__msg__StartInspection__rosidl_typesupport_introspection_c__StartInspection_message_members = {
  "task_manager__msg",  // message namespace
  "StartInspection",  // message name
  2,  // number of fields
  sizeof(task_manager__msg__StartInspection),
  task_manager__msg__StartInspection__rosidl_typesupport_introspection_c__StartInspection_message_member_array,  // message members
  task_manager__msg__StartInspection__rosidl_typesupport_introspection_c__StartInspection_init_function,  // function to initialize message memory (memory has to be allocated)
  task_manager__msg__StartInspection__rosidl_typesupport_introspection_c__StartInspection_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t task_manager__msg__StartInspection__rosidl_typesupport_introspection_c__StartInspection_message_type_support_handle = {
  0,
  &task_manager__msg__StartInspection__rosidl_typesupport_introspection_c__StartInspection_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_task_manager
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task_manager, msg, StartInspection)() {
  if (!task_manager__msg__StartInspection__rosidl_typesupport_introspection_c__StartInspection_message_type_support_handle.typesupport_identifier) {
    task_manager__msg__StartInspection__rosidl_typesupport_introspection_c__StartInspection_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &task_manager__msg__StartInspection__rosidl_typesupport_introspection_c__StartInspection_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
