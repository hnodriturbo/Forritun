# Instructions to open settings in VSCode:
# 1. Open Command Palette with Ctrl+Shift+P (Windows/Linux) or Cmd+Shift+P (Mac)
# 2. Run "Preferences: Open User Settings (JSON)"

# Ensure Black is the default formatter for Python files
"[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"  # Set Black as default formatter
}

# Automatically format Python files on save
"[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",  # Confirm Black as formatter
    "editor.formatOnSave": true  # Enable format on save
}

# Customize Black formatter arguments
"black-formatter.args": ["--config", "<file>"]  # Custom args for Black, like config file

# Set the current working directory for Black
"black-formatter.cwd": "${workspaceFolder}"  # Default, use workspace root
# OR
"black-formatter.cwd": "${fileDirname}"  # Use parent folder of the file being formatted

# Specify a custom path or command for Black
"black-formatter.path": ["~/global_env/black"]  # Path to Black binary
# OR for using with Conda environment
"black-formatter.path": ["conda", "run", "-n", "lint_env", "python", "-m", "black"]  # Command to run Black in specific conda env

# Specify the Python interpreter for launching Black server
"black-formatter.interpreter": []  # Default, use selected Python interpreter
# OR specify a custom interpreter
"black-formatter.interpreter": ["path/to/python"]  # Custom Python interpreter

# Choose which Black formatter binary to use
"black-formatter.importStrategy": "useBundled"  # Use Black bundled with extension
# OR
"black-formatter.importStrategy": "fromEnvironment"  # Use Black from selected Python environment

# Control notification behavior
"black-formatter.showNotification": "onError"  # Show notifications on errors

# Select the transport protocol for Black server communication
"black-formatter.serverTransport": "stdio"  # Use stdio (default and recommended)
# OR
"black-formatter.serverTransport": "pipe"  # Use a named pipe or Unix Domain Socket

# Commands for additional actions
# Use Command Palette to restart Black formatting server if needed
# Command: Black Formatter: Restart

# Logging
# Set log level for Black formatter from the Command Palette or set trace level
"black-formatter.trace.server": "verbose"  # Get detailed logs, useful for bug reports

# Troubleshooting
# If Black is not found in the selected environment, ensure it's installed or use the bundled version.
# Adjust `black-formatter.importStrategy` and `black-formatter.path` as needed.
