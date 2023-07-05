#!/bin/bash
#If it connects, write either connected or failed to a file, the main.py then reads it

#If it doesn't work, try leaving the earbuds in the case and close it for a few seconds, then take one out and try to connect right away

amixer scontrols
amixer sset 'Master' 50%

bluetoothctl << EOF
connect 0C:C4:13:F7:32:43
EOF

amixer scontrols
amixer sset 'Master' 50%
