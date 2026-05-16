# Execute the last edited file in the current directory.
#
# This is just a wrapper script to run any scripts.
latest_file=`ls -lt | head -2 | tail -1 | awk '{ print $9 }'`

python3 $latest_file
