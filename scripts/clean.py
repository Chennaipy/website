#!/usr/bin/env python3
"""
Clean script for Chennai Python User Group website.
This script removes generated content and cached files.
"""

import os
import shutil
import argparse
from pathlib import Path

def main():
    """Main entry point for the clean command."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Clean generated content and cache files for the Chennai Python User Group website",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show verbose output"
    )
    args = parser.parse_args()
    
    # Get the base directory (project root)
    base_dir = Path(__file__).parent.parent.absolute()
    
    # Directories and files to clean
    clean_targets = [
        base_dir / "output",
        base_dir / "__pycache__",
        base_dir / "cache",
        base_dir / "pelican.pid",
        base_dir / "srv.pid",
    ]
    
    print("🧹 Cleaning Chennai Python User Group website...")
    
    cleaned_count = 0
    for target in clean_targets:
        if target.exists():
            if args.verbose:
                print(f"  Removing: {target}")
            
            if target.is_file():
                target.unlink()
            elif target.is_dir():
                shutil.rmtree(target)
            
            cleaned_count += 1
        elif args.verbose:
            print(f"  Not found: {target}")
    
    # Also clean any Python cache files recursively (but not in .venv)
    for pycache_dir in base_dir.rglob("__pycache__"):
        # Skip virtual environment directories
        if ".venv" in str(pycache_dir) or "venv" in str(pycache_dir):
            continue
        if pycache_dir.is_dir():
            if args.verbose:
                print(f"  Removing: {pycache_dir}")
            shutil.rmtree(pycache_dir)
            cleaned_count += 1
    
    # Clean any .pyc files (but not in .venv)
    for pyc_file in base_dir.rglob("*.pyc"):
        # Skip virtual environment directories
        if ".venv" in str(pyc_file) or "venv" in str(pyc_file):
            continue
        if pyc_file.is_file():
            if args.verbose:
                print(f"  Removing: {pyc_file}")
            pyc_file.unlink()
            cleaned_count += 1
    
    if cleaned_count > 0:
        print(f"✅ Cleaned {cleaned_count} items")
    else:
        print("✅ Nothing to clean - already clean!")

if __name__ == "__main__":
    main()
