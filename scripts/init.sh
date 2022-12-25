_curr_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
export PROJECT_DIR=$( realpath "$_curr_dir/.." )
export PROJECT_NAME=$( basename "$PROJECT_DIR" )

export SCRIPTS="$PROJECT_DIR/scripts"

SQL_DIR="$PROJECT_DIR/sqlleetcode"
