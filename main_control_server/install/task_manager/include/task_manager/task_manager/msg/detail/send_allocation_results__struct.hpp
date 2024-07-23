// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from task_manager:msg/SendAllocationResults.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__MSG__DETAIL__SEND_ALLOCATION_RESULTS__STRUCT_HPP_
#define TASK_MANAGER__MSG__DETAIL__SEND_ALLOCATION_RESULTS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__task_manager__msg__SendAllocationResults __attribute__((deprecated))
#else
# define DEPRECATED__task_manager__msg__SendAllocationResults __declspec(deprecated)
#endif

namespace task_manager
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct SendAllocationResults_
{
  using Type = SendAllocationResults_<ContainerAllocator>;

  explicit SendAllocationResults_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_name = "";
      this->goal_location = "";
      this->task_assignment = "";
    }
  }

  explicit SendAllocationResults_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : robot_name(_alloc),
    goal_location(_alloc),
    task_assignment(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_name = "";
      this->goal_location = "";
      this->task_assignment = "";
    }
  }

  // field types and members
  using _robot_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _robot_name_type robot_name;
  using _goal_location_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _goal_location_type goal_location;
  using _task_assignment_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _task_assignment_type task_assignment;

  // setters for named parameter idiom
  Type & set__robot_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->robot_name = _arg;
    return *this;
  }
  Type & set__goal_location(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->goal_location = _arg;
    return *this;
  }
  Type & set__task_assignment(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->task_assignment = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    task_manager::msg::SendAllocationResults_<ContainerAllocator> *;
  using ConstRawPtr =
    const task_manager::msg::SendAllocationResults_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<task_manager::msg::SendAllocationResults_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<task_manager::msg::SendAllocationResults_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      task_manager::msg::SendAllocationResults_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<task_manager::msg::SendAllocationResults_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      task_manager::msg::SendAllocationResults_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<task_manager::msg::SendAllocationResults_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<task_manager::msg::SendAllocationResults_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<task_manager::msg::SendAllocationResults_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__task_manager__msg__SendAllocationResults
    std::shared_ptr<task_manager::msg::SendAllocationResults_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__task_manager__msg__SendAllocationResults
    std::shared_ptr<task_manager::msg::SendAllocationResults_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SendAllocationResults_ & other) const
  {
    if (this->robot_name != other.robot_name) {
      return false;
    }
    if (this->goal_location != other.goal_location) {
      return false;
    }
    if (this->task_assignment != other.task_assignment) {
      return false;
    }
    return true;
  }
  bool operator!=(const SendAllocationResults_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SendAllocationResults_

// alias to use template instance with default allocator
using SendAllocationResults =
  task_manager::msg::SendAllocationResults_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace task_manager

#endif  // TASK_MANAGER__MSG__DETAIL__SEND_ALLOCATION_RESULTS__STRUCT_HPP_
