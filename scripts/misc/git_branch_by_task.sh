#!/bin/bash
#
# Returns the name of a new branch name by the task name.

curr_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

task_name="$1"
task_name=$( echo "$task_name" | tr -d "'" )

number=$( echo $task_name | grep -oE "^[0-9]{1,5}" )
formated_name=$("$curr_dir/one_word_name_by_task.sh" "$task_name")
git_branch_name="feature-$number-$formated_name"

echo "$git_branch_name"
