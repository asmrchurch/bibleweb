#!/usr/bin/env python3
"""
Install conversion tools using Python subprocess
"""
import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a command and return result"""
    print(f"Running: {description}")
    print(f"Command: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
        if result.returncode == 0:
            print(f"✓ {description} succeeded")
            if result.stdout:
                print("Output:", result.stdout[:200])
            return True
        else:
            print(f"✗ {description} failed")
            if result.stderr:
                print("Error:", result.stderr[:200])
            return False
    except subprocess.TimeoutExpired:
        print(f"✗ {description} timed out")
        return False
    except Exception as e:
        print(f"✗ {description} failed: {e}")
        return False

def main():
    print("Installing conversion tools...")
    print("=" * 50)

    # Check if homebrew is available
    if run_command("which brew", "Checking for Homebrew"):
        print("\nHomebrew found. Installing tools...")

        # Install wkhtmltopdf
        run_command("brew install --cask wkhtmltopdf", "Installing wkhtmltopdf")

        # Install calibre
        run_command("brew install --cask calibre", "Installing calibre")

        print("\nVerifying installations...")
        run_command("which wkhtmltopdf", "Checking wkhtmltopdf")
        run_command("which ebook-convert", "Checking calibre")

    else:
        print("Homebrew not found. Please install manually:")
        print("1. wkhtmltopdf: https://wkhtmltopdf.org/downloads.html")
        print("2. calibre: https://calibre-ebook.com/download")

if __name__ == "__main__":
    main()