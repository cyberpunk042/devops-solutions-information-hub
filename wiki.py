#!/usr/bin/env python3
"""Wiki viewer — cross-platform entry point.

Usage: ./wiki                    (Linux/macOS via symlink)
       python wiki.py            (any platform)
       wiki.cmd                  (Windows)
       python3 -m tools.view     (direct module)
"""
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.argv[0] = "wiki"

from tools.view import main
main()
