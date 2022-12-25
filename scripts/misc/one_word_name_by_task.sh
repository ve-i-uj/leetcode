#!/bin/bash
#
# Returns the the task name in lower case and using hyphens instead of spaces.

curr_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

task_name="$1"

module_name=$(bash "$curr_dir/module_name_by_task.sh" "$task_name")
echo $module_name | tr -s '_' '-'
