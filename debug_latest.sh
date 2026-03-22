# Execute the last edited file and switch to the interactive debug mode if necessary.

python3 -m pdb -c continue `ls -lt | head -2 | tail -1 | awk '{ print $9 }'`
