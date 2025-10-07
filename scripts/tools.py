#!/usr/bin/env python3
"""Chennai Python User Group website development tools."""

import os
import sys
import shutil
import signal
import subprocess
import argparse
from pathlib import Path

def get_base_dir():
    """Get the project base directory."""
    return Path(__file__).parent.parent.absolute()

def clean_command(verbose=False):
    """Clean generated content and cache files."""
    base_dir = get_base_dir()
    targets = ["output", "__pycache__", "cache", "pelican.pid", "srv.pid"]
    
    print("Cleaning...")
    count = 0
    
    for target in targets:
        path = base_dir / target
        if path.exists():
            if verbose: print(f"  Removing: {path}")
            shutil.rmtree(path) if path.is_dir() else path.unlink()
            count += 1
    
    # Clean project __pycache__ dirs (skip .venv)
    for cache in base_dir.rglob("__pycache__"):
        if ".venv" not in str(cache):
            if verbose: print(f"  Removing: {cache}")
            shutil.rmtree(cache)
            count += 1
    
    print(f"Cleaned {count} items" if count else "Already clean!")

def dev_command(port=8000):
    """Start the development server."""
    base_dir = get_base_dir()
    os.chdir(base_dir)
    
    print(f"Starting server on http://localhost:{port}")
    print("Press Ctrl+C to stop")
    
    processes = []
    
    def cleanup(signum=None, frame=None):
        print("\nStopping server...")
        for p in processes:
            p.terminate()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)
    
    try:
        # Start Pelican
        pelican = subprocess.Popen([
            sys.executable, "-m", "pelican", "--debug", "--autoreload", "-r",
            "content", "-o", "output", "-s", "pelicanconf.py"
        ])
        processes.append(pelican)
        
        # Wait for output dir
        while not (base_dir / "output").exists():
            pass
        
        # Start server
        server = subprocess.Popen([
            sys.executable, "-m", "pelican.server", str(port)
        ], cwd="output")
        processes.append(server)
        
        # Keep alive
        pelican.wait()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cleanup()

def dev_main():
    """Entry point for dev command."""
    parser = argparse.ArgumentParser(description="Start development server")
    parser.add_argument("-p", "--port", type=int, default=8000, help="Port (default: 8000)")
    args = parser.parse_args()
    dev_command(args.port)

def clean_main():
    """Entry point for clean command."""
    parser = argparse.ArgumentParser(description="Clean generated files")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()
    clean_command(args.verbose)

def main():
    """Main entry point for web command (backward compatibility)."""
    parser = argparse.ArgumentParser(description="Chennai Python User Group website tools")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Dev command
    dev_parser = subparsers.add_parser("dev", help="Start development server")
    dev_parser.add_argument("-p", "--port", type=int, default=8000, help="Port (default: 8000)")
    
    # Clean command
    clean_parser = subparsers.add_parser("clean", help="Clean generated files")
    clean_parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    
    if args.command == "dev":
        dev_command(args.port)
    elif args.command == "clean":
        clean_command(args.verbose)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
