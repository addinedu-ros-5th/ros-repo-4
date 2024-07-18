// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from task_manager:srv/GenerateOrder.idl
// generated code does not contain a copyright notice

#ifndef TASK_MANAGER__SRV__DETAIL__GENERATE_ORDER__TRAITS_HPP_
#define TASK_MANAGER__SRV__DETAIL__GENERATE_ORDER__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "task_manager/srv/detail/generate_order__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace task_manager
{

namespace srv
{

inline void to_flow_style_yaml(
  const GenerateOrder_Request & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GenerateOrder_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GenerateOrder_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace task_manager

namespace rosidl_generator_traits
{

[[deprecated("use task_manager::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const task_manager::srv::GenerateOrder_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  task_manager::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use task_manager::srv::to_yaml() instead")]]
inline std::string to_yaml(const task_manager::srv::GenerateOrder_Request & msg)
{
  return task_manager::srv::to_yaml(msg);
}

template<>
inline const char * data_type<task_manager::srv::GenerateOrder_Request>()
{
  return "task_manager::srv::GenerateOrder_Request";
}

template<>
inline const char * name<task_manager::srv::GenerateOrder_Request>()
{
  return "task_manager/srv/GenerateOrder_Request";
}

template<>
struct has_fixed_size<task_manager::srv::GenerateOrder_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<task_manager::srv::GenerateOrder_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<task_manager::srv::GenerateOrder_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace task_manager
{

namespace srv
{

inline void to_flow_style_yaml(
  const GenerateOrder_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: item_ids
  {
    if (msg.item_ids.size() == 0) {
      out << "item_ids: []";
    } else {
      out << "item_ids: [";
      size_t pending_items = msg.item_ids.size();
      for (auto item : msg.item_ids) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: names
  {
    if (msg.names.size() == 0) {
      out << "names: []";
    } else {
      out << "names: [";
      size_t pending_items = msg.names.size();
      for (auto item : msg.names) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: quantities
  {
    if (msg.quantities.size() == 0) {
      out << "quantities: []";
    } else {
      out << "quantities: [";
      size_t pending_items = msg.quantities.size();
      for (auto item : msg.quantities) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: warehouses
  {
    if (msg.warehouses.size() == 0) {
      out << "warehouses: []";
    } else {
      out << "warehouses: [";
      size_t pending_items = msg.warehouses.size();
      for (auto item : msg.warehouses) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: racks
  {
    if (msg.racks.size() == 0) {
      out << "racks: []";
    } else {
      out << "racks: [";
      size_t pending_items = msg.racks.size();
      for (auto item : msg.racks) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: cells
  {
    if (msg.cells.size() == 0) {
      out << "cells: []";
    } else {
      out << "cells: [";
      size_t pending_items = msg.cells.size();
      for (auto item : msg.cells) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: statuses
  {
    if (msg.statuses.size() == 0) {
      out << "statuses: []";
    } else {
      out << "statuses: [";
      size_t pending_items = msg.statuses.size();
      for (auto item : msg.statuses) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GenerateOrder_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: item_ids
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.item_ids.size() == 0) {
      out << "item_ids: []\n";
    } else {
      out << "item_ids:\n";
      for (auto item : msg.item_ids) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: names
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.names.size() == 0) {
      out << "names: []\n";
    } else {
      out << "names:\n";
      for (auto item : msg.names) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: quantities
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.quantities.size() == 0) {
      out << "quantities: []\n";
    } else {
      out << "quantities:\n";
      for (auto item : msg.quantities) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: warehouses
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.warehouses.size() == 0) {
      out << "warehouses: []\n";
    } else {
      out << "warehouses:\n";
      for (auto item : msg.warehouses) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: racks
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.racks.size() == 0) {
      out << "racks: []\n";
    } else {
      out << "racks:\n";
      for (auto item : msg.racks) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: cells
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.cells.size() == 0) {
      out << "cells: []\n";
    } else {
      out << "cells:\n";
      for (auto item : msg.cells) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: statuses
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.statuses.size() == 0) {
      out << "statuses: []\n";
    } else {
      out << "statuses:\n";
      for (auto item : msg.statuses) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GenerateOrder_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace task_manager

namespace rosidl_generator_traits
{

[[deprecated("use task_manager::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const task_manager::srv::GenerateOrder_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  task_manager::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use task_manager::srv::to_yaml() instead")]]
inline std::string to_yaml(const task_manager::srv::GenerateOrder_Response & msg)
{
  return task_manager::srv::to_yaml(msg);
}

template<>
inline const char * data_type<task_manager::srv::GenerateOrder_Response>()
{
  return "task_manager::srv::GenerateOrder_Response";
}

template<>
inline const char * name<task_manager::srv::GenerateOrder_Response>()
{
  return "task_manager/srv/GenerateOrder_Response";
}

template<>
struct has_fixed_size<task_manager::srv::GenerateOrder_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<task_manager::srv::GenerateOrder_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<task_manager::srv::GenerateOrder_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<task_manager::srv::GenerateOrder>()
{
  return "task_manager::srv::GenerateOrder";
}

template<>
inline const char * name<task_manager::srv::GenerateOrder>()
{
  return "task_manager/srv/GenerateOrder";
}

template<>
struct has_fixed_size<task_manager::srv::GenerateOrder>
  : std::integral_constant<
    bool,
    has_fixed_size<task_manager::srv::GenerateOrder_Request>::value &&
    has_fixed_size<task_manager::srv::GenerateOrder_Response>::value
  >
{
};

template<>
struct has_bounded_size<task_manager::srv::GenerateOrder>
  : std::integral_constant<
    bool,
    has_bounded_size<task_manager::srv::GenerateOrder_Request>::value &&
    has_bounded_size<task_manager::srv::GenerateOrder_Response>::value
  >
{
};

template<>
struct is_service<task_manager::srv::GenerateOrder>
  : std::true_type
{
};

template<>
struct is_service_request<task_manager::srv::GenerateOrder_Request>
  : std::true_type
{
};

template<>
struct is_service_response<task_manager::srv::GenerateOrder_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // TASK_MANAGER__SRV__DETAIL__GENERATE_ORDER__TRAITS_HPP_
