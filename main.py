import numpy as np
import matplotlib.pyplot as plt
import attractors

# Parameters
n_iter = 1000
n_points = 1000
starting_radius = 1
axis_limit = 2.5
title = "Zaslavskii Attractor"

# Starting values
R = np.sqrt(np.random.uniform(0, starting_radius, n_points))
T = np.random.uniform(0, 2*np.pi, n_points)
X = R*np.cos(T)
Y = R*np.sin(T)

# Plot setup
fig = plt.figure(figsize=(8,8))
ax = plt.subplot(1,1,1, aspect=1, frameon=False)
fig.tight_layout()
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-axis_limit, axis_limit)
ax.set_ylim(-axis_limit, axis_limit)
ax.text(0.5, 1, title, size=36, name="Roboto", weight=100, ha="center", va="top", transform=ax.transAxes)

# Compute
for _ in range(n_iter):
    X, Y = attractors.zaslavskii(X, Y, eps=1.5, nu=0.8, r=1.2)
    # Plot result
    ax.scatter(X, Y, s=0.2, edgecolors="none", facecolor="black", alpha=0.2)

# Save figure
fig.savefig("images/" + title.replace(" ", "") + ".png")
plt.show()
