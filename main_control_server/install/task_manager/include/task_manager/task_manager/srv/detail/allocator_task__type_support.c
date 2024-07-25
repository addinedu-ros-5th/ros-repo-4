// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from task_manager:srv/AllocatorTask.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "task_manager/srv/detail/allocator_task__rosidl_typesupport_introspection_c.h"
#include "task_manager/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "task_manager/srv/detail/allocator_task__functions.h"
#include "task_manager/srv/detail/allocator_task__struct.h"


// Include directives for member types
// Member `product_code`
// Member `task_type`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void task_manager__srv__AllocatorTask_Request__rosidl_typesupport_introspection_c__AllocatorTask_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  task_manager__srv__AllocatorTask_Request__init(message_memory);
}

void task_manager__srv__AllocatorTask_Request__rosidl_typesupport_introspection_c__AllocatorTask_Request_fini_function(void * message_memory)
{
  task_manager__srv__AllocatorTask_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember task_manager__srv__AllocatorTask_Request__rosidl_typesupport_introspection_c__AllocatorTask_Request_message_member_array[2] = {
  {
    "product_code",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager__srv__AllocatorTask_Request, product_code),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "task_type",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager__srv__AllocatorTask_Request, task_type),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers task_manager__srv__AllocatorTask_Request__rosidl_typesupport_introspection_c__AllocatorTask_Request_message_members = {
  "task_manager__srv",  // message namespace
  "AllocatorTask_Request",  // message name
  2,  // number of fields
  sizeof(task_manager__srv__AllocatorTask_Request),
  task_manager__srv__AllocatorTask_Request__rosidl_typesupport_introspection_c__AllocatorTask_Request_message_member_array,  // message members
  task_manager__srv__AllocatorTask_Request__rosidl_typesupport_introspection_c__AllocatorTask_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  task_manager__srv__AllocatorTask_Request__rosidl_typesupport_introspection_c__AllocatorTask_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t task_manager__srv__AllocatorTask_Request__rosidl_typesupport_introspection_c__AllocatorTask_Request_message_type_support_handle = {
  0,
  &task_manager__srv__AllocatorTask_Request__rosidl_typesupport_introspection_c__AllocatorTask_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_task_manager
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task_manager, srv, AllocatorTask_Request)() {
  if (!task_manager__srv__AllocatorTask_Request__rosidl_typesupport_introspection_c__AllocatorTask_Request_message_type_support_handle.typesupport_identifier) {
    task_manager__srv__AllocatorTask_Request__rosidl_typesupport_introspection_c__AllocatorTask_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &task_manager__srv__AllocatorTask_Request__rosidl_typesupport_introspection_c__AllocatorTask_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "task_manager/srv/detail/allocator_task__rosidl_typesupport_introspection_c.h"
// already included above
// #include "task_manager/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "task_manager/srv/detail/allocator_task__functions.h"
// already included above
// #include "task_manager/srv/detail/allocator_task__struct.h"


// Include directives for member types
// Member `robot_name`
// Member `goal_location`
// Member `task_assignment`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void task_manager__srv__AllocatorTask_Response__rosidl_typesupport_introspection_c__AllocatorTask_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  task_manager__srv__AllocatorTask_Response__init(message_memory);
}

void task_manager__srv__AllocatorTask_Response__rosidl_typesupport_introspection_c__AllocatorTask_Response_fini_function(void * message_memory)
{
  task_manager__srv__AllocatorTask_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember task_manager__srv__AllocatorTask_Response__rosidl_typesupport_introspection_c__AllocatorTask_Response_message_member_array[3] = {
  {
    "robot_name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager__srv__AllocatorTask_Response, robot_name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "goal_location",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager__srv__AllocatorTask_Response, goal_location),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "task_assignment",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task_manager__srv__AllocatorTask_Response, task_assignment),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers task_manager__srv__AllocatorTask_Response__rosidl_typesupport_introspection_c__AllocatorTask_Response_message_members = {
  "task_manager__srv",  // message namespace
  "AllocatorTask_Response",  // message name
  3,  // number of fields
  sizeof(task_manager__srv__AllocatorTask_Response),
  task_manager__srv__AllocatorTask_Response__rosidl_typesupport_introspection_c__AllocatorTask_Response_message_member_array,  // message members
  task_manager__srv__AllocatorTask_Response__rosidl_typesupport_introspection_c__AllocatorTask_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  task_manager__srv__AllocatorTask_Response__rosidl_typesupport_introspection_c__AllocatorTask_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t task_manager__srv__AllocatorTask_Response__rosidl_typesupport_introspection_c__AllocatorTask_Response_message_type_support_handle = {
  0,
  &task_manager__srv__AllocatorTask_Response__rosidl_typesupport_introspection_c__AllocatorTask_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_task_manager
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task_manager, srv, AllocatorTask_Response)() {
  if (!task_manager__srv__AllocatorTask_Response__rosidl_typesupport_introspection_c__AllocatorTask_Response_message_type_support_handle.typesupport_identifier) {
    task_manager__srv__AllocatorTask_Response__rosidl_typesupport_introspection_c__AllocatorTask_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &task_manager__srv__AllocatorTask_Response__rosidl_typesupport_introspection_c__AllocatorTask_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "task_manager/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "task_manager/srv/detail/allocator_task__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers task_manager__srv__detail__allocator_task__rosidl_typesupport_introspection_c__AllocatorTask_service_members = {
  "task_manager__srv",  // service namespace
  "AllocatorTask",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // task_manager__srv__detail__allocator_task__rosidl_typesupport_introspection_c__AllocatorTask_Request_message_type_support_handle,
  NULL  // response message
  // task_manager__srv__detail__allocator_task__rosidl_typesupport_introspection_c__AllocatorTask_Response_message_type_support_handle
};

static rosidl_service_type_support_t task_manager__srv__detail__allocator_task__rosidl_typesupport_introspection_c__AllocatorTask_service_type_support_handle = {
  0,
  &task_manager__srv__detail__allocator_task__rosidl_typesupport_introspection_c__AllocatorTask_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task_manager, srv, AllocatorTask_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task_manager, srv, AllocatorTask_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_task_manager
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task_manager, srv, AllocatorTask)() {
  if (!task_manager__srv__detail__allocator_task__rosidl_typesupport_introspection_c__AllocatorTask_service_type_support_handle.typesupport_identifier) {
    task_manager__srv__detail__allocator_task__rosidl_typesupport_introspection_c__AllocatorTask_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)task_manager__srv__detail__allocator_task__rosidl_typesupport_introspection_c__AllocatorTask_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task_manager, srv, AllocatorTask_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task_manager, srv, AllocatorTask_Response)()->data;
  }

  return &task_manager__srv__detail__allocator_task__rosidl_typesupport_introspection_c__AllocatorTask_service_type_support_handle;
}
