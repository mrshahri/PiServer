from __future__ import print_function
import dlipower

print('Connecting to a DLI PowerSwitch at lpc.digital-loggers.com')
switch = dlipower.PowerSwitch(hostname="lpc.digital-loggers.com", userid="admin")

print('Turning off the first outlet')
switch.off(1)

print('The powerstate of the first outlet is currently', switch[0].state)

print('Renaming the first outlet as "Traffic light"')
switch[0].name = 'Traffic light'

print('The current status of the powerswitch is:')
print(switch)

# Connecting to a DLI PowerSwitch at lpc.digital-loggers.com
# Turning off the first outlet
# The powerstate of the first outlet is currently OFF
# Renaming the first outlet as "Traffic light"
# The current status of the powerswitch is:
# DLIPowerSwitch at lpc.digital-loggers.com
# Outlet      Hostname        State
# 1   Traffic light   OFF
# 2   killer robot    ON
# 3   Buiten verlicti ON
# 4   Meeting Room Li OFF
# 5   Brocade LVM123  ON
# 6   Shoretel ABC123 ON
# 7   Shortel 24V - T ON
# 8   Shortel 24V - T ON