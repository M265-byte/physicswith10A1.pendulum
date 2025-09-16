import streamlit as st
import numpy as np
from PIL import Image, ImageDraw
import time

st.title("🎯 Pendulum Simulation (with 10A1!)")

st.write("The period of a pendulum is given by:")
st.latex(r"T = 2 \pi \sqrt{\frac{L}{g}}")

# Inputs
L = st.slider("Length of pendulum (m)", 0.1, 5.0, 1.0, 0.1)
g = st.slider("Gravity (m/s²)", 1.0, 20.0, 9.8, 0.1)
amplitude = st.slider("Amplitude (degrees)", 5, 45, 20)
speed = st.slider("Animation speed (faster → smaller value)", 0.01, 0.2, 0.05)

# Period
T = 2 * np.pi * np.sqrt(L / g)
st.write(f"**Pendulum Period (T): {T:.2f} seconds**")

theta0 = np.radians(amplitude)
placeholder = st.empty()

# Animation
steps = 300
img_size = 400
center = img_size // 2

for i in range(steps):
    t = i * T / steps
    theta = theta0 * np.cos(2*np.pi*t/T)
    
    # Pendulum coordinates
    x = center + L*50 * np.sin(theta)  # scale for display
    y = center + L*50 * np.cos(theta)
    
    # Create blank image
    img = Image.new("RGB", (img_size, img_size), "white")
    draw = ImageDraw.Draw(img)
    
    # Draw string
    draw.line([center, center, x, y], fill="black", width=3)
    # Draw bob
    draw.ellipse([x-15, y-15, x+15, y+15], fill="blue")
    # Draw pivot
    draw.ellipse([center-5, center-5, center+5, center+5], fill="black")
    
    placeholder.image(img)
    time.sleep(speed)
