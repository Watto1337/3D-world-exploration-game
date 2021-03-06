# 3D-world-exploration-game
Explore a randomly generated 3D world and enjoy the simulated terrain.

Download all of the Python script files included to run the program. The script you will need to run is Example.py

To give the program control of your mouse, click inside the Pygame window. This will hide your mouse and allow you to use it to look around. To release the mouse, just click again. Looking around does not affect the way the car moves, but can offer a more interesting perspective.
Use the WASD keys to control the car: W to move forward, S to move backwards, A to turn left and D to turn right. You can only turn while you are moving.

This project was made entirely in Python and makes use of the Pygame module for Python, which can be downloaded using pip - follow the instructions at pygame.org/wiki/GettingStarted.

I wrote all of the code myself, using no libraries (with the exception of Pygame, of course). This includes the 3D rendering tool and the noise algorithm, which was inspired by experiments with Perlin Noise.

Unforeseen difficulties included:
 - Proper perspective scaling for three dimensional objects
 - Correct rotation for the third-person perspective
 - Rotation for the car model on the terrain

If you want to use either the 3D rendering tool or the noise algorithm, I would recommend taking a close look at them and analysing the function inputs and outputs. It is also important to take a look at the class definitions in the 3D renderer for the camera and the screen objects; these are essential and will not be created automatically.

The code is not yet refined or organized particularly well, but I will continue to work on it. If you want to use some or all of these modules, I would recommend waiting until the end of June 2020 to ensure that I have finished the code and cleaned it up a bit.
