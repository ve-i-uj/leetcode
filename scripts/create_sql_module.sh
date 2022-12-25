USAGE="
Example:
bash $0 easy \"27. Remove Element\"
"

set -e

_curr_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source "$_curr_dir/init.sh"

level="$1"
task_name="$2"

if [ -z "$level" ] || [ -z "$task_name" ]; then
    echo "[ERROR] Not all arguments passed"
    echo -e "$USAGE"
    exit 1
fi

module_name=$(bash "$SCRIPTS/misc/module_name_by_task.sh" "$task_name")
task_url=$(bash "$SCRIPTS/misc/url_by_task.sh" "$task_name")

task_dir="$SQL_DIR/$level/$module_name"
if [ ! -d "$task_dir" ]; then
    mkdir -p "$task_dir"
fi

echo "[INFO] Create content in the target directory (task_dir = \"$task_dir\")"
touch "$task_dir/$module_name.sql"
touch "$task_dir/data.sql"
touch "$task_dir/init.sh"

echo "bash \"$SCRIPTS/db/load_sql.sh\" \"$task_dir/data.sql\"" > "$task_dir/init.sh"
echo -e "-- 94. Binary Tree Inorder Traversal\n--\n-- $task_url\n" > "$task_dir/$module_name.sql"

echo "[INFO] Done ($0)"