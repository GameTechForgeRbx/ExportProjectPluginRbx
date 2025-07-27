# Python Server for Roblox Project Cloner
# This server receives project data from the Roblox plugin and recreates the structure.

import os
import re # Import the regular expressions module
from flask import Flask, request

app = Flask(__name__)

# Variable to store the incoming data chunks
data_chunks = []

def sanitize_name(name):
    """Removes characters that are illegal in Windows file/folder names."""
    # Replaces any of the following characters: \ / : * ? " < > | with an underscore
    if name is None:
        return "Unnamed"
    return re.sub(r'[\\/*?:"<>|]', '_', name)

# Function to recursively create the project structure
def create_project_structure(data, path):
    for item in data:
        # Sanitize the name to make it file-system-safe
        item_name = sanitize_name(item.get("Name"))
        class_name = item.get("ClassName")
        children = item.get("Children", [])
        source = item.get("Source")

        # Create a folder for non-script objects
        if source is None:
            folder_name = f"{item_name}({class_name})"
            new_path = os.path.join(path, folder_name)
            if not os.path.exists(new_path):
                os.makedirs(new_path)
            if children:
                create_project_structure(children, new_path)
        # Create a .lua file for scripts
        else:
            file_name = f"{item_name}.lua"
            file_path = os.path.join(path, file_name)
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(source)
            except Exception as e:
                print(f"Could not write script {file_path}: {e}")

            # If the script has children, create a folder for them
            if children:
                folder_name = f"{item_name}({class_name})"
                new_path = os.path.join(path, folder_name)
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                create_project_structure(children, new_path)


@app.route('/clone', methods=['POST'])
def clone():
    """Receives and stores data chunks."""
    data_chunks.append(request.data.decode('utf-8'))
    return "Chunk received", 200

@app.route('/clone/complete', methods=['POST'])
def complete_cloning():
    """Assembles chunks and creates the project structure."""
    full_data_str = "".join(data_chunks)
    data_chunks.clear()  # Clear for the next clone

    if not full_data_str:
        return "No data received", 400

    import json
    try:
        project_data = json.loads(full_data_str)
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        return "Invalid JSON data", 400

    # Define the base path for the cloned project
    # This will create the folder on your Desktop
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    cloned_project_path = os.path.join(desktop_path, "ClonedRobloxProject")

    if not os.path.exists(cloned_project_path):
        os.makedirs(cloned_project_path)

    create_project_structure(project_data, cloned_project_path)
    print("Project cloning process completed successfully!")
    return "Project cloned successfully!", 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)