# keyboard_boxes

## What is keyboard_boxes? 
Mapping button inputs to USB keyboard (HID) events

### Purpose
Allow USB keyboard input from arcade buttons, foot pedals, etc.

### Contributors

### Software Dependencies


### BOM
- 1X: Adafruit Itsy Bitsy M0 (PRODUCT ID: 3727)
- any standard two wire input switch

### Pinouts

### Information Sources
- circuit python
	- https://github.com/todbot/MIDIPedalBox
	- https://learn.adafruit.com/introducing-itsy-bitsy-m0/circuitpython-hid-keyboard-and-mouse

### Issues
- 082220: The first acrylic box did not come together properly. I think it is an issue with the build order; what panels connected with each other. Or the panel with the USB cutout is not the correct size, though it worked on the cardboard version so I don't think that is the issue.
- 082220: The adafruit sample code does not handle continuous keystrokes (needed for Zoom Mute use case)

### Questions
- 082220: How do I make the CY disk non-mountable after completing the project?

### Learnings
- 082220: Box fit shape is harder with a larger # of joinery points and when the box is perfectly square. Seems like you could create more intuitive joinery with pieces not the same size, or joinery with different sizes on different panels?
- 082220: Acrylic needs few joinery points when merged via acrylic cement.

### Feature Requests
- 082220: Add nubs on flat side of button to ME file

### Revisions
- 082120: fork from Adafruit example for initial version