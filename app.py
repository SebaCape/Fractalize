import streamlit as st
from fractal.mandelbrot import compute_mandelbrot
from fractal.rendering import render_image


st.set_page_config(layout="wide")
st.title("Mandelbrot Set Exploration")

#Sidebar Sliders
st.sidebar.header("Fractal Settings")
zoom = st.sidebar.slider("Zoom", 0.5, 10.0, 1.0, 0.1)
center_x = st.sidebar.slider("Horizontal View", -1.0, 1.0, 0.0, 0.01)
center_y = st.sidebar.slider("Vertical View", -1.0, 1.0, 0.0, 0.01)

#Constant Values
width = 600
height = 600
max_iter = int(100 * zoom**1.5)


#Compute bounds from zoom and center
x_range = 1.5 / zoom
y_range = 1.5 / zoom
xmin, xmax = center_x - x_range, center_x + x_range
ymin, ymax = center_y - y_range, center_y + y_range

#Compute Mandelbrot set and render
data = compute_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)
img_buf = render_image(data, (xmin, xmax, ymin, ymax))
st.image(img_buf, caption=f"Mandelbrot Set Zoomed (Zoom={zoom}, Center=({center_x},{center_y}))")