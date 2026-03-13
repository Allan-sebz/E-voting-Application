"""
Entry point for the National E-Voting System.
Run this file to start the application.
"""

import sys
import os 

# Ensure the evoting package can be found
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from evoting.main import main

if __name__ == "__main__":
    main()
