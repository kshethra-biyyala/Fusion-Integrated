PERMISSIONS = [
    ("leave_elm.application.view", "See leave applications"),
    ("leave_elm.application.apply", "Submit a leave application"),
    ("leave_elm.application.approve", "Approve or reject a leave application"),
]

_EMPLOYEE = ["leave_elm.application.view", "leave_elm.application.apply"]
_APPROVER = ["leave_elm.application.view", "leave_elm.application.approve"]

ROLE_GRANTS = {
    "Employee": _EMPLOYEE,
    "Leave Approver": _APPROVER,
}