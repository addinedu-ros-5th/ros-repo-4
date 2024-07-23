// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robot_state:srv/UpdateDB.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_STATE__SRV__DETAIL__UPDATE_DB__STRUCT_HPP_
#define ROBOT_STATE__SRV__DETAIL__UPDATE_DB__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__robot_state__srv__UpdateDB_Request __attribute__((deprecated))
#else
# define DEPRECATED__robot_state__srv__UpdateDB_Request __declspec(deprecated)
#endif

namespace robot_state
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct UpdateDB_Request_
{
  using Type = UpdateDB_Request_<ContainerAllocator>;

  explicit UpdateDB_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_name = "";
    }
  }

  explicit UpdateDB_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : robot_name(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_name = "";
    }
  }

  // field types and members
  using _robot_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _robot_name_type robot_name;

  // setters for named parameter idiom
  Type & set__robot_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->robot_name = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_state::srv::UpdateDB_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_state::srv::UpdateDB_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_state::srv::UpdateDB_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_state::srv::UpdateDB_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_state::srv::UpdateDB_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_state::srv::UpdateDB_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_state::srv::UpdateDB_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_state::srv::UpdateDB_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_state::srv::UpdateDB_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_state::srv::UpdateDB_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_state__srv__UpdateDB_Request
    std::shared_ptr<robot_state::srv::UpdateDB_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_state__srv__UpdateDB_Request
    std::shared_ptr<robot_state::srv::UpdateDB_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const UpdateDB_Request_ & other) const
  {
    if (this->robot_name != other.robot_name) {
      return false;
    }
    return true;
  }
  bool operator!=(const UpdateDB_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct UpdateDB_Request_

// alias to use template instance with default allocator
using UpdateDB_Request =
  robot_state::srv::UpdateDB_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace robot_state


#ifndef _WIN32
# define DEPRECATED__robot_state__srv__UpdateDB_Response __attribute__((deprecated))
#else
# define DEPRECATED__robot_state__srv__UpdateDB_Response __declspec(deprecated)
#endif

namespace robot_state
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct UpdateDB_Response_
{
  using Type = UpdateDB_Response_<ContainerAllocator>;

  explicit UpdateDB_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_name = "";
      this->battery_status = "";
      this->status = "";
    }
  }

  explicit UpdateDB_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : robot_name(_alloc),
    battery_status(_alloc),
    status(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_name = "";
      this->battery_status = "";
      this->status = "";
    }
  }

  // field types and members
  using _robot_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _robot_name_type robot_name;
  using _battery_status_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _battery_status_type battery_status;
  using _status_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _status_type status;

  // setters for named parameter idiom
  Type & set__robot_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->robot_name = _arg;
    return *this;
  }
  Type & set__battery_status(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->battery_status = _arg;
    return *this;
  }
  Type & set__status(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->status = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_state::srv::UpdateDB_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_state::srv::UpdateDB_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_state::srv::UpdateDB_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_state::srv::UpdateDB_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_state::srv::UpdateDB_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_state::srv::UpdateDB_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_state::srv::UpdateDB_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_state::srv::UpdateDB_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_state::srv::UpdateDB_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_state::srv::UpdateDB_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_state__srv__UpdateDB_Response
    std::shared_ptr<robot_state::srv::UpdateDB_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_state__srv__UpdateDB_Response
    std::shared_ptr<robot_state::srv::UpdateDB_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const UpdateDB_Response_ & other) const
  {
    if (this->robot_name != other.robot_name) {
      return false;
    }
    if (this->battery_status != other.battery_status) {
      return false;
    }
    if (this->status != other.status) {
      return false;
    }
    return true;
  }
  bool operator!=(const UpdateDB_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct UpdateDB_Response_

// alias to use template instance with default allocator
using UpdateDB_Response =
  robot_state::srv::UpdateDB_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace robot_state

namespace robot_state
{

namespace srv
{

struct UpdateDB
{
  using Request = robot_state::srv::UpdateDB_Request;
  using Response = robot_state::srv::UpdateDB_Response;
};

}  // namespace srv

}  // namespace robot_state

#endif  // ROBOT_STATE__SRV__DETAIL__UPDATE_DB__STRUCT_HPP_
