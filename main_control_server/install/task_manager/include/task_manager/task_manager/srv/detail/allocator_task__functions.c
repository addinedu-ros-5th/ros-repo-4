// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from task_manager:srv/AllocatorTask.idl
// generated code does not contain a copyright notice
#include "task_manager/srv/detail/allocator_task__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `product_code`
// Member `task_type`
#include "rosidl_runtime_c/string_functions.h"

bool
task_manager__srv__AllocatorTask_Request__init(task_manager__srv__AllocatorTask_Request * msg)
{
  if (!msg) {
    return false;
  }
  // product_code
  if (!rosidl_runtime_c__String__init(&msg->product_code)) {
    task_manager__srv__AllocatorTask_Request__fini(msg);
    return false;
  }
  // task_type
  if (!rosidl_runtime_c__String__init(&msg->task_type)) {
    task_manager__srv__AllocatorTask_Request__fini(msg);
    return false;
  }
  return true;
}

void
task_manager__srv__AllocatorTask_Request__fini(task_manager__srv__AllocatorTask_Request * msg)
{
  if (!msg) {
    return;
  }
  // product_code
  rosidl_runtime_c__String__fini(&msg->product_code);
  // task_type
  rosidl_runtime_c__String__fini(&msg->task_type);
}

bool
task_manager__srv__AllocatorTask_Request__are_equal(const task_manager__srv__AllocatorTask_Request * lhs, const task_manager__srv__AllocatorTask_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // product_code
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->product_code), &(rhs->product_code)))
  {
    return false;
  }
  // task_type
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->task_type), &(rhs->task_type)))
  {
    return false;
  }
  return true;
}

bool
task_manager__srv__AllocatorTask_Request__copy(
  const task_manager__srv__AllocatorTask_Request * input,
  task_manager__srv__AllocatorTask_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // product_code
  if (!rosidl_runtime_c__String__copy(
      &(input->product_code), &(output->product_code)))
  {
    return false;
  }
  // task_type
  if (!rosidl_runtime_c__String__copy(
      &(input->task_type), &(output->task_type)))
  {
    return false;
  }
  return true;
}

task_manager__srv__AllocatorTask_Request *
task_manager__srv__AllocatorTask_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  task_manager__srv__AllocatorTask_Request * msg = (task_manager__srv__AllocatorTask_Request *)allocator.allocate(sizeof(task_manager__srv__AllocatorTask_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(task_manager__srv__AllocatorTask_Request));
  bool success = task_manager__srv__AllocatorTask_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
task_manager__srv__AllocatorTask_Request__destroy(task_manager__srv__AllocatorTask_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    task_manager__srv__AllocatorTask_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
task_manager__srv__AllocatorTask_Request__Sequence__init(task_manager__srv__AllocatorTask_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  task_manager__srv__AllocatorTask_Request * data = NULL;

  if (size) {
    data = (task_manager__srv__AllocatorTask_Request *)allocator.zero_allocate(size, sizeof(task_manager__srv__AllocatorTask_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = task_manager__srv__AllocatorTask_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        task_manager__srv__AllocatorTask_Request__fini(&data[i - 1]);
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
task_manager__srv__AllocatorTask_Request__Sequence__fini(task_manager__srv__AllocatorTask_Request__Sequence * array)
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
      task_manager__srv__AllocatorTask_Request__fini(&array->data[i]);
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

task_manager__srv__AllocatorTask_Request__Sequence *
task_manager__srv__AllocatorTask_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  task_manager__srv__AllocatorTask_Request__Sequence * array = (task_manager__srv__AllocatorTask_Request__Sequence *)allocator.allocate(sizeof(task_manager__srv__AllocatorTask_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = task_manager__srv__AllocatorTask_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
task_manager__srv__AllocatorTask_Request__Sequence__destroy(task_manager__srv__AllocatorTask_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    task_manager__srv__AllocatorTask_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
task_manager__srv__AllocatorTask_Request__Sequence__are_equal(const task_manager__srv__AllocatorTask_Request__Sequence * lhs, const task_manager__srv__AllocatorTask_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!task_manager__srv__AllocatorTask_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
task_manager__srv__AllocatorTask_Request__Sequence__copy(
  const task_manager__srv__AllocatorTask_Request__Sequence * input,
  task_manager__srv__AllocatorTask_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(task_manager__srv__AllocatorTask_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    task_manager__srv__AllocatorTask_Request * data =
      (task_manager__srv__AllocatorTask_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!task_manager__srv__AllocatorTask_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          task_manager__srv__AllocatorTask_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!task_manager__srv__AllocatorTask_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `robot_name`
// Member `goal_location`
// Member `task_assignment`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

bool
task_manager__srv__AllocatorTask_Response__init(task_manager__srv__AllocatorTask_Response * msg)
{
  if (!msg) {
    return false;
  }
  // robot_name
  if (!rosidl_runtime_c__String__init(&msg->robot_name)) {
    task_manager__srv__AllocatorTask_Response__fini(msg);
    return false;
  }
  // goal_location
  if (!rosidl_runtime_c__String__init(&msg->goal_location)) {
    task_manager__srv__AllocatorTask_Response__fini(msg);
    return false;
  }
  // task_assignment
  if (!rosidl_runtime_c__String__init(&msg->task_assignment)) {
    task_manager__srv__AllocatorTask_Response__fini(msg);
    return false;
  }
  return true;
}

void
task_manager__srv__AllocatorTask_Response__fini(task_manager__srv__AllocatorTask_Response * msg)
{
  if (!msg) {
    return;
  }
  // robot_name
  rosidl_runtime_c__String__fini(&msg->robot_name);
  // goal_location
  rosidl_runtime_c__String__fini(&msg->goal_location);
  // task_assignment
  rosidl_runtime_c__String__fini(&msg->task_assignment);
}

bool
task_manager__srv__AllocatorTask_Response__are_equal(const task_manager__srv__AllocatorTask_Response * lhs, const task_manager__srv__AllocatorTask_Response * rhs)
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
  // goal_location
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->goal_location), &(rhs->goal_location)))
  {
    return false;
  }
  // task_assignment
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->task_assignment), &(rhs->task_assignment)))
  {
    return false;
  }
  return true;
}

bool
task_manager__srv__AllocatorTask_Response__copy(
  const task_manager__srv__AllocatorTask_Response * input,
  task_manager__srv__AllocatorTask_Response * output)
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
  // goal_location
  if (!rosidl_runtime_c__String__copy(
      &(input->goal_location), &(output->goal_location)))
  {
    return false;
  }
  // task_assignment
  if (!rosidl_runtime_c__String__copy(
      &(input->task_assignment), &(output->task_assignment)))
  {
    return false;
  }
  return true;
}

task_manager__srv__AllocatorTask_Response *
task_manager__srv__AllocatorTask_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  task_manager__srv__AllocatorTask_Response * msg = (task_manager__srv__AllocatorTask_Response *)allocator.allocate(sizeof(task_manager__srv__AllocatorTask_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(task_manager__srv__AllocatorTask_Response));
  bool success = task_manager__srv__AllocatorTask_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
task_manager__srv__AllocatorTask_Response__destroy(task_manager__srv__AllocatorTask_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    task_manager__srv__AllocatorTask_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
task_manager__srv__AllocatorTask_Response__Sequence__init(task_manager__srv__AllocatorTask_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  task_manager__srv__AllocatorTask_Response * data = NULL;

  if (size) {
    data = (task_manager__srv__AllocatorTask_Response *)allocator.zero_allocate(size, sizeof(task_manager__srv__AllocatorTask_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = task_manager__srv__AllocatorTask_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        task_manager__srv__AllocatorTask_Response__fini(&data[i - 1]);
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
task_manager__srv__AllocatorTask_Response__Sequence__fini(task_manager__srv__AllocatorTask_Response__Sequence * array)
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
      task_manager__srv__AllocatorTask_Response__fini(&array->data[i]);
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

task_manager__srv__AllocatorTask_Response__Sequence *
task_manager__srv__AllocatorTask_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  task_manager__srv__AllocatorTask_Response__Sequence * array = (task_manager__srv__AllocatorTask_Response__Sequence *)allocator.allocate(sizeof(task_manager__srv__AllocatorTask_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = task_manager__srv__AllocatorTask_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
task_manager__srv__AllocatorTask_Response__Sequence__destroy(task_manager__srv__AllocatorTask_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    task_manager__srv__AllocatorTask_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
task_manager__srv__AllocatorTask_Response__Sequence__are_equal(const task_manager__srv__AllocatorTask_Response__Sequence * lhs, const task_manager__srv__AllocatorTask_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!task_manager__srv__AllocatorTask_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
task_manager__srv__AllocatorTask_Response__Sequence__copy(
  const task_manager__srv__AllocatorTask_Response__Sequence * input,
  task_manager__srv__AllocatorTask_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(task_manager__srv__AllocatorTask_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    task_manager__srv__AllocatorTask_Response * data =
      (task_manager__srv__AllocatorTask_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!task_manager__srv__AllocatorTask_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          task_manager__srv__AllocatorTask_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!task_manager__srv__AllocatorTask_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
