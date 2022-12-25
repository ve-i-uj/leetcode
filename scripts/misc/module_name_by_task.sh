#!/bin/bash
#
# Returns the module name by the task name.

task_name="$1"

module_name=$(
    echo $task_name \
    | grep -oEw "[a-zA-Z ]+" \
    | xargs \
    | tr -s '[:blank:]' '_' \
    | tr '[:upper:]' '[:lower:]'
)

echo $module_name
