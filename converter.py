import os
from nbconvert import PythonExporter
import nbformat

def convert_ipynb_to_py(filename):
    # Check if the file is an IPython Notebook
    if filename.endswith('.ipynb'):
        ipynb_path = filename
        py_path = os.path.splitext(filename)[0] + '.py'
        
        try:
            # Read the Jupyter notebook
            with open(ipynb_path, 'r', encoding='utf-8') as f:
                notebook = nbformat.read(f, as_version=4)
            
            # Export the notebook content to a Python script
            exporter = PythonExporter()
            script, _ = exporter.from_notebook_node(notebook)
            
            # Write the Python script to the destination
            with open(py_path, 'w', encoding='utf-8') as f:
                f.write(script)

            print(f"Converted {filename} to {os.path.basename(py_path)}")
        
        except Exception as e:
            print(f"Error converting {filename}: {e}")

    else:
        print("The provided file is not a Jupyter Notebook (.ipynb file).")

# Directory of the notebook file
filename = r"D:\Hacks\Sisyphus\The-Real-Eye-rPPG-based-deepfake-detection-system\rPPG\load_media\load_media.ipynb"
convert_ipynb_to_py(filename)
