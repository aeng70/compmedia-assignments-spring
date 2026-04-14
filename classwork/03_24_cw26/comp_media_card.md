ConfettiPiece.py  
COLOURS is a list of tuples, each representing an RGB colour. random.choice picks one at random.  
Each ConfettiPiece is a small falling rectangle. \_\_init\_\_ just calls reset(), which randomises all the properties — position, size, colour, speed, spin, and horizontal drift. The starting y is randomised between \-height and 0 so the pieces are staggered across the screen from the start rather than all appearing at the top simultaneously.  
update() moves the piece each frame: y increases (downward), x shifts by the drift, and angle rotates by spin. When a piece falls off the bottom (y \> height \+ 20), reset() is called and it starts again from the top — this gives the illusion of infinite falling confetti from a fixed pool of 120 objects.  
draw() saves the current transformation matrix with push\_matrix(), moves the origin to the piece's position with translate, rotates by its angle, draws the rectangle centred on the origin, then restores the matrix with pop\_matrix(). This means the rotation is always around the piece's own centre.  
---

FloatingFlower.py  
Each FloatingFlower is a flower that floats upward with a sine-wave horizontal drift.  
In \_\_init\_\_, size or random.uniform(...) is a compact way of saying "use the provided value if given, otherwise randomise" — this works because None is falsy in Python. The phase and freq properties are per-flower offsets for the sine oscillation, so each flower drifts at a different rate and starting point, making them look independent.  
update() moves the flower upward each frame (y decreases), rotates it by spin, and adds a sine-based horizontal nudge. frame\_count is a py5 global that increments every frame — multiplying it by freq controls the oscillation speed, and adding phase offsets each flower's wave so they don't all sway in unison. When the flower floats above the top of the screen, alive is set to False.  
draw() uses the same push\_matrix/translate/rotate/pop\_matrix pattern as ConfettiPiece. It draws three layers: a large semi-transparent ellipse for the glow, the petals arranged in a circle using trigonometry (cos and sin to place each petal around a central point), and a small yellow dot in the centre. The petal loop divides TWO\_PI (a full circle in radians) equally by the number of petals to find each petal's angle, then projects outward using cos and sin to get the x and y position.  
---

main.py  
This is the py5 sketch itself. py5 in imported mode looks for specific function names — setup(), draw(), mouse\_pressed(), key\_pressed() — and calls them automatically at the right times.  
setup() runs once at the start. It sets the canvas size, sets the default text size, and fills the confetti list with 120 ConfettiPiece objects.  
draw() runs every frame (by default 60 times per second). It:

1. Clears the screen with a solid dark purple background  
2. Updates and draws all confetti if show\_conf is True  
3. Updates and draws all flowers, then filters out dead ones with a list comprehension (flowers\[:\] \= \[f for f in flowers if f.alive\]) — the \[:\] slice assignment modifies the list in place rather than creating a new one, which matters because flowers is a global  
4. Draws the venus symbol and text on top of everything  
5. Draws the hint text in the bottom-left corner

draw\_symbol() computes r (the radius) using a sine wave so it pulses smoothly between 64 and 76\. All the symbol's geometry is expressed as multiples of r, so the whole shape scales uniformly. The circle sits at cy \- r \* 0.25 (slightly above centre), the vertical line drops from the bottom of the circle to below it, and the horizontal crossbar sits partway down that line.  
draw\_text() draws three layers of text at fixed positions. The title is drawn twice — once with a semi-transparent gold offset by 2 pixels to create a subtle shadow effect, then again in white on top.  
mouse\_pressed() appends a new FloatingFlower at the cursor position with a randomised size and speed each time the user clicks.  
key\_pressed() toggles show\_conf when space is pressed, turning confetti on and off. key is a py5 global that holds the most recently pressed key as a string.  
