// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from task_manager:msg/SendAllocationResults.idl
// generated code does not contain a copyright notice
#include "task_manager/msg/detail/send_allocation_results__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `robot_name`
// Member `goal_location`
// Member `task_assignment`
#include "rosidl_runtime_c/string_functions.h"

bool
task_manager__msg__SendAllocationResults__init(task_manager__msg__SendAllocationResults * msg)
{
  if (!msg) {
    return false;
  }
  // robot_name
  if (!rosidl_runtime_c__String__init(&msg->robot_name)) {
    task_manager__msg__SendAllocationResults__fini(msg);
    return false;
  }
  // goal_location
  if (!rosidl_runtime_c__String__init(&msg->goal_location)) {
    task_manager__msg__SendAllocationResults__fini(msg);
    return false;
  }
  // task_assignment
  if (!rosidl_runtime_c__String__init(&msg->task_assignment)) {
    task_manager__msg__SendAllocationResults__fini(msg);
    return false;
  }
  return true;
}

void
task_manager__msg__SendAllocationResults__fini(task_manager__msg__SendAllocationResults * msg)
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
task_manager__msg__SendAllocationResults__are_equal(const task_manager__msg__SendAllocationResults * lhs, const task_manager__msg__SendAllocationResults * rhs)
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
task_manager__msg__SendAllocationResults__copy(
  const task_manager__msg__SendAllocationResults * input,
  task_manager__msg__SendAllocationResults * output)
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

task_manager__msg__SendAllocationResults *
task_manager__msg__SendAllocationResults__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  task_manager__msg__SendAllocationResults * msg = (task_manager__msg__SendAllocationResults *)allocator.allocate(sizeof(task_manager__msg__SendAllocationResults), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(task_manager__msg__SendAllocationResults));
  bool success = task_manager__msg__SendAllocationResults__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
task_manager__msg__SendAllocationResults__destroy(task_manager__msg__SendAllocationResults * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    task_manager__msg__SendAllocationResults__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
task_manager__msg__SendAllocationResults__Sequence__init(task_manager__msg__SendAllocationResults__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  task_manager__msg__SendAllocationResults * data = NULL;

  if (size) {
    data = (task_manager__msg__SendAllocationResults *)allocator.zero_allocate(size, sizeof(task_manager__msg__SendAllocationResults), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = task_manager__msg__SendAllocationResults__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        task_manager__msg__SendAllocationResults__fini(&data[i - 1]);
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
task_manager__msg__SendAllocationResults__Sequence__fini(task_manager__msg__SendAllocationResults__Sequence * array)
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
      task_manager__msg__SendAllocationResults__fini(&array->data[i]);
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

task_manager__msg__SendAllocationResults__Sequence *
task_manager__msg__SendAllocationResults__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  task_manager__msg__SendAllocationResults__Sequence * array = (task_manager__msg__SendAllocationResults__Sequence *)allocator.allocate(sizeof(task_manager__msg__SendAllocationResults__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = task_manager__msg__SendAllocationResults__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
task_manager__msg__SendAllocationResults__Sequence__destroy(task_manager__msg__SendAllocationResults__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    task_manager__msg__SendAllocationResults__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
task_manager__msg__SendAllocationResults__Sequence__are_equal(const task_manager__msg__SendAllocationResults__Sequence * lhs, const task_manager__msg__SendAllocationResults__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!task_manager__msg__SendAllocationResults__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
task_manager__msg__SendAllocationResults__Sequence__copy(
  const task_manager__msg__SendAllocationResults__Sequence * input,
  task_manager__msg__SendAllocationResults__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(task_manager__msg__SendAllocationResults);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    task_manager__msg__SendAllocationResults * data =
      (task_manager__msg__SendAllocationResults *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!task_manager__msg__SendAllocationResults__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          task_manager__msg__SendAllocationResults__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!task_manager__msg__SendAllocationResults__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
