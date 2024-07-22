// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from task_manager:msg/StartInspection.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__MSG__DETAIL__START_INSPECTION__STRUCT_HPP_
#define TASK_MANAGER__MSG__DETAIL__START_INSPECTION__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__task_manager__msg__StartInspection __attribute__((deprecated))
#else
# define DEPRECATED__task_manager__msg__StartInspection __declspec(deprecated)
#endif

namespace task_manager
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct StartInspection_
{
  using Type = StartInspection_<ContainerAllocator>;

  explicit StartInspection_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->signal = "";
    }
  }

  explicit StartInspection_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : signal(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->signal = "";
    }
  }

  // field types and members
  using _signal_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _signal_type signal;

  // setters for named parameter idiom
  Type & set__signal(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->signal = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    task_manager::msg::StartInspection_<ContainerAllocator> *;
  using ConstRawPtr =
    const task_manager::msg::StartInspection_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<task_manager::msg::StartInspection_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<task_manager::msg::StartInspection_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      task_manager::msg::StartInspection_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<task_manager::msg::StartInspection_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      task_manager::msg::StartInspection_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<task_manager::msg::StartInspection_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<task_manager::msg::StartInspection_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<task_manager::msg::StartInspection_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__task_manager__msg__StartInspection
    std::shared_ptr<task_manager::msg::StartInspection_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__task_manager__msg__StartInspection
    std::shared_ptr<task_manager::msg::StartInspection_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const StartInspection_ & other) const
  {
    if (this->signal != other.signal) {
      return false;
    }
    return true;
  }
  bool operator!=(const StartInspection_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct StartInspection_

// alias to use template instance with default allocator
using StartInspection =
  task_manager::msg::StartInspection_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace task_manager

#endif  // TASK_MANAGER__MSG__DETAIL__START_INSPECTION__STRUCT_HPP_
