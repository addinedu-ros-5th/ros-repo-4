// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from task_manager:srv/GenerateOrder.idl
// generated code does not contain a copyright notice
#include "task_manager/srv/detail/generate_order__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
task_manager__srv__GenerateOrder_Request__init(task_manager__srv__GenerateOrder_Request * msg)
{
  if (!msg) {
    return false;
  }
  // structure_needs_at_least_one_member
  return true;
}

void
task_manager__srv__GenerateOrder_Request__fini(task_manager__srv__GenerateOrder_Request * msg)
{
  if (!msg) {
    return;
  }
  // structure_needs_at_least_one_member
}

bool
task_manager__srv__GenerateOrder_Request__are_equal(const task_manager__srv__GenerateOrder_Request * lhs, const task_manager__srv__GenerateOrder_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // structure_needs_at_least_one_member
  if (lhs->structure_needs_at_least_one_member != rhs->structure_needs_at_least_one_member) {
    return false;
  }
  return true;
}

bool
task_manager__srv__GenerateOrder_Request__copy(
  const task_manager__srv__GenerateOrder_Request * input,
  task_manager__srv__GenerateOrder_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // structure_needs_at_least_one_member
  output->structure_needs_at_least_one_member = input->structure_needs_at_least_one_member;
  return true;
}

task_manager__srv__GenerateOrder_Request *
task_manager__srv__GenerateOrder_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  task_manager__srv__GenerateOrder_Request * msg = (task_manager__srv__GenerateOrder_Request *)allocator.allocate(sizeof(task_manager__srv__GenerateOrder_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(task_manager__srv__GenerateOrder_Request));
  bool success = task_manager__srv__GenerateOrder_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
task_manager__srv__GenerateOrder_Request__destroy(task_manager__srv__GenerateOrder_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    task_manager__srv__GenerateOrder_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
task_manager__srv__GenerateOrder_Request__Sequence__init(task_manager__srv__GenerateOrder_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  task_manager__srv__GenerateOrder_Request * data = NULL;

  if (size) {
    data = (task_manager__srv__GenerateOrder_Request *)allocator.zero_allocate(size, sizeof(task_manager__srv__GenerateOrder_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = task_manager__srv__GenerateOrder_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        task_manager__srv__GenerateOrder_Request__fini(&data[i - 1]);
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
task_manager__srv__GenerateOrder_Request__Sequence__fini(task_manager__srv__GenerateOrder_Request__Sequence * array)
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
      task_manager__srv__GenerateOrder_Request__fini(&array->data[i]);
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

task_manager__srv__GenerateOrder_Request__Sequence *
task_manager__srv__GenerateOrder_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  task_manager__srv__GenerateOrder_Request__Sequence * array = (task_manager__srv__GenerateOrder_Request__Sequence *)allocator.allocate(sizeof(task_manager__srv__GenerateOrder_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = task_manager__srv__GenerateOrder_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
task_manager__srv__GenerateOrder_Request__Sequence__destroy(task_manager__srv__GenerateOrder_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    task_manager__srv__GenerateOrder_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
task_manager__srv__GenerateOrder_Request__Sequence__are_equal(const task_manager__srv__GenerateOrder_Request__Sequence * lhs, const task_manager__srv__GenerateOrder_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!task_manager__srv__GenerateOrder_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
task_manager__srv__GenerateOrder_Request__Sequence__copy(
  const task_manager__srv__GenerateOrder_Request__Sequence * input,
  task_manager__srv__GenerateOrder_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(task_manager__srv__GenerateOrder_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    task_manager__srv__GenerateOrder_Request * data =
      (task_manager__srv__GenerateOrder_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!task_manager__srv__GenerateOrder_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          task_manager__srv__GenerateOrder_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!task_manager__srv__GenerateOrder_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


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

bool
task_manager__srv__GenerateOrder_Response__init(task_manager__srv__GenerateOrder_Response * msg)
{
  if (!msg) {
    return false;
  }
  // item_ids
  if (!rosidl_runtime_c__String__Sequence__init(&msg->item_ids, 0)) {
    task_manager__srv__GenerateOrder_Response__fini(msg);
    return false;
  }
  // names
  if (!rosidl_runtime_c__String__Sequence__init(&msg->names, 0)) {
    task_manager__srv__GenerateOrder_Response__fini(msg);
    return false;
  }
  // quantities
  if (!rosidl_runtime_c__int32__Sequence__init(&msg->quantities, 0)) {
    task_manager__srv__GenerateOrder_Response__fini(msg);
    return false;
  }
  // warehouses
  if (!rosidl_runtime_c__String__Sequence__init(&msg->warehouses, 0)) {
    task_manager__srv__GenerateOrder_Response__fini(msg);
    return false;
  }
  // racks
  if (!rosidl_runtime_c__String__Sequence__init(&msg->racks, 0)) {
    task_manager__srv__GenerateOrder_Response__fini(msg);
    return false;
  }
  // cells
  if (!rosidl_runtime_c__String__Sequence__init(&msg->cells, 0)) {
    task_manager__srv__GenerateOrder_Response__fini(msg);
    return false;
  }
  // statuses
  if (!rosidl_runtime_c__String__Sequence__init(&msg->statuses, 0)) {
    task_manager__srv__GenerateOrder_Response__fini(msg);
    return false;
  }
  return true;
}

void
task_manager__srv__GenerateOrder_Response__fini(task_manager__srv__GenerateOrder_Response * msg)
{
  if (!msg) {
    return;
  }
  // item_ids
  rosidl_runtime_c__String__Sequence__fini(&msg->item_ids);
  // names
  rosidl_runtime_c__String__Sequence__fini(&msg->names);
  // quantities
  rosidl_runtime_c__int32__Sequence__fini(&msg->quantities);
  // warehouses
  rosidl_runtime_c__String__Sequence__fini(&msg->warehouses);
  // racks
  rosidl_runtime_c__String__Sequence__fini(&msg->racks);
  // cells
  rosidl_runtime_c__String__Sequence__fini(&msg->cells);
  // statuses
  rosidl_runtime_c__String__Sequence__fini(&msg->statuses);
}

bool
task_manager__srv__GenerateOrder_Response__are_equal(const task_manager__srv__GenerateOrder_Response * lhs, const task_manager__srv__GenerateOrder_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // item_ids
  if (!rosidl_runtime_c__String__Sequence__are_equal(
      &(lhs->item_ids), &(rhs->item_ids)))
  {
    return false;
  }
  // names
  if (!rosidl_runtime_c__String__Sequence__are_equal(
      &(lhs->names), &(rhs->names)))
  {
    return false;
  }
  // quantities
  if (!rosidl_runtime_c__int32__Sequence__are_equal(
      &(lhs->quantities), &(rhs->quantities)))
  {
    return false;
  }
  // warehouses
  if (!rosidl_runtime_c__String__Sequence__are_equal(
      &(lhs->warehouses), &(rhs->warehouses)))
  {
    return false;
  }
  // racks
  if (!rosidl_runtime_c__String__Sequence__are_equal(
      &(lhs->racks), &(rhs->racks)))
  {
    return false;
  }
  // cells
  if (!rosidl_runtime_c__String__Sequence__are_equal(
      &(lhs->cells), &(rhs->cells)))
  {
    return false;
  }
  // statuses
  if (!rosidl_runtime_c__String__Sequence__are_equal(
      &(lhs->statuses), &(rhs->statuses)))
  {
    return false;
  }
  return true;
}

bool
task_manager__srv__GenerateOrder_Response__copy(
  const task_manager__srv__GenerateOrder_Response * input,
  task_manager__srv__GenerateOrder_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // item_ids
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->item_ids), &(output->item_ids)))
  {
    return false;
  }
  // names
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->names), &(output->names)))
  {
    return false;
  }
  // quantities
  if (!rosidl_runtime_c__int32__Sequence__copy(
      &(input->quantities), &(output->quantities)))
  {
    return false;
  }
  // warehouses
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->warehouses), &(output->warehouses)))
  {
    return false;
  }
  // racks
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->racks), &(output->racks)))
  {
    return false;
  }
  // cells
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->cells), &(output->cells)))
  {
    return false;
  }
  // statuses
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->statuses), &(output->statuses)))
  {
    return false;
  }
  return true;
}

task_manager__srv__GenerateOrder_Response *
task_manager__srv__GenerateOrder_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  task_manager__srv__GenerateOrder_Response * msg = (task_manager__srv__GenerateOrder_Response *)allocator.allocate(sizeof(task_manager__srv__GenerateOrder_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(task_manager__srv__GenerateOrder_Response));
  bool success = task_manager__srv__GenerateOrder_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
task_manager__srv__GenerateOrder_Response__destroy(task_manager__srv__GenerateOrder_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    task_manager__srv__GenerateOrder_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
task_manager__srv__GenerateOrder_Response__Sequence__init(task_manager__srv__GenerateOrder_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  task_manager__srv__GenerateOrder_Response * data = NULL;

  if (size) {
    data = (task_manager__srv__GenerateOrder_Response *)allocator.zero_allocate(size, sizeof(task_manager__srv__GenerateOrder_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = task_manager__srv__GenerateOrder_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        task_manager__srv__GenerateOrder_Response__fini(&data[i - 1]);
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
task_manager__srv__GenerateOrder_Response__Sequence__fini(task_manager__srv__GenerateOrder_Response__Sequence * array)
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
      task_manager__srv__GenerateOrder_Response__fini(&array->data[i]);
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

task_manager__srv__GenerateOrder_Response__Sequence *
task_manager__srv__GenerateOrder_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  task_manager__srv__GenerateOrder_Response__Sequence * array = (task_manager__srv__GenerateOrder_Response__Sequence *)allocator.allocate(sizeof(task_manager__srv__GenerateOrder_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = task_manager__srv__GenerateOrder_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
task_manager__srv__GenerateOrder_Response__Sequence__destroy(task_manager__srv__GenerateOrder_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    task_manager__srv__GenerateOrder_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
task_manager__srv__GenerateOrder_Response__Sequence__are_equal(const task_manager__srv__GenerateOrder_Response__Sequence * lhs, const task_manager__srv__GenerateOrder_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!task_manager__srv__GenerateOrder_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
task_manager__srv__GenerateOrder_Response__Sequence__copy(
  const task_manager__srv__GenerateOrder_Response__Sequence * input,
  task_manager__srv__GenerateOrder_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(task_manager__srv__GenerateOrder_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    task_manager__srv__GenerateOrder_Response * data =
      (task_manager__srv__GenerateOrder_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!task_manager__srv__GenerateOrder_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          task_manager__srv__GenerateOrder_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!task_manager__srv__GenerateOrder_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
