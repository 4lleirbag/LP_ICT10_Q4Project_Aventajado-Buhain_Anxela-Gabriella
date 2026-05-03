import numpy as np
import matplotlib.pyplot as plt
from pyscript import document, window, display

# Initial data
mo, tu, we, th, fr = 1, 0, 7, 4, 9 # Matches your screenshot example
positions = [0, 1, 2, 3, 4]
labels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def plot():
    plt.clf()
    global mo, tu, we, th, fr
    
    day = document.getElementById("day").value
    n_val = document.getElementById("num").value
    n = int(n_val) if n_val else 0

    if day == 'monday': mo = n
    elif day == 'tuesday': tu = n
    elif day == 'wednesday': we = n
    elif day == 'thursday': th = n
    elif day == 'friday': fr = n

    y = np.array([mo, tu, we, th, fr])
    x = np.arange(len(labels))

    # Create the plot style
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, y, marker='o', linestyle='-', color='#1f77b4') # Blue line + dots
    
    ax.set_title("Weekly Attendance (Absences)")
    ax.set_xlabel('Day')
    ax.set_ylabel('Number of Absences')
    ax.set_xticks(positions)
    ax.set_xticklabels(labels)
    ax.grid(True, linestyle='-', alpha=0.7) # Enable the grid
    
    # Display the plot in the specific div
    display(fig, target="mypyplot", append=False)

# Expose to JS
window.plot = plot

# Initial run to show the graph on load
plot()