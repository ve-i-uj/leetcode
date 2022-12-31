# Import global constants
curr_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source `realpath $curr_dir/init.sh`

USAGE="
Example:
bash $0 <task_name> <level>
"

task_name="$1"
level="$2"

if [ -z "$level" ] || [ -z "$task_name" ]; then
    echo "[ERROR] Not all arguments passed"
    echo -e "$USAGE"
    exit 1
fi

module_name=$(bash "$curr_dir/misc/module_name_by_task.sh" "$task_name")
task_url=$(bash "$curr_dir/misc/url_by_task.sh" "$task_name")

# These variables need for "envsubst"
export task_name=$task_name task_url=$task_url module_name=$module_name level=$level

path="$PROJECT_DIR/leetcode/pyleetcode/tests/test_$level/test_$module_name.py"
echo "[INFO] Create a test module template (path = \"$path\") ..."
envsubst < "$curr_dir/templates/py_test_file.template" > $path

path="$PROJECT_DIR/leetcode/pyleetcode/pyleetcode/$level/$module_name.py"
echo "[INFO] Create a module template (path = \"$path\") ..."
envsubst < "$curr_dir/templates/py_module.template" > $path

echo "[INFO] Done ($0)"
