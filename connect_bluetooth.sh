#!/bin/bash

amixer scontrols
amixer sset 'Master' 50%

bluetoothctl << EOF
connect 0C:C4:13:F7:32:43
EOF

amixer scontrols
amixer sset 'Master' 50%
