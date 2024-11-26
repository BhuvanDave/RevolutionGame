import tkinter as tk

# Function to update the red progress bar (1.5 seconds)
# def update_red(progress_red, bars, root, red_speed):
#     current_red = progress_red.get()
#     increment = 1  # Calculate increment based on the speed
#     if current_red < 100:
#         progress_red.set(current_red + increment)
#         bars['red'].coords(bars['red_rect'], 0, 100 - current_red, 50, 100)
#         root.after(int((10/red_speed)), update_red, progress_red, bars, root, red_speed)  # Update every 1.5 seconds
#     else:
#         # Reset the red bar and start over immediately
#         progress_red.set(0)
#         bars['red'].coords(bars['red_rect'], 0, 100, 50, 100)
#         root.after(0, update_red, progress_red, bars, root, red_speed)  # Restart the cycle

# # Function to update the orange progress bar (5 seconds)
# def update_orange(progress_orange, bars, root, orange_speed):
#     current_orange = progress_orange.get()
#     increment = 1  # Calculate increment based on the speed
#     if current_orange < 100:
#         progress_orange.set(current_orange + increment)
#         bars['orange'].coords(bars['orange_rect'], 0, 100 - current_orange, 50, 100)
#         root.after(int((10/orange_speed)), update_orange, progress_orange, bars, root, orange_speed)  # Update every 5 seconds
#     else:
#         # Reset the orange bar and start over immediately
#         progress_orange.set(0)
#         bars['orange'].coords(bars['orange_rect'], 0, 100, 50, 100)
#         root.after(0, update_orange, progress_orange, bars, root, orange_speed)  # Restart the cycle

# # Function to update the yellow progress bar (10 seconds)
# def update_yellow(progress_yellow, bars, root, yellow_speed):
#     current_yellow = progress_yellow.get()
#     increment = 1  # Calculate increment based on the speed
#     if current_yellow < 100:
#         progress_yellow.set(current_yellow + increment)
#         bars['yellow'].coords(bars['yellow_rect'], 0, 100 - current_yellow, 50, 100)
#         root.after(int((10/yellow_speed)), update_yellow, progress_yellow, bars, root, yellow_speed)  # Update every 10 seconds
#     else:
#         # Reset the yellow bar and start over immediately
#         progress_yellow.set(0)
#         bars['yellow'].coords(bars['yellow_rect'], 0, 100, 50, 100)
#         root.after(0, update_yellow, progress_yellow, bars, root, yellow_speed)  # Restart the cycle

# Create the main window
root = tk.Tk()
root.title("Vertical Progress Bars Example")
root.geometry("300x150")

# Create a label for description
label = tk.Label(root, text="Vertical Progress Bars", font=("Arial", 14))
label.grid(row=0, column=0, columnspan=3, pady=10)  # Grid the label at the top

# Create progress variables for each bar
progress_red = tk.IntVar()
progress_orange = tk.IntVar()
progress_yellow = tk.IntVar()

# Create a canvas to draw the progress bars
bars = {
    'red': tk.Canvas(root, width=50, height=100, bg="white"),
    'orange': tk.Canvas(root, width=50, height=100, bg="white"),
    'yellow': tk.Canvas(root, width=50, height=100, bg="white")
}

# Grid the canvases next to each other (no padding)
bars['red'].grid(row=1, column=0)
bars['orange'].grid(row=1, column=1)
bars['yellow'].grid(row=1, column=2)

# Create the vertical rectangles for each color
bars['red_rect'] = bars['red'].create_rectangle(0, 100, 50, 100, fill="red", outline="")
bars['orange_rect'] = bars['orange'].create_rectangle(0, 100, 50, 100, fill="orange", outline="")
bars['yellow_rect'] = bars['yellow'].create_rectangle(0, 100, 50, 100, fill="yellow", outline="")

# Speed variables (how much the bar should fill up per second)
red_speed = 10  # Red bar should fill in ~1.5 seconds
orange_speed = 0.2  # Orange bar should fill in ~5 seconds
yellow_speed = 0.1  # Yellow bar should fill in ~10 seconds

# Start updating the progress bars with their respective speeds
# update_red(progress_red, bars, root, red_speed)
# update_orange(progress_orange, bars, root, orange_speed)
# update_yellow(progress_yellow, bars, root, yellow_speed)

# Run the Tkinter event loop
root.mainloop()
