set -e

# Import global constants
curr_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source `realpath $curr_dir/init.sh`

USAGE="
Usage. The script creates a template of a rust module for the leetcode task.
Use the task name as the first argument (easy, medium, hard) and \
the task level name as the second. Example:
bash $0 \"27. Remove Element\" easy
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
git_branch=$(bash "$SCRIPTS/misc/git_branch_by_task.sh" "$task_name")

echo "[INFO] Check the leetcode git branch name is \"develop\""
cd "$PROJECT_DIR"
current_branch=$(git branch --show-current)
if [ $current_branch != "develop" ]; then
    echo "[ERROR] The current git branch name is not \"develop\" (current branch = \"$current_branch\")"
    exit 1
fi
git checkout -b "$git_branch"

# These variables need for "envsubst"
export task_name=$task_name task_url=$task_url module_name=$module_name

path="$SRC_PATH/$level/$module_name.rs"
echo "[INFO] Create a module template (path = \"$path\") ..."
envsubst < "$curr_dir/templates/rs_module.template" > $path

echo "[INFO] Add the reference to the \"$module_name\" in the mod.rs ..."
touch "$SRC_PATH/$level/mod.rs"
echo "pub mod $module_name;" >> "$SRC_PATH/$level/mod.rs"

echo "[INFO] Done ($0)"
