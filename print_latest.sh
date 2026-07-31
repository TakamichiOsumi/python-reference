# Print the last edited file in the current directory.
latest_file=`ls -lt | head -2 | tail -1 | awk '{ print $9 }'`

echo $PWD/$latest_file
