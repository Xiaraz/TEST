#!/usr/bin/env python3
"""
Launch script for YouTube Content Coach.
Run this file to start the interactive assistant.

Usage:
    python run_coach.py
"""

import sys
import os

# Ensure the project root is in the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from youtube_coach.main import main

if __name__ == "__main__":
    main()
