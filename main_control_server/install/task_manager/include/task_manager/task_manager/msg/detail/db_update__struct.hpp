// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from task_manager:msg/DbUpdate.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__MSG__DETAIL__DB_UPDATE__STRUCT_HPP_
#define TASK_MANAGER__MSG__DETAIL__DB_UPDATE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__task_manager__msg__DbUpdate __attribute__((deprecated))
#else
# define DEPRECATED__task_manager__msg__DbUpdate __declspec(deprecated)
#endif

namespace task_manager
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct DbUpdate_
{
  using Type = DbUpdate_<ContainerAllocator>;

  explicit DbUpdate_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = "";
    }
  }

  explicit DbUpdate_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : status(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = "";
    }
  }

  // field types and members
  using _status_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _status_type status;

  // setters for named parameter idiom
  Type & set__status(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->status = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    task_manager::msg::DbUpdate_<ContainerAllocator> *;
  using ConstRawPtr =
    const task_manager::msg::DbUpdate_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<task_manager::msg::DbUpdate_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<task_manager::msg::DbUpdate_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      task_manager::msg::DbUpdate_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<task_manager::msg::DbUpdate_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      task_manager::msg::DbUpdate_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<task_manager::msg::DbUpdate_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<task_manager::msg::DbUpdate_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<task_manager::msg::DbUpdate_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__task_manager__msg__DbUpdate
    std::shared_ptr<task_manager::msg::DbUpdate_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__task_manager__msg__DbUpdate
    std::shared_ptr<task_manager::msg::DbUpdate_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DbUpdate_ & other) const
  {
    if (this->status != other.status) {
      return false;
    }
    return true;
  }
  bool operator!=(const DbUpdate_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DbUpdate_

// alias to use template instance with default allocator
using DbUpdate =
  task_manager::msg::DbUpdate_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace task_manager

#endif  // TASK_MANAGER__MSG__DETAIL__DB_UPDATE__STRUCT_HPP_
