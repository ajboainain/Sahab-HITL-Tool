# s_hitl_tool

## HITL Tool
1) Clone or download the contents of this repository.
2) Go to the directory of this project (where you downloaded it)
3) Open console and type: python -m venv venv
4) type in console: venv/Scripts/activate
5) pip install -r requirements.txt
6) Finally, run the file hitl_tool.py: python hitl_tool.py

## Mission Planner
7) On Mission Planner, press CTRL+F
8) Click "mavlink"
9) On the empty boxes in the table, select:
    - Type: UDP
    - Direction: Outbound
    - Port 5052 (or whatever you choose, as long as it's not taken)
    - Host/Baud: 127.0.0.1
10) Hit "Go"


NOTE: the flight controller must automatically set itself
to armed, and channels 1-12 must all be "RC-PASSTHROUGH".
Use "AUTO-ARM" Cube