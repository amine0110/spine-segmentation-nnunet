# Credit to: https://github.com/edsaac/stpyvista

import pathlib

script_path = pathlib.Path(__file__).resolve()
ASSETS = script_path.parent / 'assets'

import pyvista as pv
import streamlit as st
from stpyvista import stpyvista
from glob import glob
import platform

if platform.system() == 'Linux':
    pv.start_xvfb()

st.set_page_config(page_icon="🧊", layout="wide", page_title="STL Viewer - PYCAD Team")

# Hex colors for the STL files
hex_colors = [
    "#FFC800", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF",
    "#808080", "#800000", "#008000", "#000080", "#808000", "#800080",
    "#008080", "#C0C0C0", "#FF4500", "#7FFF00", "#6495ED", "#DC143C",
    "#00FFFF"
]


def delmodel():
    del st.session_state.fileuploader


## Streamlit layout
st.sidebar.image(str(ASSETS / 'logo_pycad.png'), width=100)
st.sidebar.header("Streamlit Demo - by PYCAD Team")

placeholder = st.empty()


# paths = ['sinus.stl', 'airway_green.stl', 'jaws.stl']
colors = hex_colors # ["#ffc800", "#31de5f", "3145de"]
paths = glob(str(ASSETS / 'stls' / '*.stl'))

## Initialize pyvista reader and plotter
plotter = pv.Plotter(border=False, window_size=[1500, 1000])
plotter.background_color = "#000000"

for i, path in enumerate(paths):
    reader = pv.STLReader(path)
    mesh = reader.read() 
    plotter.add_mesh(mesh, color=colors[i])
    

plotter.view_isometric()


## Show in webpage
with placeholder.container():
    st.button("Restart", "btn_rerender", on_click=delmodel)
    stpyvista(plotter, key="my_stl")