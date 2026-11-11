# prompts.py: ready-made, tested INSTRUCTIONS the user can pick. (Chapter 9)
from mcp.server.mcpserver.prompts import base
from pydantic import Field

from core import mcp


@mcp.prompt(name="format", description="Rewrites the contents of a document in Markdown format.")
def format_document(
    doc_id: str = Field(description="Id of the document to format"),
) -> list[base.Message]:
    prompt = f"""Your goal is to reformat a document to be written with markdown syntax.

The id of the document you need to reformat is:
<document_id>
{doc_id}
</document_id>

Add headers, bullet points, tables, etc. as needed. Feel free to add in structure.
Use the 'read_doc_contents' tool to read the document first. Then use the 'edit_document' tool
to replace the WHOLE current text with the reformatted version in one edit.
Do not change any facts or numbers. Reply with a one-line summary when done."""
    return [base.UserMessage(prompt)]


@mcp.prompt(name="board_brief", description="Summarises a document as 3 board-ready bullet points.")
def board_brief(
    doc_id: str = Field(description="Id of the document to summarise"),
) -> list[base.Message]:
    prompt = f"""You are briefing Halvora's board of directors.

Read the document with id '{doc_id}' using the 'read_doc_contents' tool.
Then write exactly 3 bullet points:
- each one sentence, at most 25 words,
- each containing at least one number from the document,
- ordered from most to least important for the board.
No introduction, no conclusion, only the 3 bullets."""
    return [base.UserMessage(prompt)]
