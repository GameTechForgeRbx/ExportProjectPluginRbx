# ExportProjectPluginRbx

A Roblox Studio plugin and companion Python tool to help you export and process Roblox projects with ease.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Plugin Setup](#plugin-setup)
  - [Python File Setup](#python-file-setup)
- [Usage](#usage)
  - [When to Use the Plugin](#when-to-use-the-plugin)
  - [How to Use the Plugin and Python Tool](#how-to-use-the-plugin-and-python-tool)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Overview

**ExportProjectPluginRbx** is a Roblox Studio plugin designed to simplify the process of exporting Roblox places, models, or assets. It includes a Python script to further process or automate exported data for integration with external tools or pipelines.

---

## Features

- **Simple export** of your Roblox project assets with a single click.
- **Python integration** for post-export processing, automation, or conversion to other formats.
- Supports complex or multi-asset projects.

---

## Prerequisites

- **Roblox Studio** (latest version recommended)
- **Python 3.8+** (for using the Python tool)
- Basic familiarity with Roblox Studio plugins and running Python scripts

---

## Installation

### Plugin Setup

1. **Download the Plugin File:**
   - Locate the plugin file (`ExportProjectPlugin.rbxm` or similar) in this repository.

2. **Add the Plugin to Roblox Studio:**
   - Open Roblox Studio.
   - Go to the **Plugins** tab.
   - Click **Manage Plugins** > **Open Plugins Folder**.
   - Copy the plugin file into this folder.
   - Restart Roblox Studio if necessary.

3. **Enable the Plugin:**
   - In Roblox Studio, go to the **Plugins** tab.
   - Ensure the **ExportProjectPluginRbx** is enabled (toggle switch).

### Python File Setup

1. **Download the Python Script:**
   - Find the Python file (e.g., `Plugin.py` or `export_processor.py`) in this repository.

2. **Install Python (if not installed):**
   - Download from [python.org](https://www.python.org/downloads/).
   - Ensure Python is added to your PATH.

3. **Install Required Dependencies:**
   - Open a terminal/command prompt.
   - Navigate to the directory containing the Python file.
   - Install dependencies (if a `requirements.txt` is provided):
     ```bash
     pip install -r requirements.txt
     ```

---

## Usage

### When to Use the Plugin

- When you want to export assets, places, or models from your Roblox project for backup, sharing, or further processing.
- When you need to automate export tasks as part of a build pipeline using the provided Python tool.

### How to Use the Plugin and Python Tool

1. **Start the Python Tool First:**
   - In your terminal or command prompt, navigate to the directory containing `Plugin.py`.
   - Run the script:
     ```bash
     python Plugin.py
     ```
   - Keep this script running; it will wait for export requests from Roblox Studio.

2. **Open Your Project in Roblox Studio.**

3. **Use the Plugin:**
   - Go to the **Plugins** tab.
   - Click on **ExportProjectPluginRbx**.
   - Follow the plugin's UI prompts to select what you want to export (e.g., place, models, assets).
   - Specify the export destination if prompted.

4. **Export:**
   - Click the **Export** button in the plugin UI.
   - The plugin will communicate with the running Python script to handle the export and any post-processing.

5. **Check Output:**
   - The exported files will be saved at your designated location, and any additional processing handled by the Python script will be completed.

---

## Troubleshooting

- **Plugin not showing up?**
  - Confirm the plugin file is in the correct plugins folder.
  - Make sure Roblox Studio is restarted after installing.

- **Python script errors?**
  - Ensure all dependencies are installed.
  - Check your Python version (`python --version`).

- **File not exporting/processing correctly?**
  - Double-check file paths.
  - Ensure the Python script (`Plugin.py`) is running before clicking export in Studio.
  - Review plugin and script logs or error messages.

---

## License

See [LICENSE](LICENSE) for details.

---

**Contributions and suggestions are welcome!**
