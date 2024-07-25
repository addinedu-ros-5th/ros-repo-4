// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from robot_state:srv/UpdateDB.idl
// generated code does not contain a copyright notice
#include "robot_state/srv/detail/update_db__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `robot_name`
#include "rosidl_runtime_c/string_functions.h"

bool
robot_state__srv__UpdateDB_Request__init(robot_state__srv__UpdateDB_Request * msg)
{
  if (!msg) {
    return false;
  }
  // robot_name
  if (!rosidl_runtime_c__String__init(&msg->robot_name)) {
    robot_state__srv__UpdateDB_Request__fini(msg);
    return false;
  }
  return true;
}

void
robot_state__srv__UpdateDB_Request__fini(robot_state__srv__UpdateDB_Request * msg)
{
  if (!msg) {
    return;
  }
  // robot_name
  rosidl_runtime_c__String__fini(&msg->robot_name);
}

bool
robot_state__srv__UpdateDB_Request__are_equal(const robot_state__srv__UpdateDB_Request * lhs, const robot_state__srv__UpdateDB_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // robot_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->robot_name), &(rhs->robot_name)))
  {
    return false;
  }
  return true;
}

bool
robot_state__srv__UpdateDB_Request__copy(
  const robot_state__srv__UpdateDB_Request * input,
  robot_state__srv__UpdateDB_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // robot_name
  if (!rosidl_runtime_c__String__copy(
      &(input->robot_name), &(output->robot_name)))
  {
    return false;
  }
  return true;
}

robot_state__srv__UpdateDB_Request *
robot_state__srv__UpdateDB_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_state__srv__UpdateDB_Request * msg = (robot_state__srv__UpdateDB_Request *)allocator.allocate(sizeof(robot_state__srv__UpdateDB_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(robot_state__srv__UpdateDB_Request));
  bool success = robot_state__srv__UpdateDB_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
robot_state__srv__UpdateDB_Request__destroy(robot_state__srv__UpdateDB_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    robot_state__srv__UpdateDB_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
robot_state__srv__UpdateDB_Request__Sequence__init(robot_state__srv__UpdateDB_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_state__srv__UpdateDB_Request * data = NULL;

  if (size) {
    data = (robot_state__srv__UpdateDB_Request *)allocator.zero_allocate(size, sizeof(robot_state__srv__UpdateDB_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = robot_state__srv__UpdateDB_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        robot_state__srv__UpdateDB_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
robot_state__srv__UpdateDB_Request__Sequence__fini(robot_state__srv__UpdateDB_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      robot_state__srv__UpdateDB_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

robot_state__srv__UpdateDB_Request__Sequence *
robot_state__srv__UpdateDB_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_state__srv__UpdateDB_Request__Sequence * array = (robot_state__srv__UpdateDB_Request__Sequence *)allocator.allocate(sizeof(robot_state__srv__UpdateDB_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = robot_state__srv__UpdateDB_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
robot_state__srv__UpdateDB_Request__Sequence__destroy(robot_state__srv__UpdateDB_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    robot_state__srv__UpdateDB_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
robot_state__srv__UpdateDB_Request__Sequence__are_equal(const robot_state__srv__UpdateDB_Request__Sequence * lhs, const robot_state__srv__UpdateDB_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!robot_state__srv__UpdateDB_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
robot_state__srv__UpdateDB_Request__Sequence__copy(
  const robot_state__srv__UpdateDB_Request__Sequence * input,
  robot_state__srv__UpdateDB_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(robot_state__srv__UpdateDB_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    robot_state__srv__UpdateDB_Request * data =
      (robot_state__srv__UpdateDB_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!robot_state__srv__UpdateDB_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          robot_state__srv__UpdateDB_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!robot_state__srv__UpdateDB_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `robot_name`
// Member `battery_status`
// Member `status`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

bool
robot_state__srv__UpdateDB_Response__init(robot_state__srv__UpdateDB_Response * msg)
{
  if (!msg) {
    return false;
  }
  // robot_name
  if (!rosidl_runtime_c__String__init(&msg->robot_name)) {
    robot_state__srv__UpdateDB_Response__fini(msg);
    return false;
  }
  // battery_status
  if (!rosidl_runtime_c__String__init(&msg->battery_status)) {
    robot_state__srv__UpdateDB_Response__fini(msg);
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__init(&msg->status)) {
    robot_state__srv__UpdateDB_Response__fini(msg);
    return false;
  }
  return true;
}

void
robot_state__srv__UpdateDB_Response__fini(robot_state__srv__UpdateDB_Response * msg)
{
  if (!msg) {
    return;
  }
  // robot_name
  rosidl_runtime_c__String__fini(&msg->robot_name);
  // battery_status
  rosidl_runtime_c__String__fini(&msg->battery_status);
  // status
  rosidl_runtime_c__String__fini(&msg->status);
}

bool
robot_state__srv__UpdateDB_Response__are_equal(const robot_state__srv__UpdateDB_Response * lhs, const robot_state__srv__UpdateDB_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // robot_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->robot_name), &(rhs->robot_name)))
  {
    return false;
  }
  // battery_status
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->battery_status), &(rhs->battery_status)))
  {
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->status), &(rhs->status)))
  {
    return false;
  }
  return true;
}

bool
robot_state__srv__UpdateDB_Response__copy(
  const robot_state__srv__UpdateDB_Response * input,
  robot_state__srv__UpdateDB_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // robot_name
  if (!rosidl_runtime_c__String__copy(
      &(input->robot_name), &(output->robot_name)))
  {
    return false;
  }
  // battery_status
  if (!rosidl_runtime_c__String__copy(
      &(input->battery_status), &(output->battery_status)))
  {
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__copy(
      &(input->status), &(output->status)))
  {
    return false;
  }
  return true;
}

robot_state__srv__UpdateDB_Response *
robot_state__srv__UpdateDB_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_state__srv__UpdateDB_Response * msg = (robot_state__srv__UpdateDB_Response *)allocator.allocate(sizeof(robot_state__srv__UpdateDB_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(robot_state__srv__UpdateDB_Response));
  bool success = robot_state__srv__UpdateDB_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
robot_state__srv__UpdateDB_Response__destroy(robot_state__srv__UpdateDB_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    robot_state__srv__UpdateDB_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
robot_state__srv__UpdateDB_Response__Sequence__init(robot_state__srv__UpdateDB_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_state__srv__UpdateDB_Response * data = NULL;

  if (size) {
    data = (robot_state__srv__UpdateDB_Response *)allocator.zero_allocate(size, sizeof(robot_state__srv__UpdateDB_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = robot_state__srv__UpdateDB_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        robot_state__srv__UpdateDB_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
robot_state__srv__UpdateDB_Response__Sequence__fini(robot_state__srv__UpdateDB_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      robot_state__srv__UpdateDB_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

robot_state__srv__UpdateDB_Response__Sequence *
robot_state__srv__UpdateDB_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_state__srv__UpdateDB_Response__Sequence * array = (robot_state__srv__UpdateDB_Response__Sequence *)allocator.allocate(sizeof(robot_state__srv__UpdateDB_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = robot_state__srv__UpdateDB_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
robot_state__srv__UpdateDB_Response__Sequence__destroy(robot_state__srv__UpdateDB_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    robot_state__srv__UpdateDB_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
robot_state__srv__UpdateDB_Response__Sequence__are_equal(const robot_state__srv__UpdateDB_Response__Sequence * lhs, const robot_state__srv__UpdateDB_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!robot_state__srv__UpdateDB_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
robot_state__srv__UpdateDB_Response__Sequence__copy(
  const robot_state__srv__UpdateDB_Response__Sequence * input,
  robot_state__srv__UpdateDB_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(robot_state__srv__UpdateDB_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    robot_state__srv__UpdateDB_Response * data =
      (robot_state__srv__UpdateDB_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!robot_state__srv__UpdateDB_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          robot_state__srv__UpdateDB_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!robot_state__srv__UpdateDB_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
