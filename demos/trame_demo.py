import pathlib

script_path = pathlib.Path(__file__).resolve()
ASSETS = script_path.parent / 'assets'

from trame.app import get_server
from trame.ui.vuetify import SinglePageLayout
from trame.widgets import vtk, vuetify

from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow
)
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOGeometry import vtkSTLReader
from glob import glob

spine_colors = ["AliceBlue", "Aquamarine", "Beige", "BlueViolet", "Burlywood", "Carrot", "Cornflower", "Darkgreen", "Darkmagenta", "Magenta", "Gold",
                "LavenderBlush", "LightSalmon", "YellowGreen", "MidnightBlue", "MintCream", "Olive", "PapayaWhip", "Pink"]

filenames = sorted(glob(str(ASSETS / 'stls' / '*.stl')))

def load_stl(filename, color):
    reader = vtkSTLReader()
    reader.SetFileName(filename)

    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetDiffuse(0.8)
    actor.GetProperty().SetDiffuseColor(color)
    actor.GetProperty().SetSpecular(0.3)
    actor.GetProperty().SetSpecularPower(60.0)

    return actor

server = get_server(client_type="vue2")
ctrl = server.controller

colors = vtkNamedColors()

# Create a rendering window and renderer
ren = vtkRenderer()
renderWindow = vtkRenderWindow()
renderWindow.AddRenderer(ren)

for i, filename in enumerate(filenames):
    color = colors.GetColor3d(spine_colors[i])
    actor = load_stl(filename, color)
    ren.AddActor(actor)

ren.SetBackground(colors.GetColor3d('WhiteSmoke'))
ren.ResetCamera()

with SinglePageLayout(server) as layout:
    layout.title.set_text("Spine STL Viewer")
    layout.icon.clickable = False
    layout.icon.path = str(ASSETS / 'logo_pycad.png')  # Set your logo_pycad here

    with layout.toolbar:
        vuetify.VSpacer()
        vuetify.VImg(src=str(ASSETS / 'logo_pycad.png'), max_height=50, max_width=50)
        vuetify.VSpacer()
        vuetify.VToolbarTitle("Built by PYCAD Team")

    with layout.content:
        with vuetify.VContainer(
            fluid=True,
            classes="pa-0 fill-height",
        ):
            html_view = vtk.VtkLocalView(renderWindow)  # client side rendering
            ctrl.on_server_ready.add(html_view.update)

if __name__ == "__main__":
    server.start()
