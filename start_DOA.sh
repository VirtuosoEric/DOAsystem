#!/bin/bash
# start_DOA.sh
# Start the DOA Python server and then launch Chromium in kiosk mode.

# Start the Python server in the background.
python3 /home/raspberry/Desktop/project/DOAsystem/DOA_server.py &
server_pid=$!

# Wait a moment for the server to initialize.
sleep 2

# Set the display variable explicitly (assuming your local display is :0).
export DISPLAY=:0

# Set the X authority file if needed (adjust the path if your user home is different).
export XAUTHORITY=/home/raspberry/.Xauthority

# Optionally, wait until a display is detected (using xrandr).
while ! xrandr | grep " connected" > /dev/null; do
    sleep 1
done

# Launch Chromium in kiosk mode pointing to the local server.
chromium-browser --noerrdialogs --disable-infobars --kiosk http://localhost:5000
