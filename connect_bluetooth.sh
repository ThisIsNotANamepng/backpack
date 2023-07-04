#!/bin/bash
#If it connects, write either connected or failed to a file, the main.py then reads it
amixer scontrols
amixer sset 'Master' 50%

bluetoothctl << EOF
connect 0C:C4:13:F7:32:43
EOF

amixer scontrols
amixer sset 'Master' 50%
