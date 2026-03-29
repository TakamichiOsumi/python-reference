# Copy the contents of the last edited file in the current directory to clipboard.

cat `ls -lt | head -2 | tail -1 | awk '{ print $9 }'` | grep -vE "^[ \t]*#.*" | pbcopy
