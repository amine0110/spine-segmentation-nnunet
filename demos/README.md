# What to do next?

Once you have your model trained, there are several ways of using or presenting your model to your clients, investers or supervisors.

The first thing that you can do it to create a sophisticated inference script to be used as an API or to be deployed in any type of UIs.

## Create a desktop application
You can create a desktop application based on QT that will help you upload your DICOMs/NIFTI and run the inference using the script that you created then show the output in 3D. I have attached [an example](qt_demo.py) of how to create the skeleton of a desktop application, you can use it with your inference code.

![desktop_app](/demos/assets/desktop_app.gif)

## Create a web application based on streamlit
You can deploy your model in a streamlit application where the user can upload their inputs and visualize the outputs in the UI directly. I have attached a [demo example](/demos/streamlit_demo.py) of how to create the visualization section in a streamlit application.

![streamlit_app](/demos/assets/streamlit_app.gif)

## Create a web application based on trame
Also another option to create a web application using Python, is Trame, this is a framework that helps you create good web applications for medical imaging and 3D visualization. I have attached a [demo example](/demos/trame_demo.py) of how to create the 3D viewer inside a trame application.

![trame_app](/demos/assets/trame_app.gif)

---
## Do you need something different?
Contact us and we can discuss your project in details 🚀