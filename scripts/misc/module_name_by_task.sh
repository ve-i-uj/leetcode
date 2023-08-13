#!/bin/bash
#
# Returns the module name by the task name.

task_name="$1"
task_name=$( echo "$task_name" | tr -d "'" )

module_name=$(
    echo $task_name \
    | python3 -c "import re; print(\
        re.findall(\
            '\d+\.\s*\d*([\w\d ]+)', \
            '$task_name'
        )[0]\
        .strip()\
        .replace(' ', '_')\
        .replace('-', '_')\
        .lower()
    )"
)
echo $module_name
