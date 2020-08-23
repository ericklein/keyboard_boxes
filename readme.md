# keyboard_boxes

## What is keyboard_boxes? 
Mapping button inputs to USB keyboard (HID) events

### Purpose
Allow USB keyboard input from arcade buttons, foot pedals, etc.

### Contributors
branched from adafruit and todbot example code (see Information Sources)

### Software Dependencies
see import list

### BOM
- 1X: Adafruit Itsy Bitsy M0 (product ID 3727)
- 1X: Large Arcade Button with LED (product ID 1190)
- 1X: Arcade Button Quick-Connect Wire Pairs (product ID 1152)

### Pinouts
- Arcade button switch to A1 (doesn't matter) and GND
- Arcade light to D7 (doesn't matter) and GND

### Information Sources
- https://github.com/todbot/MIDIPedalBox
- https://learn.adafruit.com/introducing-itsy-bitsy-m0/circuitpython-hid-keyboard-and-mouse

### Issues
- 082220: The first acrylic box did not come together properly. I think it is an issue with the build order; what panels connected with each other. Or the panel with the USB cutout is not the correct size, though it worked on the cardboard version so I don't think that is the issue.

### Questions
- 082220: How do I make the CY disk non-mountable after completing the project?

### Learnings
- 082220: Box fit shape is harder with a larger # of joinery points and when the box is perfectly square. Seems like you could create more intuitive joinery with pieces not the same size, or joinery with different sizes on different panels?
- 082220: Acrylic needs few joinery points when merged via acrylic cement.

### Feature Requests
- 082220: Add nubs on flat side of button to ME file

### Revisions
- 082120: fork from Adafruit example for initial version
- 082320: switching to todbot example for continuous keystrokes, review Adafruit for BOBW code
- 082320: [issue 082220]: The adafruit sample code does not handle continuous keystrokes (needed for Zoom Mute use case)