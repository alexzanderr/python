

echo "this is run every time i run a command"

last_command=$(fc -ln -1)
result=$(python3 validate_url.py $last_command)
if [ result = "yes" ]; then
    xdg-open last_command
fi