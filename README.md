# Claude API Notebooks

Hands-on Python notebooks that walk through the Claude API, topic by topic. Clone the repo, add your API key, and run them. Each notebook explains one topic, shows what to look for in the output, and tells you what it will cost before you spend anything.

I built these after completing Anthropic's [Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api) course, to make the ideas runnable on the current API and models.

> This is an independent learning project. It is not affiliated with or endorsed by Anthropic. The explanations and code here are my own.

## Quick start

You need Python 3.10+ and an [Anthropic API key](https://platform.claude.com/). The commands below use [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/thefatdeveloper/claude-api-notebooks.git
cd claude-api-notebooks
uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install -r requirements.txt
cp .env.example .env        # then paste your key into .env
jupyter lab
```

Open `notebooks/00_setup_and_first_request.ipynb` and run it from the top.

## Learning path

| # | Notebook | What it covers | Status |
|---|---|---|---|
| 00 | [Setup and first request](notebooks/00_setup_and_first_request.ipynb) | Request flow, models, cost checks, response anatomy, errors | Ready |
| 01 | [Conversations and control](notebooks/01_conversations_and_control.ipynb) | Multi-turn chat, system prompts, streaming, stop sequences | Ready |
| 02 | Structured outputs | Validated JSON with Pydantic | Planned |
| 03 | Prompt evaluation | Test datasets, model and code graders | Planned |
| 04 | Prompt engineering | Clarity, specificity, XML tags and examples, each measured | Planned |
| 05 | Tool use | Schemas, the tool loop, multiple tools, streaming | Planned |
| 06 | Built-in tools | Text editor, web search, code execution, Files API | Planned |
| 07 | RAG I | Chunking, embeddings, semantic search | Planned |
| 08 | RAG II | BM25, hybrid search, reranking, contextual retrieval | Planned |
| 09 | Claude features | Thinking, images, PDFs, citations, prompt caching | Planned |
| 10 | Model Context Protocol | Building a server and a client | Planned |
| 11 | Agents and workflows | Chaining, routing, parallelization, agents | Planned |
| 12 | Claude Code and computer use | A guide to both | Planned |
| 13 | Capstone | A board-report assistant that combines the above | Planned |

## Staying within budget

Running these notebooks spends real money on your API account. Three limits keep that under control:

1. **A spend limit on your account. Set this first.** In the [Claude Console](https://platform.claude.com/settings/billing), open **Billing**, then under **Spend limits** click **Set limit**. Anthropic enforces it, so it covers everything on your account.
2. **A budget in each notebook.** Each notebook states its expected cost at the top. A small `track()` function in its setup prints the cost of every call and stops the notebook at `BUDGET_USD`.
3. **`max_tokens` on every call.** This limits how much a single answer can cost.

Every notebook is self-contained: its client, cost tracking and helper functions are all written in the notebook itself. Costs are worked out from list prices, which can change, so check the [pricing page](https://platform.claude.com/docs/en/about-claude/pricing).

## License

[MIT](LICENSE)
