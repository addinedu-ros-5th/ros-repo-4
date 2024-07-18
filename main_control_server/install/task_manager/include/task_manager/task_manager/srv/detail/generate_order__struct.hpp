// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from task_manager:srv/GenerateOrder.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__SRV__DETAIL__GENERATE_ORDER__STRUCT_HPP_
#define TASK_MANAGER__SRV__DETAIL__GENERATE_ORDER__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__task_manager__srv__GenerateOrder_Request __attribute__((deprecated))
#else
# define DEPRECATED__task_manager__srv__GenerateOrder_Request __declspec(deprecated)
#endif

namespace task_manager
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GenerateOrder_Request_
{
  using Type = GenerateOrder_Request_<ContainerAllocator>;

  explicit GenerateOrder_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit GenerateOrder_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  // field types and members
  using _structure_needs_at_least_one_member_type =
    uint8_t;
  _structure_needs_at_least_one_member_type structure_needs_at_least_one_member;


  // constant declarations

  // pointer types
  using RawPtr =
    task_manager::srv::GenerateOrder_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const task_manager::srv::GenerateOrder_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<task_manager::srv::GenerateOrder_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<task_manager::srv::GenerateOrder_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      task_manager::srv::GenerateOrder_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<task_manager::srv::GenerateOrder_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      task_manager::srv::GenerateOrder_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<task_manager::srv::GenerateOrder_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<task_manager::srv::GenerateOrder_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<task_manager::srv::GenerateOrder_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__task_manager__srv__GenerateOrder_Request
    std::shared_ptr<task_manager::srv::GenerateOrder_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__task_manager__srv__GenerateOrder_Request
    std::shared_ptr<task_manager::srv::GenerateOrder_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GenerateOrder_Request_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const GenerateOrder_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GenerateOrder_Request_

// alias to use template instance with default allocator
using GenerateOrder_Request =
  task_manager::srv::GenerateOrder_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace task_manager


#ifndef _WIN32
# define DEPRECATED__task_manager__srv__GenerateOrder_Response __attribute__((deprecated))
#else
# define DEPRECATED__task_manager__srv__GenerateOrder_Response __declspec(deprecated)
#endif

namespace task_manager
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GenerateOrder_Response_
{
  using Type = GenerateOrder_Response_<ContainerAllocator>;

  explicit GenerateOrder_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit GenerateOrder_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _item_ids_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _item_ids_type item_ids;
  using _names_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _names_type names;
  using _quantities_type =
    std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>>;
  _quantities_type quantities;
  using _warehouses_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _warehouses_type warehouses;
  using _racks_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _racks_type racks;
  using _cells_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _cells_type cells;
  using _statuses_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _statuses_type statuses;

  // setters for named parameter idiom
  Type & set__item_ids(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->item_ids = _arg;
    return *this;
  }
  Type & set__names(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->names = _arg;
    return *this;
  }
  Type & set__quantities(
    const std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>> & _arg)
  {
    this->quantities = _arg;
    return *this;
  }
  Type & set__warehouses(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->warehouses = _arg;
    return *this;
  }
  Type & set__racks(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->racks = _arg;
    return *this;
  }
  Type & set__cells(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->cells = _arg;
    return *this;
  }
  Type & set__statuses(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->statuses = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    task_manager::srv::GenerateOrder_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const task_manager::srv::GenerateOrder_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<task_manager::srv::GenerateOrder_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<task_manager::srv::GenerateOrder_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      task_manager::srv::GenerateOrder_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<task_manager::srv::GenerateOrder_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      task_manager::srv::GenerateOrder_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<task_manager::srv::GenerateOrder_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<task_manager::srv::GenerateOrder_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<task_manager::srv::GenerateOrder_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__task_manager__srv__GenerateOrder_Response
    std::shared_ptr<task_manager::srv::GenerateOrder_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__task_manager__srv__GenerateOrder_Response
    std::shared_ptr<task_manager::srv::GenerateOrder_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GenerateOrder_Response_ & other) const
  {
    if (this->item_ids != other.item_ids) {
      return false;
    }
    if (this->names != other.names) {
      return false;
    }
    if (this->quantities != other.quantities) {
      return false;
    }
    if (this->warehouses != other.warehouses) {
      return false;
    }
    if (this->racks != other.racks) {
      return false;
    }
    if (this->cells != other.cells) {
      return false;
    }
    if (this->statuses != other.statuses) {
      return false;
    }
    return true;
  }
  bool operator!=(const GenerateOrder_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GenerateOrder_Response_

// alias to use template instance with default allocator
using GenerateOrder_Response =
  task_manager::srv::GenerateOrder_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace task_manager

namespace task_manager
{

namespace srv
{

struct GenerateOrder
{
  using Request = task_manager::srv::GenerateOrder_Request;
  using Response = task_manager::srv::GenerateOrder_Response;
};

}  // namespace srv

}  // namespace task_manager

#endif  // TASK_MANAGER__SRV__DETAIL__GENERATE_ORDER__STRUCT_HPP_
