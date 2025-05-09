#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <python_script.py> <comma_separated_packages>"
    exit 1
fi

PY_SCRIPT="$1"
REQUIRED_PKGS="$2"
BASENAME=$(basename "$PY_SCRIPT" .py)
TARGET="$HOME/.local/bin/$BASENAME"

PY_SCRIPT_DIR="$(readlink -f "$PY_SCRIPT")"
PY_SCRIPT_DIR="$(dirname "$PY_SCRIPT_DIR")"

if [ -e "$TARGET" ]; then
    echo "Error: Target script '$TARGET' already exists. Aborting."
    exit 1
fi

cat > "$TARGET" <<EOF
#!/bin/bash

SCRIPT_BASENAME="\$(basename "\$0")"
SCRIPT_NAME="\${SCRIPT_BASENAME%.*}"
REQUIRED_PYTHON_PACKAGES="${REQUIRED_PKGS//,/ }"
VENV_DIR="\$HOME/.\${SCRIPT_NAME}_venv"

if [ ! -d "\${VENV_DIR}" ]; then
    echo "Creating virtual environment at \${VENV_DIR}"
    python -m venv "\${VENV_DIR}"
    source "\${VENV_DIR}/bin/activate"
    pip install --upgrade pip
    for pkg in \${REQUIRED_PYTHON_PACKAGES}; do
        pip install "\$pkg"
    done
    deactivate
fi

echo "Activating virtual environment at \${VENV_DIR}"
source "\${VENV_DIR}/bin/activate"

# Set the location of Python script
MAIN_SCRIPT_PATH="$PY_SCRIPT_DIR/\${SCRIPT_NAME}.py"

# Fallback to finding the script in the same directory if not found at the specified location
if [ ! -f "\$MAIN_SCRIPT_PATH" ]; then
    SCRIPT_DIR=\$(dirname "\$(readlink -f "\$0")")
    MAIN_SCRIPT_PATH="\${SCRIPT_DIR}/\${SCRIPT_NAME}.py"
fi

# Execute with Python and pass all arguments
python "\$MAIN_SCRIPT_PATH" "\$@"

# Deactivate the virtual environment when done
deactivate
echo "Virtual environment deactivated"
EOF

chmod +x "$TARGET"
echo "Generated script: $TARGET"