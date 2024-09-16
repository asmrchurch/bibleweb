if sudo lsof -t -i:80 > /dev/null; then
    sudo kill $(sudo lsof -t -i:80)
    echo "Killed process on port 80."
else
    echo "No process running on port 80."
fi
