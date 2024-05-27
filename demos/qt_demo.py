
import pathlib

script_path = pathlib.Path(__file__).resolve()
ASSETS = script_path.parent / 'assets'


import sys
import pathlib
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton, QGridLayout, QCheckBox, QScrollArea
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer
import vtkmodules.all as vtk
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOGeometry import vtkSTLReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer
)
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from glob import glob

class VTKVisualizer(QWidget):
    def __init__(self, stl_files, spine_colors, parent=None):
        super(VTKVisualizer, self).__init__(parent)
        self.colors = vtkNamedColors()
        self.stl_files = stl_files
        self.spine_colors = spine_colors
        self.actors = {}

        self.vl = QVBoxLayout()

        self.vtk_widget = QVTKRenderWindowInteractor(self)
        self.vl.addWidget(self.vtk_widget)

        self.ren = vtkRenderer()
        self.ren.SetBackground(self.colors.GetColor3d('White'))  # Set background to white
        self.vtk_widget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtk_widget.GetRenderWindow().GetInteractor()

        self.setLayout(self.vl)
        self.setStyleSheet("background-color: #2c3e50; border-radius: 10px;")

        self.load_models()

        self.rotating = False
        self.rotation_timer = QTimer()
        self.rotation_timer.timeout.connect(self.rotate_camera)

    def load_models(self):
        self.ren.RemoveAllViewProps()
        for i, file in enumerate(self.stl_files):
            actor = self.create_actor(file, self.spine_colors[i])
            self.actors[file] = actor

    def create_actor(self, filename, color):
        reader = vtkSTLReader()
        reader.SetFileName(filename)

        mapper = vtkPolyDataMapper()
        mapper.SetInputConnection(reader.GetOutputPort())

        actor = vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetDiffuse(0.8)
        actor.GetProperty().SetDiffuseColor(self.colors.GetColor3d(color))
        actor.GetProperty().SetSpecular(0.3)
        actor.GetProperty().SetSpecularPower(60.0)
        actor.GetProperty().SetOpacity(1.0)

        return actor

    def update_models(self, selected_files):
        self.ren.RemoveAllViewProps()
        for file in selected_files:
            self.ren.AddActor(self.actors[file])
        self.vtk_widget.GetRenderWindow().Render()

    def rotate_camera(self):
        if self.rotating:
            self.ren.GetActiveCamera().Azimuth(2)  # Adjusted rotation speed
            self.vtk_widget.GetRenderWindow().Render()

    def toggle_rotation(self):
        if self.rotating:
            self.rotation_timer.stop()
        else:
            self.rotation_timer.start(30)  # Adjusted timer interval for smoother rotation
        self.rotating = not self.rotating

    def closeEvent(self, event):
        self.rotation_timer.stop()
        super(VTKVisualizer, self).closeEvent(event)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("STL Viewer - PYCAD Team")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QGridLayout()
        central_widget.setLayout(main_layout)
        central_widget.setStyleSheet("background-color: black;")

        title_label = QLabel("STL Viewer")
        title_label.setFont(QFont("Arial", 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: white; margin: 10px;")

        # Get the directory of the current script
        script_dir = pathlib.Path(__file__).resolve().parent

        # Path to the STL files
        stl_files = sorted(glob(str(ASSETS / 'stls' / '*.stl')))

        spine_colors = ["AliceBlue", "Aquamarine", "Beige", "BlueViolet", "Burlywood", "Carrot", "Cornflower", "Darkgreen", "Darkmagenta", "Magenta", "Gold",
                        "LavenderBlush", "LightSalmon", "YellowGreen", "MidnightBlue", "MintCream", "Olive", "PapayaWhip", "Pink"]

        vtk_visualizer = VTKVisualizer(stl_files, spine_colors, self)

        # Create a scrollable area for the checkboxes
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        checkbox_widget = QWidget()
        checkbox_layout = QVBoxLayout()
        checkbox_widget.setLayout(checkbox_layout)
        scroll_area.setWidget(checkbox_widget)

        checkboxes = []
        for stl_file in stl_files:
            checkbox = QCheckBox(pathlib.Path(stl_file).stem)
            checkbox.setChecked(True)
            checkbox.setStyleSheet("color: white;")
            checkbox.stateChanged.connect(lambda state, file=stl_file: self.update_visualizer(state, file, vtk_visualizer))
            checkbox_layout.addWidget(checkbox)
            checkboxes.append(checkbox)

        # Start/Stop Rotation button
        rotation_button = QPushButton("Start/Stop Rotation")
        rotation_button.setFont(QFont("Arial", 14))
        rotation_button.setStyleSheet("background-color: #ffc800; color: black; padding: 10px; border-radius: 5px;")
        rotation_button.clicked.connect(vtk_visualizer.toggle_rotation)

        footer_layout = QHBoxLayout()
        logo_label = QLabel()
        logo_path = ASSETS / "logo_pycad.png"
        logo_label.setPixmap(QPixmap(str(logo_path)).scaled(50, 50, Qt.KeepAspectRatio))
        footer_layout.addWidget(logo_label)

        text_label = QLabel("Built by PYCAD team")
        text_label.setFont(QFont("Arial", 14))
        text_label.setStyleSheet("color: white;")
        footer_layout.addWidget(text_label)

        footer_layout.addStretch()

        main_layout.addWidget(title_label, 0, 0, 1, 2)
        main_layout.addWidget(scroll_area, 1, 0)
        main_layout.addWidget(rotation_button, 2, 0)
        main_layout.addWidget(vtk_visualizer, 1, 1, 2, 1)
        main_layout.addLayout(footer_layout, 3, 0, 1, 2)

    def update_visualizer(self, state, file, vtk_visualizer):
        selected_files = [checkbox.text() + '.stl' for checkbox in self.findChildren(QCheckBox) if checkbox.isChecked()]
        selected_files = [str(pathlib.Path(file).with_name(name)) for name in selected_files]
        vtk_visualizer.update_models(selected_files)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
