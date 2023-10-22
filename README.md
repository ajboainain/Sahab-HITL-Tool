# Sahab HITL Tool

## Mission Planner
1) On Mission Planner, press CTRL+F
2) Click "mavlink"
3) On the empty boxes in the table, select:
    - Type: UDP
    - Direction: Outbound
    - Port 5052 (or whatever you choose, as long as it's not taken)
    - Host/Baud: 127.0.0.1
4) Hit "Go"
5) For faster refresh rate, go to:
    - CONFIG tab
    - Planner side tab
    - "Telemetry Rates" -> "RC" = desired value (higher is better)
6) Enable joystick from "Actions" -> "Joystick"

## HITL Tool
7) Clone or download the contents of this repository.
8) Go to the directory of this project (where you downloaded it)
9) Open console and type: python -m venv venv
10) type in console: venv/Scripts/activate
11) pip install -r requirements.txt
12) Run the file hitl_tool.py: python hitl_tool.py
13) Select the flight controller you wish to connect to and hit connect
14) Select the port you chose in step 3 and hit connect


## Using Sahab HITL Tool


NOTE: the flight controller must automatically set itself
to armed, and channels 1-12 must all be "RC-PASSTHROUGH".
Use "AUTO-ARM" Cube