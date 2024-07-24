// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from minibot_interfaces:msg/RobotState.idl
// generated code does not contain a copyright notice
#include "minibot_interfaces/msg/detail/robot_state__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
minibot_interfaces__msg__RobotState__init(minibot_interfaces__msg__RobotState * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    minibot_interfaces__msg__RobotState__fini(msg);
    return false;
  }
  // enable_motor
  // left_lamp
  // right_lamp
  return true;
}

void
minibot_interfaces__msg__RobotState__fini(minibot_interfaces__msg__RobotState * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // enable_motor
  // left_lamp
  // right_lamp
}

bool
minibot_interfaces__msg__RobotState__are_equal(const minibot_interfaces__msg__RobotState * lhs, const minibot_interfaces__msg__RobotState * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // enable_motor
  if (lhs->enable_motor != rhs->enable_motor) {
    return false;
  }
  // left_lamp
  if (lhs->left_lamp != rhs->left_lamp) {
    return false;
  }
  // right_lamp
  if (lhs->right_lamp != rhs->right_lamp) {
    return false;
  }
  return true;
}

bool
minibot_interfaces__msg__RobotState__copy(
  const minibot_interfaces__msg__RobotState * input,
  minibot_interfaces__msg__RobotState * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // enable_motor
  output->enable_motor = input->enable_motor;
  // left_lamp
  output->left_lamp = input->left_lamp;
  // right_lamp
  output->right_lamp = input->right_lamp;
  return true;
}

minibot_interfaces__msg__RobotState *
minibot_interfaces__msg__RobotState__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  minibot_interfaces__msg__RobotState * msg = (minibot_interfaces__msg__RobotState *)allocator.allocate(sizeof(minibot_interfaces__msg__RobotState), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(minibot_interfaces__msg__RobotState));
  bool success = minibot_interfaces__msg__RobotState__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
minibot_interfaces__msg__RobotState__destroy(minibot_interfaces__msg__RobotState * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    minibot_interfaces__msg__RobotState__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
minibot_interfaces__msg__RobotState__Sequence__init(minibot_interfaces__msg__RobotState__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  minibot_interfaces__msg__RobotState * data = NULL;

  if (size) {
    data = (minibot_interfaces__msg__RobotState *)allocator.zero_allocate(size, sizeof(minibot_interfaces__msg__RobotState), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = minibot_interfaces__msg__RobotState__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        minibot_interfaces__msg__RobotState__fini(&data[i - 1]);
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
minibot_interfaces__msg__RobotState__Sequence__fini(minibot_interfaces__msg__RobotState__Sequence * array)
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
      minibot_interfaces__msg__RobotState__fini(&array->data[i]);
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

minibot_interfaces__msg__RobotState__Sequence *
minibot_interfaces__msg__RobotState__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  minibot_interfaces__msg__RobotState__Sequence * array = (minibot_interfaces__msg__RobotState__Sequence *)allocator.allocate(sizeof(minibot_interfaces__msg__RobotState__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = minibot_interfaces__msg__RobotState__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
minibot_interfaces__msg__RobotState__Sequence__destroy(minibot_interfaces__msg__RobotState__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    minibot_interfaces__msg__RobotState__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
minibot_interfaces__msg__RobotState__Sequence__are_equal(const minibot_interfaces__msg__RobotState__Sequence * lhs, const minibot_interfaces__msg__RobotState__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!minibot_interfaces__msg__RobotState__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
minibot_interfaces__msg__RobotState__Sequence__copy(
  const minibot_interfaces__msg__RobotState__Sequence * input,
  minibot_interfaces__msg__RobotState__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(minibot_interfaces__msg__RobotState);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    minibot_interfaces__msg__RobotState * data =
      (minibot_interfaces__msg__RobotState *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!minibot_interfaces__msg__RobotState__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          minibot_interfaces__msg__RobotState__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!minibot_interfaces__msg__RobotState__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
