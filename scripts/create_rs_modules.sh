# Import global constants
curr_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source `realpath $curr_dir/../init.sh`

USAGE="
Usage. The script creates a template of a rust module for the leetcode task.
Use the task level name as the first argument (easy, medium, hard) and \
the task name as the second. Example:
bash $0 easy \"27. Remove Element\"
"

SRC_PATH="$PROJECT_DIR/leetcode/rsleetcode/src"

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
export task_name=$task_name task_url=$task_url module_name=$module_name

path="$SRC_PATH/$level/$module_name.rs"
echo "[INFO] Create a module template (path = \"$path\") ..."
envsubst < "$curr_dir/templates/rs_module.template" > $path

echo "[INFO] Add the reference to the \"$module_name\" in the mod.rs ..."
touch "$SRC_PATH/$level/mod.rs"
echo "pub mod $module_name;" >> "$SRC_PATH/$level/mod.rs"

echo "[INFO] Done ($0)"
