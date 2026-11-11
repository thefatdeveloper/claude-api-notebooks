# tools.py: ACTIONS Claude can take. (Chapter 4)
from mcp.server.mcpserver.exceptions import ToolError
from pydantic import Field

from core import docs, mcp


@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a Halvora document and return it as a string.",
)
def read_document(
    doc_id: str = Field(description="Id of the document to read, e.g. 'software-engineering'"),
) -> str:
    if doc_id not in docs:
        raise ToolError(f"Doc with id {doc_id} not found. Available: {', '.join(docs)}")
    return docs[doc_id]


@mcp.tool(
    name="edit_document",
    description="Edit a document by replacing a string in the document's content with a new string.",
)
def edit_document(
    doc_id: str = Field(description="Id of the document that will be edited"),
    old_str: str = Field(description="The text to replace. Must match exactly, including whitespace."),
    new_str: str = Field(description="The new text to insert in place of the old text."),
) -> str:
    if doc_id not in docs:
        raise ToolError(f"Doc with id {doc_id} not found. Available: {', '.join(docs)}")
    if old_str not in docs[doc_id]:
        raise ToolError("old_str was not found in the document. Read it first and copy the text exactly.")
    docs[doc_id] = docs[doc_id].replace(old_str, new_str)
    return f"Edited {doc_id}: replaced {len(old_str)} characters."
