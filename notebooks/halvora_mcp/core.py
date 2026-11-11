# core.py: the server object and the documents it manages.
import re
from pathlib import Path

from mcp.server.mcpserver import MCPServer          # called FastMCP in SDK 1.x

mcp = MCPServer("HalvoraDocs", log_level="ERROR")   # the name clients see; log only real errors


def _load_docs():
    """Split the report into one document per '## ' section, keyed by a short id."""
    report = (Path(__file__).parent.parent / "data" / "halvora_report.md").read_text(encoding="utf-8")
    docs = {}
    for section in re.split(r"\n(?=## )", report)[1:]:              # [1:] skips the title block
        title = section.splitlines()[0].lstrip("# ").strip()        # "Section 2: Software Engineering"
        title = title.split(":", 1)[-1].strip()                     # "Software Engineering"
        doc_id = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")   # "software-engineering"
        docs[doc_id] = section.strip()
    return docs


docs = _load_docs()                    # doc_id -> text, kept in memory
