# main.py
import sys
from pathlib import Path

# Add the parent directory of 'examples' to the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from examples import example_usage


def main():
    example_usage.run_example()


if __name__ == "__main__":
    main()
