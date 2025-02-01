#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# -----------------------------
# Simulation parameters
# -----------------------------
dt = 0.02             # time step
bound = 1.0           # tesseract boundaries: each coordinate in [-bound, bound]
num_frames = 1000     # number of animation frames

# -----------------------------
# Initial state in 4D (x, y, z, w)
# -----------------------------
pos = np.random.uniform(-0.5, 0.5, 4)  # initial position in 4D space
vel = np.random.uniform(-1, 1, 4)        # initial velocity in 4D space

# -----------------------------
# Set up the figure and subplots for projections
# -----------------------------
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Left subplot: Projection onto the (x, y) plane
axs[0].set_title("Projection onto (x, y) plane")
axs[0].set_xlim(-bound, bound)
axs[0].set_ylim(-bound, bound)
axs[0].set_aspect('equal', 'box')

# Right subplot: Projection onto the (z, w) plane
axs[1].set_title("Projection onto (z, w) plane")
axs[1].set_xlim(-bound, bound)
axs[1].set_ylim(-bound, bound)
axs[1].set_aspect('equal', 'box')

# Optionally, draw the square boundaries for each projection.
for ax in axs:
    ax.plot([-bound, bound], [bound, bound], 'k-')    # top edge
    ax.plot([bound, bound], [bound, -bound], 'k-')       # right edge
    ax.plot([bound, -bound], [-bound, -bound], 'k-')     # bottom edge
    ax.plot([-bound, -bound], [-bound, bound], 'k-')     # left edge

# Create plot objects for the ball in each projection.
ball_xy, = axs[0].plot([], [], 'bo', markersize=10)  # blue dot for (x, y)
ball_zw, = axs[1].plot([], [], 'ro', markersize=10)  # red dot for (z, w)

# -----------------------------
# Animation initialization function
# -----------------------------
def init():
    ball_xy.set_data([], [])
    ball_zw.set_data([], [])
    return ball_xy, ball_zw

# -----------------------------
# Animation update function
# -----------------------------
def update(frame):
    global pos, vel
    # Update the 4D position using the current velocity.
    pos = pos + vel * dt

    # Check for collisions with the tesseract walls (each coordinate)
    for i in range(4):
        if pos[i] > bound:
            pos[i] = bound
            vel[i] *= -1  # reverse velocity on hitting the positive wall
        elif pos[i] < -bound:
            pos[i] = -bound
            vel[i] *= -1  # reverse velocity on hitting the negative wall

    # Update the ball's position in each subplot.
    ball_xy.set_data(pos[0], pos[1])
    ball_zw.set_data(pos[2], pos[3])
    return ball_xy, ball_zw

# -----------------------------
# Create the animation
# -----------------------------
ani = animation.FuncAnimation(fig, update, frames=num_frames,
                              init_func=init, interval=20, blit=True)

# Show the animation window.
plt.show()
