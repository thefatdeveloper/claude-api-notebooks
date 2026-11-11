# server.py: the program an MCP client starts. It loads whichever chapter files exist.
import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))     # so "import core" works from anywhere
from core import mcp

for part in ["tools", "resources", "prompts"]:      # chapters 4, 7 and 9
    if (Path(__file__).parent / f"{part}.py").exists():
        importlib.import_module(part)

if __name__ == "__main__":
    mcp.run()                                        # the default transport is stdio
