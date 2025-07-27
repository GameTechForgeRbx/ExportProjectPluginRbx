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
  - [How to Use the Plugin](#how-to-use-the-plugin)
  - [How to Use the Python Tool](#how-to-use-the-python-tool)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Overview

**ExportProjectPluginRbx** is a Roblox Studio plugin designed to simplify the process of exporting the Structure of a Roblox-Game. It includes a Python script to further process or automate exported data for integration with external tools or pipelines.

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
   - Find the Python file (e.g., `export_processor.py`) in this repository.

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

### How to Use the Plugin

1. **Open Your Project in Roblox Studio.**
2. **Use the Plugin:**
   - Go to the **Plugins** tab.
   - Click on **ExportProjectPluginRbx**.
   - Follow the plugin's UI prompts to select what you want to export (e.g., place, models, assets).
   - Specify the export destination if prompted.
   - Click **Export**.
3. **Exported Files:**
   - The exported file(s) will be saved to your chosen directory, typically as `.rbxl`, `.rbxm`, or other supported formats.

### How to Use the Python Tool

1. **Locate the Exported Files:**
   - Use the files exported by the plugin as input for the Python script.

2. **Run the Python Script:**
   - In terminal/command prompt, navigate to the script’s directory.
   - Run the script, specifying the exported file:
     ```bash
     python export_processor.py path/to/exported_file.rbxl
     ```
   - (Optional) Add additional arguments as supported by the script for custom processing.

3. **Processed Output:**
   - The script will process the export, perform any conversions, or trigger automations as defined.

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
  - Review plugin and script logs or error messages.

---

## License

See [LICENSE](LICENSE) for details.

---

**Contributions and suggestions are welcome!**
