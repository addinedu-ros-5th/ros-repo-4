// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from task_manager:srv/AllocatorTask.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__SRV__DETAIL__ALLOCATOR_TASK__STRUCT_HPP_
#define TASK_MANAGER__SRV__DETAIL__ALLOCATOR_TASK__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__task_manager__srv__AllocatorTask_Request __attribute__((deprecated))
#else
# define DEPRECATED__task_manager__srv__AllocatorTask_Request __declspec(deprecated)
#endif

namespace task_manager
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AllocatorTask_Request_
{
  using Type = AllocatorTask_Request_<ContainerAllocator>;

  explicit AllocatorTask_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->product_code = "";
      this->task_type = "";
    }
  }

  explicit AllocatorTask_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : product_code(_alloc),
    task_type(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->product_code = "";
      this->task_type = "";
    }
  }

  // field types and members
  using _product_code_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _product_code_type product_code;
  using _task_type_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _task_type_type task_type;

  // setters for named parameter idiom
  Type & set__product_code(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->product_code = _arg;
    return *this;
  }
  Type & set__task_type(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->task_type = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    task_manager::srv::AllocatorTask_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const task_manager::srv::AllocatorTask_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<task_manager::srv::AllocatorTask_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<task_manager::srv::AllocatorTask_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      task_manager::srv::AllocatorTask_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<task_manager::srv::AllocatorTask_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      task_manager::srv::AllocatorTask_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<task_manager::srv::AllocatorTask_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<task_manager::srv::AllocatorTask_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<task_manager::srv::AllocatorTask_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__task_manager__srv__AllocatorTask_Request
    std::shared_ptr<task_manager::srv::AllocatorTask_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__task_manager__srv__AllocatorTask_Request
    std::shared_ptr<task_manager::srv::AllocatorTask_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AllocatorTask_Request_ & other) const
  {
    if (this->product_code != other.product_code) {
      return false;
    }
    if (this->task_type != other.task_type) {
      return false;
    }
    return true;
  }
  bool operator!=(const AllocatorTask_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AllocatorTask_Request_

// alias to use template instance with default allocator
using AllocatorTask_Request =
  task_manager::srv::AllocatorTask_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace task_manager


#ifndef _WIN32
# define DEPRECATED__task_manager__srv__AllocatorTask_Response __attribute__((deprecated))
#else
# define DEPRECATED__task_manager__srv__AllocatorTask_Response __declspec(deprecated)
#endif

namespace task_manager
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AllocatorTask_Response_
{
  using Type = AllocatorTask_Response_<ContainerAllocator>;

  explicit AllocatorTask_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_name = "";
      this->goal_location = "";
      this->task_assignment = "";
    }
  }

  explicit AllocatorTask_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    task_manager::srv::AllocatorTask_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const task_manager::srv::AllocatorTask_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<task_manager::srv::AllocatorTask_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<task_manager::srv::AllocatorTask_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      task_manager::srv::AllocatorTask_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<task_manager::srv::AllocatorTask_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      task_manager::srv::AllocatorTask_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<task_manager::srv::AllocatorTask_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<task_manager::srv::AllocatorTask_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<task_manager::srv::AllocatorTask_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__task_manager__srv__AllocatorTask_Response
    std::shared_ptr<task_manager::srv::AllocatorTask_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__task_manager__srv__AllocatorTask_Response
    std::shared_ptr<task_manager::srv::AllocatorTask_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AllocatorTask_Response_ & other) const
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
  bool operator!=(const AllocatorTask_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AllocatorTask_Response_

// alias to use template instance with default allocator
using AllocatorTask_Response =
  task_manager::srv::AllocatorTask_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace task_manager

namespace task_manager
{

namespace srv
{

struct AllocatorTask
{
  using Request = task_manager::srv::AllocatorTask_Request;
  using Response = task_manager::srv::AllocatorTask_Response;
};

}  // namespace srv

}  // namespace task_manager

#endif  // TASK_MANAGER__SRV__DETAIL__ALLOCATOR_TASK__STRUCT_HPP_
