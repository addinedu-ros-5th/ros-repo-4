// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from task_manager:srv/GenerateOrder.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "task_manager/srv/detail/generate_order__rosidl_typesupport_introspection_c.h"
#include "task_manager/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "task_manager/srv/detail/generate_order__functions.h"
#include "task_manager/srv/detail/generate_order__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void task_manager__srv__GenerateOrder_Request__rosidl_typesupport_introspection_c__GenerateOrder_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  task_manager__srv__GenerateOrder_Request__init(message_memory);
}

void task_manager__srv__GenerateOrder_Request__rosidl_typesupport_introspection_c__GenerateOrder_Request_fini_function(void * message_memory)
{
  task_manager__srv__GenerateOrder_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember task_manager__srv__GenerateOrder_Request__rosidl_typesupport_introspection_c__GenerateOrder_Request_message_member_array[1] = {
  {
    "structure_needs_at_least_one_member",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager__srv__GenerateOrder_Request, structure_needs_at_least_one_member),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers task_manager__srv__GenerateOrder_Request__rosidl_typesupport_introspection_c__GenerateOrder_Request_message_members = {
  "task_manager__srv",  // message namespace
  "GenerateOrder_Request",  // message name
  1,  // number of fields
  sizeof(task_manager__srv__GenerateOrder_Request),
  task_manager__srv__GenerateOrder_Request__rosidl_typesupport_introspection_c__GenerateOrder_Request_message_member_array,  // message members
  task_manager__srv__GenerateOrder_Request__rosidl_typesupport_introspection_c__GenerateOrder_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  task_manager__srv__GenerateOrder_Request__rosidl_typesupport_introspection_c__GenerateOrder_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t task_manager__srv__GenerateOrder_Request__rosidl_typesupport_introspection_c__GenerateOrder_Request_message_type_support_handle = {
  0,
  &task_manager__srv__GenerateOrder_Request__rosidl_typesupport_introspection_c__GenerateOrder_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_task_manager
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task_manager, srv, GenerateOrder_Request)() {
  if (!task_manager__srv__GenerateOrder_Request__rosidl_typesupport_introspection_c__GenerateOrder_Request_message_type_support_handle.typesupport_identifier) {
    task_manager__srv__GenerateOrder_Request__rosidl_typesupport_introspection_c__GenerateOrder_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &task_manager__srv__GenerateOrder_Request__rosidl_typesupport_introspection_c__GenerateOrder_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "task_manager/srv/detail/generate_order__rosidl_typesupport_introspection_c.h"
// already included above
// #include "task_manager/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "task_manager/srv/detail/generate_order__functions.h"
// already included above
// #include "task_manager/srv/detail/generate_order__struct.h"


// Include directives for member types
// Member `item_ids`
// Member `names`
// Member `warehouses`
// Member `racks`
// Member `cells`
// Member `statuses`
#include "rosidl_runtime_c/string_functions.h"
// Member `quantities`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__GenerateOrder_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  task_manager__srv__GenerateOrder_Response__init(message_memory);
}

void task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__GenerateOrder_Response_fini_function(void * message_memory)
{
  task_manager__srv__GenerateOrder_Response__fini(message_memory);
}

size_t task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__size_function__GenerateOrder_Response__item_ids(
  const void * untyped_member)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return member->size;
}

const void * task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_const_function__GenerateOrder_Response__item_ids(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void * task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_function__GenerateOrder_Response__item_ids(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__fetch_function__GenerateOrder_Response__item_ids(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const rosidl_runtime_c__String * item =
    ((const rosidl_runtime_c__String *)
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_const_function__GenerateOrder_Response__item_ids(untyped_member, index));
  rosidl_runtime_c__String * value =
    (rosidl_runtime_c__String *)(untyped_value);
  *value = *item;
}

void task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__assign_function__GenerateOrder_Response__item_ids(
  void * untyped_member, size_t index, const void * untyped_value)
{
  rosidl_runtime_c__String * item =
    ((rosidl_runtime_c__String *)
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_function__GenerateOrder_Response__item_ids(untyped_member, index));
  const rosidl_runtime_c__String * value =
    (const rosidl_runtime_c__String *)(untyped_value);
  *item = *value;
}

bool task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__resize_function__GenerateOrder_Response__item_ids(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  rosidl_runtime_c__String__Sequence__fini(member);
  return rosidl_runtime_c__String__Sequence__init(member, size);
}

size_t task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__size_function__GenerateOrder_Response__names(
  const void * untyped_member)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return member->size;
}

const void * task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_const_function__GenerateOrder_Response__names(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void * task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_function__GenerateOrder_Response__names(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__fetch_function__GenerateOrder_Response__names(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const rosidl_runtime_c__String * item =
    ((const rosidl_runtime_c__String *)
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_const_function__GenerateOrder_Response__names(untyped_member, index));
  rosidl_runtime_c__String * value =
    (rosidl_runtime_c__String *)(untyped_value);
  *value = *item;
}

void task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__assign_function__GenerateOrder_Response__names(
  void * untyped_member, size_t index, const void * untyped_value)
{
  rosidl_runtime_c__String * item =
    ((rosidl_runtime_c__String *)
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_function__GenerateOrder_Response__names(untyped_member, index));
  const rosidl_runtime_c__String * value =
    (const rosidl_runtime_c__String *)(untyped_value);
  *item = *value;
}

bool task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__resize_function__GenerateOrder_Response__names(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  rosidl_runtime_c__String__Sequence__fini(member);
  return rosidl_runtime_c__String__Sequence__init(member, size);
}

size_t task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__size_function__GenerateOrder_Response__quantities(
  const void * untyped_member)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return member->size;
}

const void * task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_const_function__GenerateOrder_Response__quantities(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void * task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_function__GenerateOrder_Response__quantities(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__fetch_function__GenerateOrder_Response__quantities(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const int32_t * item =
    ((const int32_t *)
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_const_function__GenerateOrder_Response__quantities(untyped_member, index));
  int32_t * value =
    (int32_t *)(untyped_value);
  *value = *item;
}

void task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__assign_function__GenerateOrder_Response__quantities(
  void * untyped_member, size_t index, const void * untyped_value)
{
  int32_t * item =
    ((int32_t *)
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_function__GenerateOrder_Response__quantities(untyped_member, index));
  const int32_t * value =
    (const int32_t *)(untyped_value);
  *item = *value;
}

bool task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__resize_function__GenerateOrder_Response__quantities(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  rosidl_runtime_c__int32__Sequence__fini(member);
  return rosidl_runtime_c__int32__Sequence__init(member, size);
}

size_t task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__size_function__GenerateOrder_Response__warehouses(
  const void * untyped_member)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return member->size;
}

const void * task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_const_function__GenerateOrder_Response__warehouses(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void * task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_function__GenerateOrder_Response__warehouses(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__fetch_function__GenerateOrder_Response__warehouses(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const rosidl_runtime_c__String * item =
    ((const rosidl_runtime_c__String *)
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_const_function__GenerateOrder_Response__warehouses(untyped_member, index));
  rosidl_runtime_c__String * value =
    (rosidl_runtime_c__String *)(untyped_value);
  *value = *item;
}

void task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__assign_function__GenerateOrder_Response__warehouses(
  void * untyped_member, size_t index, const void * untyped_value)
{
  rosidl_runtime_c__String * item =
    ((rosidl_runtime_c__String *)
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_function__GenerateOrder_Response__warehouses(untyped_member, index));
  const rosidl_runtime_c__String * value =
    (const rosidl_runtime_c__String *)(untyped_value);
  *item = *value;
}

bool task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__resize_function__GenerateOrder_Response__warehouses(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  rosidl_runtime_c__String__Sequence__fini(member);
  return rosidl_runtime_c__String__Sequence__init(member, size);
}

size_t task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__size_function__GenerateOrder_Response__racks(
  const void * untyped_member)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return member->size;
}

const void * task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_const_function__GenerateOrder_Response__racks(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void * task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_function__GenerateOrder_Response__racks(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__fetch_function__GenerateOrder_Response__racks(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const rosidl_runtime_c__String * item =
    ((const rosidl_runtime_c__String *)
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_const_function__GenerateOrder_Response__racks(untyped_member, index));
  rosidl_runtime_c__String * value =
    (rosidl_runtime_c__String *)(untyped_value);
  *value = *item;
}

void task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__assign_function__GenerateOrder_Response__racks(
  void * untyped_member, size_t index, const void * untyped_value)
{
  rosidl_runtime_c__String * item =
    ((rosidl_runtime_c__String *)
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_function__GenerateOrder_Response__racks(untyped_member, index));
  const rosidl_runtime_c__String * value =
    (const rosidl_runtime_c__String *)(untyped_value);
  *item = *value;
}

bool task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__resize_function__GenerateOrder_Response__racks(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  rosidl_runtime_c__String__Sequence__fini(member);
  return rosidl_runtime_c__String__Sequence__init(member, size);
}

size_t task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__size_function__GenerateOrder_Response__cells(
  const void * untyped_member)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return member->size;
}

const void * task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_const_function__GenerateOrder_Response__cells(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void * task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_function__GenerateOrder_Response__cells(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__fetch_function__GenerateOrder_Response__cells(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const rosidl_runtime_c__String * item =
    ((const rosidl_runtime_c__String *)
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_const_function__GenerateOrder_Response__cells(untyped_member, index));
  rosidl_runtime_c__String * value =
    (rosidl_runtime_c__String *)(untyped_value);
  *value = *item;
}

void task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__assign_function__GenerateOrder_Response__cells(
  void * untyped_member, size_t index, const void * untyped_value)
{
  rosidl_runtime_c__String * item =
    ((rosidl_runtime_c__String *)
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_function__GenerateOrder_Response__cells(untyped_member, index));
  const rosidl_runtime_c__String * value =
    (const rosidl_runtime_c__String *)(untyped_value);
  *item = *value;
}

bool task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__resize_function__GenerateOrder_Response__cells(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  rosidl_runtime_c__String__Sequence__fini(member);
  return rosidl_runtime_c__String__Sequence__init(member, size);
}

size_t task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__size_function__GenerateOrder_Response__statuses(
  const void * untyped_member)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return member->size;
}

const void * task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_const_function__GenerateOrder_Response__statuses(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void * task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_function__GenerateOrder_Response__statuses(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__fetch_function__GenerateOrder_Response__statuses(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const rosidl_runtime_c__String * item =
    ((const rosidl_runtime_c__String *)
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_const_function__GenerateOrder_Response__statuses(untyped_member, index));
  rosidl_runtime_c__String * value =
    (rosidl_runtime_c__String *)(untyped_value);
  *value = *item;
}

void task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__assign_function__GenerateOrder_Response__statuses(
  void * untyped_member, size_t index, const void * untyped_value)
{
  rosidl_runtime_c__String * item =
    ((rosidl_runtime_c__String *)
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_function__GenerateOrder_Response__statuses(untyped_member, index));
  const rosidl_runtime_c__String * value =
    (const rosidl_runtime_c__String *)(untyped_value);
  *item = *value;
}

bool task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__resize_function__GenerateOrder_Response__statuses(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  rosidl_runtime_c__String__Sequence__fini(member);
  return rosidl_runtime_c__String__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__GenerateOrder_Response_message_member_array[7] = {
  {
    "item_ids",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager__srv__GenerateOrder_Response, item_ids),  // bytes offset in struct
    NULL,  // default value
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__size_function__GenerateOrder_Response__item_ids,  // size() function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_const_function__GenerateOrder_Response__item_ids,  // get_const(index) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_function__GenerateOrder_Response__item_ids,  // get(index) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__fetch_function__GenerateOrder_Response__item_ids,  // fetch(index, &value) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__assign_function__GenerateOrder_Response__item_ids,  // assign(index, value) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__resize_function__GenerateOrder_Response__item_ids  // resize(index) function pointer
  },
  {
    "names",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager__srv__GenerateOrder_Response, names),  // bytes offset in struct
    NULL,  // default value
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__size_function__GenerateOrder_Response__names,  // size() function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_const_function__GenerateOrder_Response__names,  // get_const(index) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_function__GenerateOrder_Response__names,  // get(index) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__fetch_function__GenerateOrder_Response__names,  // fetch(index, &value) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__assign_function__GenerateOrder_Response__names,  // assign(index, value) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__resize_function__GenerateOrder_Response__names  // resize(index) function pointer
  },
  {
    "quantities",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager__srv__GenerateOrder_Response, quantities),  // bytes offset in struct
    NULL,  // default value
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__size_function__GenerateOrder_Response__quantities,  // size() function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_const_function__GenerateOrder_Response__quantities,  // get_const(index) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_function__GenerateOrder_Response__quantities,  // get(index) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__fetch_function__GenerateOrder_Response__quantities,  // fetch(index, &value) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__assign_function__GenerateOrder_Response__quantities,  // assign(index, value) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__resize_function__GenerateOrder_Response__quantities  // resize(index) function pointer
  },
  {
    "warehouses",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager__srv__GenerateOrder_Response, warehouses),  // bytes offset in struct
    NULL,  // default value
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__size_function__GenerateOrder_Response__warehouses,  // size() function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_const_function__GenerateOrder_Response__warehouses,  // get_const(index) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_function__GenerateOrder_Response__warehouses,  // get(index) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__fetch_function__GenerateOrder_Response__warehouses,  // fetch(index, &value) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__assign_function__GenerateOrder_Response__warehouses,  // assign(index, value) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__resize_function__GenerateOrder_Response__warehouses  // resize(index) function pointer
  },
  {
    "racks",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager__srv__GenerateOrder_Response, racks),  // bytes offset in struct
    NULL,  // default value
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__size_function__GenerateOrder_Response__racks,  // size() function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_const_function__GenerateOrder_Response__racks,  // get_const(index) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_function__GenerateOrder_Response__racks,  // get(index) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__fetch_function__GenerateOrder_Response__racks,  // fetch(index, &value) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__assign_function__GenerateOrder_Response__racks,  // assign(index, value) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__resize_function__GenerateOrder_Response__racks  // resize(index) function pointer
  },
  {
    "cells",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager__srv__GenerateOrder_Response, cells),  // bytes offset in struct
    NULL,  // default value
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__size_function__GenerateOrder_Response__cells,  // size() function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_const_function__GenerateOrder_Response__cells,  // get_const(index) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_function__GenerateOrder_Response__cells,  // get(index) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__fetch_function__GenerateOrder_Response__cells,  // fetch(index, &value) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__assign_function__GenerateOrder_Response__cells,  // assign(index, value) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__resize_function__GenerateOrder_Response__cells  // resize(index) function pointer
  },
  {
    "statuses",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager__srv__GenerateOrder_Response, statuses),  // bytes offset in struct
    NULL,  // default value
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__size_function__GenerateOrder_Response__statuses,  // size() function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_const_function__GenerateOrder_Response__statuses,  // get_const(index) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__get_function__GenerateOrder_Response__statuses,  // get(index) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__fetch_function__GenerateOrder_Response__statuses,  // fetch(index, &value) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__assign_function__GenerateOrder_Response__statuses,  // assign(index, value) function pointer
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__resize_function__GenerateOrder_Response__statuses  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__GenerateOrder_Response_message_members = {
  "task_manager__srv",  // message namespace
  "GenerateOrder_Response",  // message name
  7,  // number of fields
  sizeof(task_manager__srv__GenerateOrder_Response),
  task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__GenerateOrder_Response_message_member_array,  // message members
  task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__GenerateOrder_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__GenerateOrder_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__GenerateOrder_Response_message_type_support_handle = {
  0,
  &task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__GenerateOrder_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_task_manager
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task_manager, srv, GenerateOrder_Response)() {
  if (!task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__GenerateOrder_Response_message_type_support_handle.typesupport_identifier) {
    task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__GenerateOrder_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &task_manager__srv__GenerateOrder_Response__rosidl_typesupport_introspection_c__GenerateOrder_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "task_manager/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "task_manager/srv/detail/generate_order__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers task_manager__srv__detail__generate_order__rosidl_typesupport_introspection_c__GenerateOrder_service_members = {
  "task_manager__srv",  // service namespace
  "GenerateOrder",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // task_manager__srv__detail__generate_order__rosidl_typesupport_introspection_c__GenerateOrder_Request_message_type_support_handle,
  NULL  // response message
  // task_manager__srv__detail__generate_order__rosidl_typesupport_introspection_c__GenerateOrder_Response_message_type_support_handle
};

static rosidl_service_type_support_t task_manager__srv__detail__generate_order__rosidl_typesupport_introspection_c__GenerateOrder_service_type_support_handle = {
  0,
  &task_manager__srv__detail__generate_order__rosidl_typesupport_introspection_c__GenerateOrder_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task_manager, srv, GenerateOrder_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task_manager, srv, GenerateOrder_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_task_manager
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task_manager, srv, GenerateOrder)() {
  if (!task_manager__srv__detail__generate_order__rosidl_typesupport_introspection_c__GenerateOrder_service_type_support_handle.typesupport_identifier) {
    task_manager__srv__detail__generate_order__rosidl_typesupport_introspection_c__GenerateOrder_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)task_manager__srv__detail__generate_order__rosidl_typesupport_introspection_c__GenerateOrder_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task_manager, srv, GenerateOrder_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task_manager, srv, GenerateOrder_Response)()->data;
  }

  return &task_manager__srv__detail__generate_order__rosidl_typesupport_introspection_c__GenerateOrder_service_type_support_handle;
}
