# Copy the contents of the last edited file in the current directory to clipboard.

latest_file=`ls -lt | head -2 | tail -1 | awk '{ print $9 }'`
cat $latest_file | grep -vE "^[ \t]*#.*" | pbcopy

# Trigger the creation of the backup file, if -c option is appended.
while getopts "c" opt; do
    case "$opt" in
	c)
	    cp $latest_file ${latest_file}.backup_`date '+%Y%m%d%H%M%S'`
	    ;;
    esac
done
