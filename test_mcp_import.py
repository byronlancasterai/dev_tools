#!/usr/bin/env python3
"""Test if the mcp package is importable in python3."""

try:
    import mcp
    print(f"mcp version: {mcp.__version__ if hasattr(mcp, '__version__') else 'unknown'}")
    print("Import successful.")
except ImportError as e:
    print(f"Import failed: {e}")
except Exception as e:
    print(f"Other error: {e}")