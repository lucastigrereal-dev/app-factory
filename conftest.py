"""PyTest configuration file for System Creation OS tests.

This conftest ensures that the ``src`` directory is on ``sys.path`` so
that modules can be imported without installing the package. It also
provides common fixtures if needed in the future.
"""

import os
import sys

# Add the src directory to sys.path so tests can import modules without
# installing the package. This path is resolved relative to the project root.
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(ROOT_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

def pytest_configure(config):
    """Hook to configure PyTest with project‑wide settings (placeholder)."""
    # No global fixtures yet; placeholder for future use.
    return