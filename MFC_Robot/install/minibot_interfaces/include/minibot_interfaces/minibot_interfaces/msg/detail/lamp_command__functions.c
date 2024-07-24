// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from minibot_interfaces:msg/LampCommand.idl
// generated code does not contain a copyright notice
#include "minibot_interfaces/msg/detail/lamp_command__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
minibot_interfaces__msg__LampCommand__init(minibot_interfaces__msg__LampCommand * msg)
{
  if (!msg) {
    return false;
  }
  // l_command
  // r_command
  return true;
}

void
minibot_interfaces__msg__LampCommand__fini(minibot_interfaces__msg__LampCommand * msg)
{
  if (!msg) {
    return;
  }
  // l_command
  // r_command
}

bool
minibot_interfaces__msg__LampCommand__are_equal(const minibot_interfaces__msg__LampCommand * lhs, const minibot_interfaces__msg__LampCommand * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // l_command
  if (lhs->l_command != rhs->l_command) {
    return false;
  }
  // r_command
  if (lhs->r_command != rhs->r_command) {
    return false;
  }
  return true;
}

bool
minibot_interfaces__msg__LampCommand__copy(
  const minibot_interfaces__msg__LampCommand * input,
  minibot_interfaces__msg__LampCommand * output)
{
  if (!input || !output) {
    return false;
  }
  // l_command
  output->l_command = input->l_command;
  // r_command
  output->r_command = input->r_command;
  return true;
}

minibot_interfaces__msg__LampCommand *
minibot_interfaces__msg__LampCommand__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  minibot_interfaces__msg__LampCommand * msg = (minibot_interfaces__msg__LampCommand *)allocator.allocate(sizeof(minibot_interfaces__msg__LampCommand), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(minibot_interfaces__msg__LampCommand));
  bool success = minibot_interfaces__msg__LampCommand__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
minibot_interfaces__msg__LampCommand__destroy(minibot_interfaces__msg__LampCommand * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    minibot_interfaces__msg__LampCommand__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
minibot_interfaces__msg__LampCommand__Sequence__init(minibot_interfaces__msg__LampCommand__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  minibot_interfaces__msg__LampCommand * data = NULL;

  if (size) {
    data = (minibot_interfaces__msg__LampCommand *)allocator.zero_allocate(size, sizeof(minibot_interfaces__msg__LampCommand), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = minibot_interfaces__msg__LampCommand__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        minibot_interfaces__msg__LampCommand__fini(&data[i - 1]);
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
minibot_interfaces__msg__LampCommand__Sequence__fini(minibot_interfaces__msg__LampCommand__Sequence * array)
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
      minibot_interfaces__msg__LampCommand__fini(&array->data[i]);
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

minibot_interfaces__msg__LampCommand__Sequence *
minibot_interfaces__msg__LampCommand__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  minibot_interfaces__msg__LampCommand__Sequence * array = (minibot_interfaces__msg__LampCommand__Sequence *)allocator.allocate(sizeof(minibot_interfaces__msg__LampCommand__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = minibot_interfaces__msg__LampCommand__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
minibot_interfaces__msg__LampCommand__Sequence__destroy(minibot_interfaces__msg__LampCommand__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    minibot_interfaces__msg__LampCommand__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
minibot_interfaces__msg__LampCommand__Sequence__are_equal(const minibot_interfaces__msg__LampCommand__Sequence * lhs, const minibot_interfaces__msg__LampCommand__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!minibot_interfaces__msg__LampCommand__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
minibot_interfaces__msg__LampCommand__Sequence__copy(
  const minibot_interfaces__msg__LampCommand__Sequence * input,
  minibot_interfaces__msg__LampCommand__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(minibot_interfaces__msg__LampCommand);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    minibot_interfaces__msg__LampCommand * data =
      (minibot_interfaces__msg__LampCommand *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!minibot_interfaces__msg__LampCommand__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          minibot_interfaces__msg__LampCommand__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!minibot_interfaces__msg__LampCommand__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
