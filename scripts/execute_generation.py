#!/usr/bin/env python3
"""
Execute the generation script manually
"""
import sys
import os

# Add the current directory to the path
sys.path.insert(0, '/Users/suganolab/web/bibleweb')

# Import and run the main function
from generate_all_formats import main

if __name__ == "__main__":
    print("Starting 1 Esdras format generation...")
    main()
    print("Generation complete!")