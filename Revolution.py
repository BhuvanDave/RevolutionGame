import tkinter as tk
from tkmacosx import Button 
import threading
import os

# File to save the money value
SAVE_FILE = "data.txt"

# Function to load saved money and other data
def load_data():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as file:
            saved_data = file.read().splitlines()
            if len(saved_data) < 3:
                # If the file doesn't have enough data, return default values
                return 0, 0, 0
            money = int(saved_data[0])
            red_count = int(saved_data[1])
            yellow_count = int(saved_data[2])
            return money, red_count, yellow_count
    return 0, 0, 0  # Default money and counts if no save file exists

# Function to save money and counts
def save_data():
    with open(SAVE_FILE, "w") as file:
        file.write(f"{money}\n{red_count}\n{yellow_count}")

# Function to update money and display it
def add_dollar():
    global money
    money += 1
    update_display()
    save_data()

# Function to reset money and counts to $0
def reset_money():
    global money, red_count, yellow_count
    money = 0
    red_count = 0
    yellow_count = 0
    update_display()
    save_data()

# Function to buy auto-income
def buy_red():
    global money, red_count
    if money >= 10:  # Check if the player has enough money
        money -= 10
        red_count += 1  # Increase auto-income by 1
        update_display()
        save_data()

# Function to buy auto-upgrade
def buy_yellow():
    global money, yellow_count
    if money >= 100:  # Check if the player has enough money
        money -= 100
        yellow_count += 1  # Increase auto-upgrade count by 1
        update_display()
        save_data()

# Function to generate money automatically (called by Timer)
def generate_auto_income():
    global money
    money += red_count + (10 * yellow_count)
    update_display()
    save_data()
    start_timer()  # Restart the timer after each call

# Function to start the auto income timer
def start_timer():
    global timer
    timer = threading.Timer(1, generate_auto_income)  # Call every 1 second
    timer.start()

# Function to update the display labels
def update_display():
    money_label.config(text=f"Money: ${money}")
    # Update the top panel labels for counts
    red_count_label.config(text=f"Red Count: {red_count}")
    yellow_count_label.config(text=f"Orange Count: {yellow_count}")

# Initialize variables
money, red_count, yellow_count = load_data()
timer = None


#region GUI using tkinter
# Create the main window
root = tk.Tk()
root.title("Idle Game")
root.geometry("900x300")  # Set the window size

# Create the main frame to organize layout
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)


#region Top Panel
# Create a top panel to display auto income count and auto upgrade count
top_panel = tk.Frame(main_frame)
top_panel.grid(row=0, column=0, columnspan=2, pady=10)

# Create and pack the auto income count label on the top panel
red_count_label = tk.Label(top_panel, text=f"Red Count: {red_count}", font=("Arial", 16))
red_count_label.grid(row=0, column=0, padx=20)

# Create and pack the auto upgrade count label on the top panel
yellow_count_label = tk.Label(top_panel, text=f"Orange Count: {yellow_count}", font=("Arial", 16))
yellow_count_label.grid(row=0, column=1, padx=20)
#endregion

#region Left Panel
# Create a left panel to hold the buttons
left_panel = tk.Frame(main_frame)
left_panel.grid(row=1, column=0, padx=10, pady=10)

# Create and pack the "Buy Red" button 
buy_red_button = Button(left_panel, text="Buy Red ($10)", font=("Arial", 14), command=buy_red, bg="red", fg="black")
buy_red_button.grid(row=0, column=0, padx=10, pady=10, sticky="n")

# Create and pack the "Buy Orange" button 
buy_orange_button = Button(left_panel, text="Buy Orange ($100)", font=("Arial", 14), command=buy_yellow, bg="orange", fg="black")
buy_orange_button.grid(row=1, column=0, padx=10, pady=10, sticky="n")

# Create and pack the "Buy Yellow" button 
buy_yellow_button = Button(left_panel, text="Buy Yellow ($1000)", font=("Arial", 14), command=buy_yellow, bg="yellow", fg="black")
buy_yellow_button.grid(row=2, column=0, padx=10, pady=10, sticky="n")

# endregion

#region Middle Panel 
# Create a middle panel with 3 columns
middle_panel = tk.Frame(main_frame)
middle_panel.grid(row=1, column=1, pady=10, padx=10)

# Create progress variables for each bar
progress_red = tk.IntVar()
progress_orange = tk.IntVar()
progress_yellow = tk.IntVar()

# Create a canvas to draw the progress bars
bars = {
    'red': tk.Canvas(middle_panel, width=50, height=100, bg="white"),
    'orange': tk.Canvas(middle_panel, width=50, height=100, bg="white"),
    'yellow': tk.Canvas(middle_panel, width=50, height=100, bg="white")
}

# Grid the canvases next to each other (no padding)
bars['red'].grid(row=1, column=0)
bars['orange'].grid(row=1, column=1)
bars['yellow'].grid(row=1, column=2)

# Create the vertical rectangles for each color
bars['red_rect'] = bars['red'].create_rectangle(0, 100, 50, 100, fill="red", outline="")
bars['orange_rect'] = bars['orange'].create_rectangle(0, 100, 50, 100, fill="orange", outline="")
bars['yellow_rect'] = bars['yellow'].create_rectangle(0, 100, 50, 100, fill="yellow", outline="")
#endregion

#region Right Panel
# Create a right panel to hold the information
right_panel = tk.Frame(main_frame)
right_panel.grid(row=1, column=2, padx=10, pady=10)

# Create and pack the money label
money_label = tk.Label(right_panel, text=f"Money: ${money}", font=("Arial", 24))
money_label.grid(row=0, column=0, pady=10)

# Create and pack the "Add Money" button
add_money_button = tk.Button(right_panel, text="Add $1", font=("Arial", 18), command=add_dollar)
add_money_button.grid(row=1, column=0, pady=10)

# Create and pack the "Reset" button
reset_button = tk.Button(right_panel, text="Reset to $0", font=("Arial", 18), command=reset_money)
reset_button.grid(row=2, column=0, pady=10)
#endregion
#endregion

# Start generating auto income
start_timer()

# Run the application
root.mainloop()
