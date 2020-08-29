# Commands to set proper resolution on BENQ FP71G+ monitor
# run with sudo
# parameters for command below was get using: cvt 1280 1024 60
xrandr --newmode "1280x1024_60.00"  109.00  1280 1368 1496 1712  1024 1027 1034 1063 +hsync +vsync
xrandr --addmode VGA-0 1280x1024_60.00
xrandr --output VGA-0 --mode 1280x1024_60.00

