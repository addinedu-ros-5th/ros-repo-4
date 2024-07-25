// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from minibot_interfaces:msg/LampCommand.idl
// generated code does not contain a copyright notice

#ifndef MINIBOT_INTERFACES__MSG__DETAIL__LAMP_COMMAND__STRUCT_HPP_
#define MINIBOT_INTERFACES__MSG__DETAIL__LAMP_COMMAND__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__minibot_interfaces__msg__LampCommand __attribute__((deprecated))
#else
# define DEPRECATED__minibot_interfaces__msg__LampCommand __declspec(deprecated)
#endif

namespace minibot_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct LampCommand_
{
  using Type = LampCommand_<ContainerAllocator>;

  explicit LampCommand_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->l_command = 0;
      this->r_command = 0;
    }
  }

  explicit LampCommand_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->l_command = 0;
      this->r_command = 0;
    }
  }

  // field types and members
  using _l_command_type =
    uint8_t;
  _l_command_type l_command;
  using _r_command_type =
    uint8_t;
  _r_command_type r_command;

  // setters for named parameter idiom
  Type & set__l_command(
    const uint8_t & _arg)
  {
    this->l_command = _arg;
    return *this;
  }
  Type & set__r_command(
    const uint8_t & _arg)
  {
    this->r_command = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    minibot_interfaces::msg::LampCommand_<ContainerAllocator> *;
  using ConstRawPtr =
    const minibot_interfaces::msg::LampCommand_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<minibot_interfaces::msg::LampCommand_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<minibot_interfaces::msg::LampCommand_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      minibot_interfaces::msg::LampCommand_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<minibot_interfaces::msg::LampCommand_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      minibot_interfaces::msg::LampCommand_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<minibot_interfaces::msg::LampCommand_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<minibot_interfaces::msg::LampCommand_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<minibot_interfaces::msg::LampCommand_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__minibot_interfaces__msg__LampCommand
    std::shared_ptr<minibot_interfaces::msg::LampCommand_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__minibot_interfaces__msg__LampCommand
    std::shared_ptr<minibot_interfaces::msg::LampCommand_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const LampCommand_ & other) const
  {
    if (this->l_command != other.l_command) {
      return false;
    }
    if (this->r_command != other.r_command) {
      return false;
    }
    return true;
  }
  bool operator!=(const LampCommand_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct LampCommand_

// alias to use template instance with default allocator
using LampCommand =
  minibot_interfaces::msg::LampCommand_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace minibot_interfaces

#endif  // MINIBOT_INTERFACES__MSG__DETAIL__LAMP_COMMAND__STRUCT_HPP_
