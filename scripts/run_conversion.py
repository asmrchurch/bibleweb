#!/usr/bin/env python3
import os
import subprocess
import sys

# Change to the correct directory
os.chdir('/Users/suganolab/web/bibleweb')

# Run the main script
try:
    result = subprocess.run([sys.executable, 'generate_all_formats.py'],
                          capture_output=True, text=True, check=True)
    print("STDOUT:")
    print(result.stdout)
    if result.stderr:
        print("STDERR:")
        print(result.stderr)
except subprocess.CalledProcessError as e:
    print(f"Script failed with return code {e.returncode}")
    print("STDOUT:", e.stdout)
    print("STDERR:", e.stderr)
except Exception as e:
    print(f"Error running script: {e}")