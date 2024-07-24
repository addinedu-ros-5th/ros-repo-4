// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_state:action/RobotTask.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_STATE__ACTION__DETAIL__ROBOT_TASK__BUILDER_HPP_
#define ROBOT_STATE__ACTION__DETAIL__ROBOT_TASK__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robot_state/action/detail/robot_task__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robot_state
{

namespace action
{

namespace builder
{

class Init_RobotTask_Goal_orientation_w
{
public:
  explicit Init_RobotTask_Goal_orientation_w(::robot_state::action::RobotTask_Goal & msg)
  : msg_(msg)
  {}
  ::robot_state::action::RobotTask_Goal orientation_w(::robot_state::action::RobotTask_Goal::_orientation_w_type arg)
  {
    msg_.orientation_w = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_state::action::RobotTask_Goal msg_;
};

class Init_RobotTask_Goal_orientation_z
{
public:
  explicit Init_RobotTask_Goal_orientation_z(::robot_state::action::RobotTask_Goal & msg)
  : msg_(msg)
  {}
  Init_RobotTask_Goal_orientation_w orientation_z(::robot_state::action::RobotTask_Goal::_orientation_z_type arg)
  {
    msg_.orientation_z = std::move(arg);
    return Init_RobotTask_Goal_orientation_w(msg_);
  }

private:
  ::robot_state::action::RobotTask_Goal msg_;
};

class Init_RobotTask_Goal_pos_y
{
public:
  explicit Init_RobotTask_Goal_pos_y(::robot_state::action::RobotTask_Goal & msg)
  : msg_(msg)
  {}
  Init_RobotTask_Goal_orientation_z pos_y(::robot_state::action::RobotTask_Goal::_pos_y_type arg)
  {
    msg_.pos_y = std::move(arg);
    return Init_RobotTask_Goal_orientation_z(msg_);
  }

private:
  ::robot_state::action::RobotTask_Goal msg_;
};

class Init_RobotTask_Goal_pos_x
{
public:
  Init_RobotTask_Goal_pos_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotTask_Goal_pos_y pos_x(::robot_state::action::RobotTask_Goal::_pos_x_type arg)
  {
    msg_.pos_x = std::move(arg);
    return Init_RobotTask_Goal_pos_y(msg_);
  }

private:
  ::robot_state::action::RobotTask_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_state::action::RobotTask_Goal>()
{
  return robot_state::action::builder::Init_RobotTask_Goal_pos_x();
}

}  // namespace robot_state


namespace robot_state
{

namespace action
{

namespace builder
{

class Init_RobotTask_Result_goal_location
{
public:
  explicit Init_RobotTask_Result_goal_location(::robot_state::action::RobotTask_Result & msg)
  : msg_(msg)
  {}
  ::robot_state::action::RobotTask_Result goal_location(::robot_state::action::RobotTask_Result::_goal_location_type arg)
  {
    msg_.goal_location = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_state::action::RobotTask_Result msg_;
};

class Init_RobotTask_Result_robot_name
{
public:
  Init_RobotTask_Result_robot_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotTask_Result_goal_location robot_name(::robot_state::action::RobotTask_Result::_robot_name_type arg)
  {
    msg_.robot_name = std::move(arg);
    return Init_RobotTask_Result_goal_location(msg_);
  }

private:
  ::robot_state::action::RobotTask_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_state::action::RobotTask_Result>()
{
  return robot_state::action::builder::Init_RobotTask_Result_robot_name();
}

}  // namespace robot_state


namespace robot_state
{

namespace action
{

namespace builder
{

class Init_RobotTask_Feedback_remained_dist
{
public:
  Init_RobotTask_Feedback_remained_dist()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_state::action::RobotTask_Feedback remained_dist(::robot_state::action::RobotTask_Feedback::_remained_dist_type arg)
  {
    msg_.remained_dist = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_state::action::RobotTask_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_state::action::RobotTask_Feedback>()
{
  return robot_state::action::builder::Init_RobotTask_Feedback_remained_dist();
}

}  // namespace robot_state


namespace robot_state
{

namespace action
{

namespace builder
{

class Init_RobotTask_SendGoal_Request_goal
{
public:
  explicit Init_RobotTask_SendGoal_Request_goal(::robot_state::action::RobotTask_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::robot_state::action::RobotTask_SendGoal_Request goal(::robot_state::action::RobotTask_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_state::action::RobotTask_SendGoal_Request msg_;
};

class Init_RobotTask_SendGoal_Request_goal_id
{
public:
  Init_RobotTask_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotTask_SendGoal_Request_goal goal_id(::robot_state::action::RobotTask_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_RobotTask_SendGoal_Request_goal(msg_);
  }

private:
  ::robot_state::action::RobotTask_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_state::action::RobotTask_SendGoal_Request>()
{
  return robot_state::action::builder::Init_RobotTask_SendGoal_Request_goal_id();
}

}  // namespace robot_state


namespace robot_state
{

namespace action
{

namespace builder
{

class Init_RobotTask_SendGoal_Response_stamp
{
public:
  explicit Init_RobotTask_SendGoal_Response_stamp(::robot_state::action::RobotTask_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::robot_state::action::RobotTask_SendGoal_Response stamp(::robot_state::action::RobotTask_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_state::action::RobotTask_SendGoal_Response msg_;
};

class Init_RobotTask_SendGoal_Response_accepted
{
public:
  Init_RobotTask_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotTask_SendGoal_Response_stamp accepted(::robot_state::action::RobotTask_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_RobotTask_SendGoal_Response_stamp(msg_);
  }

private:
  ::robot_state::action::RobotTask_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_state::action::RobotTask_SendGoal_Response>()
{
  return robot_state::action::builder::Init_RobotTask_SendGoal_Response_accepted();
}

}  // namespace robot_state


namespace robot_state
{

namespace action
{

namespace builder
{

class Init_RobotTask_GetResult_Request_goal_id
{
public:
  Init_RobotTask_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_state::action::RobotTask_GetResult_Request goal_id(::robot_state::action::RobotTask_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_state::action::RobotTask_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_state::action::RobotTask_GetResult_Request>()
{
  return robot_state::action::builder::Init_RobotTask_GetResult_Request_goal_id();
}

}  // namespace robot_state


namespace robot_state
{

namespace action
{

namespace builder
{

class Init_RobotTask_GetResult_Response_result
{
public:
  explicit Init_RobotTask_GetResult_Response_result(::robot_state::action::RobotTask_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::robot_state::action::RobotTask_GetResult_Response result(::robot_state::action::RobotTask_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_state::action::RobotTask_GetResult_Response msg_;
};

class Init_RobotTask_GetResult_Response_status
{
public:
  Init_RobotTask_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotTask_GetResult_Response_result status(::robot_state::action::RobotTask_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_RobotTask_GetResult_Response_result(msg_);
  }

private:
  ::robot_state::action::RobotTask_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_state::action::RobotTask_GetResult_Response>()
{
  return robot_state::action::builder::Init_RobotTask_GetResult_Response_status();
}

}  // namespace robot_state


namespace robot_state
{

namespace action
{

namespace builder
{

class Init_RobotTask_FeedbackMessage_feedback
{
public:
  explicit Init_RobotTask_FeedbackMessage_feedback(::robot_state::action::RobotTask_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::robot_state::action::RobotTask_FeedbackMessage feedback(::robot_state::action::RobotTask_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_state::action::RobotTask_FeedbackMessage msg_;
};

class Init_RobotTask_FeedbackMessage_goal_id
{
public:
  Init_RobotTask_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotTask_FeedbackMessage_feedback goal_id(::robot_state::action::RobotTask_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_RobotTask_FeedbackMessage_feedback(msg_);
  }

private:
  ::robot_state::action::RobotTask_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_state::action::RobotTask_FeedbackMessage>()
{
  return robot_state::action::builder::Init_RobotTask_FeedbackMessage_goal_id();
}

}  // namespace robot_state

#endif  // ROBOT_STATE__ACTION__DETAIL__ROBOT_TASK__BUILDER_HPP_
