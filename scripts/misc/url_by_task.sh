#!/bin/bash
#
# Returns the url of the leetcode task.

curr_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

task_name="$1"

formated_name=$("$curr_dir/one_word_name_by_task.sh" "$task_name")
task_url="https://leetcode.com/problems/$formated_name/"

echo "$task_url"
