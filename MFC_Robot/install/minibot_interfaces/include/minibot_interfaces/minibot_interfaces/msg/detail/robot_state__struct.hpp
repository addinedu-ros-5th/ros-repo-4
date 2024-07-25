// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from minibot_interfaces:msg/RobotState.idl
// generated code does not contain a copyright notice

#ifndef MINIBOT_INTERFACES__MSG__DETAIL__ROBOT_STATE__STRUCT_HPP_
#define MINIBOT_INTERFACES__MSG__DETAIL__ROBOT_STATE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__minibot_interfaces__msg__RobotState __attribute__((deprecated))
#else
# define DEPRECATED__minibot_interfaces__msg__RobotState __declspec(deprecated)
#endif

namespace minibot_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct RobotState_
{
  using Type = RobotState_<ContainerAllocator>;

  explicit RobotState_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->enable_motor = false;
      this->left_lamp = 0;
      this->right_lamp = 0;
    }
  }

  explicit RobotState_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->enable_motor = false;
      this->left_lamp = 0;
      this->right_lamp = 0;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _enable_motor_type =
    bool;
  _enable_motor_type enable_motor;
  using _left_lamp_type =
    uint8_t;
  _left_lamp_type left_lamp;
  using _right_lamp_type =
    uint8_t;
  _right_lamp_type right_lamp;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__enable_motor(
    const bool & _arg)
  {
    this->enable_motor = _arg;
    return *this;
  }
  Type & set__left_lamp(
    const uint8_t & _arg)
  {
    this->left_lamp = _arg;
    return *this;
  }
  Type & set__right_lamp(
    const uint8_t & _arg)
  {
    this->right_lamp = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    minibot_interfaces::msg::RobotState_<ContainerAllocator> *;
  using ConstRawPtr =
    const minibot_interfaces::msg::RobotState_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<minibot_interfaces::msg::RobotState_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<minibot_interfaces::msg::RobotState_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      minibot_interfaces::msg::RobotState_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<minibot_interfaces::msg::RobotState_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      minibot_interfaces::msg::RobotState_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<minibot_interfaces::msg::RobotState_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<minibot_interfaces::msg::RobotState_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<minibot_interfaces::msg::RobotState_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__minibot_interfaces__msg__RobotState
    std::shared_ptr<minibot_interfaces::msg::RobotState_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__minibot_interfaces__msg__RobotState
    std::shared_ptr<minibot_interfaces::msg::RobotState_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotState_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->enable_motor != other.enable_motor) {
      return false;
    }
    if (this->left_lamp != other.left_lamp) {
      return false;
    }
    if (this->right_lamp != other.right_lamp) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotState_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotState_

// alias to use template instance with default allocator
using RobotState =
  minibot_interfaces::msg::RobotState_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace minibot_interfaces

#endif  // MINIBOT_INTERFACES__MSG__DETAIL__ROBOT_STATE__STRUCT_HPP_
