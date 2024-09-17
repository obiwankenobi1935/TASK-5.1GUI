import tkinter as tk
from gpiozero import LED
from time import sleep

# Set up GPIO pins for the LEDs
red_led = LED(17)
green_led = LED(27)
blue_led = LED(22)

# Function to turn on red LED
def turn_on_red():
    red_led.on()
    green_led.off()
    blue_led.off()

# Function to turn on green LED
def turn_on_green():
    red_led.off()
    green_led.on()
    blue_led.off()

# Function to turn on blue LED
def turn_on_blue():
    red_led.off()
    green_led.off()
    blue_led.on()

# GUI setup
root = tk.Tk()
root.title("LED Control")

# Create buttons to control the LEDs
red_button = tk.Button(root, text="Red LED", command=turn_on_red, bg="red", fg="white")
red_button.pack(padx=10, pady=5)

green_button = tk.Button(root, text="Green LED", command=turn_on_green, bg="green", fg="white")
green_button.pack(padx=10, pady=5)

blue_button = tk.Button(root, text="Blue LED", command=turn_on_blue, bg="blue", fg="white")
blue_button.pack(padx=10, pady=5)

# Start the Tkinter event loop
root.mainloop()

