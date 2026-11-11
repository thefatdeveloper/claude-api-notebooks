# resources.py: DATA the app can read and put into the prompt. (Chapter 7)
from mcp.server.mcpserver.exceptions import ResourceNotFoundError

from core import docs, mcp


@mcp.resource("docs://documents", mime_type="application/json")
def list_docs() -> list[str]:
    """All document ids, for @mention autocomplete."""
    return list(docs.keys())


@mcp.resource("docs://documents/{doc_id}", mime_type="text/plain")
def fetch_doc(doc_id: str) -> str:
    """One document's full text."""
    if doc_id not in docs:
        raise ResourceNotFoundError(f"Doc with id {doc_id} not found")
    return docs[doc_id]
