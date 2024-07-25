// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from task_manager:msg/InspectionComplete.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__MSG__DETAIL__INSPECTION_COMPLETE__STRUCT_HPP_
#define TASK_MANAGER__MSG__DETAIL__INSPECTION_COMPLETE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__task_manager__msg__InspectionComplete __attribute__((deprecated))
#else
# define DEPRECATED__task_manager__msg__InspectionComplete __declspec(deprecated)
#endif

namespace task_manager
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct InspectionComplete_
{
  using Type = InspectionComplete_<ContainerAllocator>;

  explicit InspectionComplete_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->product_code = "";
    }
  }

  explicit InspectionComplete_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : product_code(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->product_code = "";
    }
  }

  // field types and members
  using _product_code_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _product_code_type product_code;

  // setters for named parameter idiom
  Type & set__product_code(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->product_code = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    task_manager::msg::InspectionComplete_<ContainerAllocator> *;
  using ConstRawPtr =
    const task_manager::msg::InspectionComplete_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<task_manager::msg::InspectionComplete_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<task_manager::msg::InspectionComplete_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      task_manager::msg::InspectionComplete_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<task_manager::msg::InspectionComplete_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      task_manager::msg::InspectionComplete_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<task_manager::msg::InspectionComplete_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<task_manager::msg::InspectionComplete_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<task_manager::msg::InspectionComplete_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__task_manager__msg__InspectionComplete
    std::shared_ptr<task_manager::msg::InspectionComplete_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__task_manager__msg__InspectionComplete
    std::shared_ptr<task_manager::msg::InspectionComplete_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const InspectionComplete_ & other) const
  {
    if (this->product_code != other.product_code) {
      return false;
    }
    return true;
  }
  bool operator!=(const InspectionComplete_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct InspectionComplete_

// alias to use template instance with default allocator
using InspectionComplete =
  task_manager::msg::InspectionComplete_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace task_manager

#endif  // TASK_MANAGER__MSG__DETAIL__INSPECTION_COMPLETE__STRUCT_HPP_
