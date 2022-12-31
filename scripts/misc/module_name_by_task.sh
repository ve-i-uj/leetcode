#!/bin/bash
#
# Returns the module name by the task name.

task_name="$1"

module_name=$(
    echo $task_name \
    | python3 -c "import re; print(\
        re.findall(\
            '\d+\. ([0-9a-zA-Z -_]+)', \
            '16. 3Sum Closest'
        )[0]\
        .replace(' ', '-')\
        .lower()
    )"
)
echo $module_name
