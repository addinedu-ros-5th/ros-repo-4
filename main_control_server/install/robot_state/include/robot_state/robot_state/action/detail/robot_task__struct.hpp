// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robot_state:action/RobotTask.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_STATE__ACTION__DETAIL__ROBOT_TASK__STRUCT_HPP_
#define ROBOT_STATE__ACTION__DETAIL__ROBOT_TASK__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__robot_state__action__RobotTask_Goal __attribute__((deprecated))
#else
# define DEPRECATED__robot_state__action__RobotTask_Goal __declspec(deprecated)
#endif

namespace robot_state
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct RobotTask_Goal_
{
  using Type = RobotTask_Goal_<ContainerAllocator>;

  explicit RobotTask_Goal_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->pos_x = 0.0f;
      this->pos_y = 0.0f;
      this->orientation_z = 0.0f;
      this->orientation_w = 0.0f;
    }
  }

  explicit RobotTask_Goal_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->pos_x = 0.0f;
      this->pos_y = 0.0f;
      this->orientation_z = 0.0f;
      this->orientation_w = 0.0f;
    }
  }

  // field types and members
  using _pos_x_type =
    float;
  _pos_x_type pos_x;
  using _pos_y_type =
    float;
  _pos_y_type pos_y;
  using _orientation_z_type =
    float;
  _orientation_z_type orientation_z;
  using _orientation_w_type =
    float;
  _orientation_w_type orientation_w;

  // setters for named parameter idiom
  Type & set__pos_x(
    const float & _arg)
  {
    this->pos_x = _arg;
    return *this;
  }
  Type & set__pos_y(
    const float & _arg)
  {
    this->pos_y = _arg;
    return *this;
  }
  Type & set__orientation_z(
    const float & _arg)
  {
    this->orientation_z = _arg;
    return *this;
  }
  Type & set__orientation_w(
    const float & _arg)
  {
    this->orientation_w = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_state::action::RobotTask_Goal_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_state::action::RobotTask_Goal_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_state::action::RobotTask_Goal_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_state::action::RobotTask_Goal_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_state::action::RobotTask_Goal_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_state::action::RobotTask_Goal_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_state::action::RobotTask_Goal_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_state::action::RobotTask_Goal_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_state::action::RobotTask_Goal_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_state::action::RobotTask_Goal_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_state__action__RobotTask_Goal
    std::shared_ptr<robot_state::action::RobotTask_Goal_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_state__action__RobotTask_Goal
    std::shared_ptr<robot_state::action::RobotTask_Goal_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotTask_Goal_ & other) const
  {
    if (this->pos_x != other.pos_x) {
      return false;
    }
    if (this->pos_y != other.pos_y) {
      return false;
    }
    if (this->orientation_z != other.orientation_z) {
      return false;
    }
    if (this->orientation_w != other.orientation_w) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotTask_Goal_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotTask_Goal_

// alias to use template instance with default allocator
using RobotTask_Goal =
  robot_state::action::RobotTask_Goal_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace robot_state


#ifndef _WIN32
# define DEPRECATED__robot_state__action__RobotTask_Result __attribute__((deprecated))
#else
# define DEPRECATED__robot_state__action__RobotTask_Result __declspec(deprecated)
#endif

namespace robot_state
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct RobotTask_Result_
{
  using Type = RobotTask_Result_<ContainerAllocator>;

  explicit RobotTask_Result_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_name = "";
      this->goal_location = "";
    }
  }

  explicit RobotTask_Result_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : robot_name(_alloc),
    goal_location(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_name = "";
      this->goal_location = "";
    }
  }

  // field types and members
  using _robot_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _robot_name_type robot_name;
  using _goal_location_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _goal_location_type goal_location;

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

  // constant declarations

  // pointer types
  using RawPtr =
    robot_state::action::RobotTask_Result_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_state::action::RobotTask_Result_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_state::action::RobotTask_Result_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_state::action::RobotTask_Result_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_state::action::RobotTask_Result_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_state::action::RobotTask_Result_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_state::action::RobotTask_Result_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_state::action::RobotTask_Result_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_state::action::RobotTask_Result_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_state::action::RobotTask_Result_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_state__action__RobotTask_Result
    std::shared_ptr<robot_state::action::RobotTask_Result_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_state__action__RobotTask_Result
    std::shared_ptr<robot_state::action::RobotTask_Result_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotTask_Result_ & other) const
  {
    if (this->robot_name != other.robot_name) {
      return false;
    }
    if (this->goal_location != other.goal_location) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotTask_Result_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotTask_Result_

// alias to use template instance with default allocator
using RobotTask_Result =
  robot_state::action::RobotTask_Result_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace robot_state


#ifndef _WIN32
# define DEPRECATED__robot_state__action__RobotTask_Feedback __attribute__((deprecated))
#else
# define DEPRECATED__robot_state__action__RobotTask_Feedback __declspec(deprecated)
#endif

namespace robot_state
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct RobotTask_Feedback_
{
  using Type = RobotTask_Feedback_<ContainerAllocator>;

  explicit RobotTask_Feedback_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->remained_dist = 0.0f;
    }
  }

  explicit RobotTask_Feedback_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->remained_dist = 0.0f;
    }
  }

  // field types and members
  using _remained_dist_type =
    float;
  _remained_dist_type remained_dist;

  // setters for named parameter idiom
  Type & set__remained_dist(
    const float & _arg)
  {
    this->remained_dist = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_state::action::RobotTask_Feedback_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_state::action::RobotTask_Feedback_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_state::action::RobotTask_Feedback_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_state::action::RobotTask_Feedback_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_state::action::RobotTask_Feedback_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_state::action::RobotTask_Feedback_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_state::action::RobotTask_Feedback_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_state::action::RobotTask_Feedback_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_state::action::RobotTask_Feedback_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_state::action::RobotTask_Feedback_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_state__action__RobotTask_Feedback
    std::shared_ptr<robot_state::action::RobotTask_Feedback_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_state__action__RobotTask_Feedback
    std::shared_ptr<robot_state::action::RobotTask_Feedback_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotTask_Feedback_ & other) const
  {
    if (this->remained_dist != other.remained_dist) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotTask_Feedback_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotTask_Feedback_

// alias to use template instance with default allocator
using RobotTask_Feedback =
  robot_state::action::RobotTask_Feedback_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace robot_state


// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.hpp"
// Member 'goal'
#include "robot_state/action/detail/robot_task__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__robot_state__action__RobotTask_SendGoal_Request __attribute__((deprecated))
#else
# define DEPRECATED__robot_state__action__RobotTask_SendGoal_Request __declspec(deprecated)
#endif

namespace robot_state
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct RobotTask_SendGoal_Request_
{
  using Type = RobotTask_SendGoal_Request_<ContainerAllocator>;

  explicit RobotTask_SendGoal_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_init),
    goal(_init)
  {
    (void)_init;
  }

  explicit RobotTask_SendGoal_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init),
    goal(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;
  using _goal_type =
    robot_state::action::RobotTask_Goal_<ContainerAllocator>;
  _goal_type goal;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }
  Type & set__goal(
    const robot_state::action::RobotTask_Goal_<ContainerAllocator> & _arg)
  {
    this->goal = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_state::action::RobotTask_SendGoal_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_state::action::RobotTask_SendGoal_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_state::action::RobotTask_SendGoal_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_state::action::RobotTask_SendGoal_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_state::action::RobotTask_SendGoal_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_state::action::RobotTask_SendGoal_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_state::action::RobotTask_SendGoal_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_state::action::RobotTask_SendGoal_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_state::action::RobotTask_SendGoal_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_state::action::RobotTask_SendGoal_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_state__action__RobotTask_SendGoal_Request
    std::shared_ptr<robot_state::action::RobotTask_SendGoal_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_state__action__RobotTask_SendGoal_Request
    std::shared_ptr<robot_state::action::RobotTask_SendGoal_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotTask_SendGoal_Request_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    if (this->goal != other.goal) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotTask_SendGoal_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotTask_SendGoal_Request_

// alias to use template instance with default allocator
using RobotTask_SendGoal_Request =
  robot_state::action::RobotTask_SendGoal_Request_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace robot_state


// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__robot_state__action__RobotTask_SendGoal_Response __attribute__((deprecated))
#else
# define DEPRECATED__robot_state__action__RobotTask_SendGoal_Response __declspec(deprecated)
#endif

namespace robot_state
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct RobotTask_SendGoal_Response_
{
  using Type = RobotTask_SendGoal_Response_<ContainerAllocator>;

  explicit RobotTask_SendGoal_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->accepted = false;
    }
  }

  explicit RobotTask_SendGoal_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->accepted = false;
    }
  }

  // field types and members
  using _accepted_type =
    bool;
  _accepted_type accepted;
  using _stamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _stamp_type stamp;

  // setters for named parameter idiom
  Type & set__accepted(
    const bool & _arg)
  {
    this->accepted = _arg;
    return *this;
  }
  Type & set__stamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->stamp = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_state::action::RobotTask_SendGoal_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_state::action::RobotTask_SendGoal_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_state::action::RobotTask_SendGoal_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_state::action::RobotTask_SendGoal_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_state::action::RobotTask_SendGoal_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_state::action::RobotTask_SendGoal_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_state::action::RobotTask_SendGoal_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_state::action::RobotTask_SendGoal_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_state::action::RobotTask_SendGoal_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_state::action::RobotTask_SendGoal_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_state__action__RobotTask_SendGoal_Response
    std::shared_ptr<robot_state::action::RobotTask_SendGoal_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_state__action__RobotTask_SendGoal_Response
    std::shared_ptr<robot_state::action::RobotTask_SendGoal_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotTask_SendGoal_Response_ & other) const
  {
    if (this->accepted != other.accepted) {
      return false;
    }
    if (this->stamp != other.stamp) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotTask_SendGoal_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotTask_SendGoal_Response_

// alias to use template instance with default allocator
using RobotTask_SendGoal_Response =
  robot_state::action::RobotTask_SendGoal_Response_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace robot_state

namespace robot_state
{

namespace action
{

struct RobotTask_SendGoal
{
  using Request = robot_state::action::RobotTask_SendGoal_Request;
  using Response = robot_state::action::RobotTask_SendGoal_Response;
};

}  // namespace action

}  // namespace robot_state


// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__robot_state__action__RobotTask_GetResult_Request __attribute__((deprecated))
#else
# define DEPRECATED__robot_state__action__RobotTask_GetResult_Request __declspec(deprecated)
#endif

namespace robot_state
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct RobotTask_GetResult_Request_
{
  using Type = RobotTask_GetResult_Request_<ContainerAllocator>;

  explicit RobotTask_GetResult_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_init)
  {
    (void)_init;
  }

  explicit RobotTask_GetResult_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_state::action::RobotTask_GetResult_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_state::action::RobotTask_GetResult_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_state::action::RobotTask_GetResult_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_state::action::RobotTask_GetResult_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_state::action::RobotTask_GetResult_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_state::action::RobotTask_GetResult_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_state::action::RobotTask_GetResult_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_state::action::RobotTask_GetResult_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_state::action::RobotTask_GetResult_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_state::action::RobotTask_GetResult_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_state__action__RobotTask_GetResult_Request
    std::shared_ptr<robot_state::action::RobotTask_GetResult_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_state__action__RobotTask_GetResult_Request
    std::shared_ptr<robot_state::action::RobotTask_GetResult_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotTask_GetResult_Request_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotTask_GetResult_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotTask_GetResult_Request_

// alias to use template instance with default allocator
using RobotTask_GetResult_Request =
  robot_state::action::RobotTask_GetResult_Request_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace robot_state


// Include directives for member types
// Member 'result'
// already included above
// #include "robot_state/action/detail/robot_task__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__robot_state__action__RobotTask_GetResult_Response __attribute__((deprecated))
#else
# define DEPRECATED__robot_state__action__RobotTask_GetResult_Response __declspec(deprecated)
#endif

namespace robot_state
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct RobotTask_GetResult_Response_
{
  using Type = RobotTask_GetResult_Response_<ContainerAllocator>;

  explicit RobotTask_GetResult_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : result(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
    }
  }

  explicit RobotTask_GetResult_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : result(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
    }
  }

  // field types and members
  using _status_type =
    int8_t;
  _status_type status;
  using _result_type =
    robot_state::action::RobotTask_Result_<ContainerAllocator>;
  _result_type result;

  // setters for named parameter idiom
  Type & set__status(
    const int8_t & _arg)
  {
    this->status = _arg;
    return *this;
  }
  Type & set__result(
    const robot_state::action::RobotTask_Result_<ContainerAllocator> & _arg)
  {
    this->result = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_state::action::RobotTask_GetResult_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_state::action::RobotTask_GetResult_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_state::action::RobotTask_GetResult_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_state::action::RobotTask_GetResult_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_state::action::RobotTask_GetResult_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_state::action::RobotTask_GetResult_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_state::action::RobotTask_GetResult_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_state::action::RobotTask_GetResult_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_state::action::RobotTask_GetResult_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_state::action::RobotTask_GetResult_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_state__action__RobotTask_GetResult_Response
    std::shared_ptr<robot_state::action::RobotTask_GetResult_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_state__action__RobotTask_GetResult_Response
    std::shared_ptr<robot_state::action::RobotTask_GetResult_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotTask_GetResult_Response_ & other) const
  {
    if (this->status != other.status) {
      return false;
    }
    if (this->result != other.result) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotTask_GetResult_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotTask_GetResult_Response_

// alias to use template instance with default allocator
using RobotTask_GetResult_Response =
  robot_state::action::RobotTask_GetResult_Response_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace robot_state

namespace robot_state
{

namespace action
{

struct RobotTask_GetResult
{
  using Request = robot_state::action::RobotTask_GetResult_Request;
  using Response = robot_state::action::RobotTask_GetResult_Response;
};

}  // namespace action

}  // namespace robot_state


// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.hpp"
// Member 'feedback'
// already included above
// #include "robot_state/action/detail/robot_task__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__robot_state__action__RobotTask_FeedbackMessage __attribute__((deprecated))
#else
# define DEPRECATED__robot_state__action__RobotTask_FeedbackMessage __declspec(deprecated)
#endif

namespace robot_state
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct RobotTask_FeedbackMessage_
{
  using Type = RobotTask_FeedbackMessage_<ContainerAllocator>;

  explicit RobotTask_FeedbackMessage_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_init),
    feedback(_init)
  {
    (void)_init;
  }

  explicit RobotTask_FeedbackMessage_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init),
    feedback(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;
  using _feedback_type =
    robot_state::action::RobotTask_Feedback_<ContainerAllocator>;
  _feedback_type feedback;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }
  Type & set__feedback(
    const robot_state::action::RobotTask_Feedback_<ContainerAllocator> & _arg)
  {
    this->feedback = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_state::action::RobotTask_FeedbackMessage_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_state::action::RobotTask_FeedbackMessage_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_state::action::RobotTask_FeedbackMessage_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_state::action::RobotTask_FeedbackMessage_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_state::action::RobotTask_FeedbackMessage_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_state::action::RobotTask_FeedbackMessage_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_state::action::RobotTask_FeedbackMessage_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_state::action::RobotTask_FeedbackMessage_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_state::action::RobotTask_FeedbackMessage_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_state::action::RobotTask_FeedbackMessage_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_state__action__RobotTask_FeedbackMessage
    std::shared_ptr<robot_state::action::RobotTask_FeedbackMessage_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_state__action__RobotTask_FeedbackMessage
    std::shared_ptr<robot_state::action::RobotTask_FeedbackMessage_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotTask_FeedbackMessage_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    if (this->feedback != other.feedback) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotTask_FeedbackMessage_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotTask_FeedbackMessage_

// alias to use template instance with default allocator
using RobotTask_FeedbackMessage =
  robot_state::action::RobotTask_FeedbackMessage_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace robot_state

#include "action_msgs/srv/cancel_goal.hpp"
#include "action_msgs/msg/goal_info.hpp"
#include "action_msgs/msg/goal_status_array.hpp"

namespace robot_state
{

namespace action
{

struct RobotTask
{
  /// The goal message defined in the action definition.
  using Goal = robot_state::action::RobotTask_Goal;
  /// The result message defined in the action definition.
  using Result = robot_state::action::RobotTask_Result;
  /// The feedback message defined in the action definition.
  using Feedback = robot_state::action::RobotTask_Feedback;

  struct Impl
  {
    /// The send_goal service using a wrapped version of the goal message as a request.
    using SendGoalService = robot_state::action::RobotTask_SendGoal;
    /// The get_result service using a wrapped version of the result message as a response.
    using GetResultService = robot_state::action::RobotTask_GetResult;
    /// The feedback message with generic fields which wraps the feedback message.
    using FeedbackMessage = robot_state::action::RobotTask_FeedbackMessage;

    /// The generic service to cancel a goal.
    using CancelGoalService = action_msgs::srv::CancelGoal;
    /// The generic message for the status of a goal.
    using GoalStatusMessage = action_msgs::msg::GoalStatusArray;
  };
};

typedef struct RobotTask RobotTask;

}  // namespace action

}  // namespace robot_state

#endif  // ROBOT_STATE__ACTION__DETAIL__ROBOT_TASK__STRUCT_HPP_
