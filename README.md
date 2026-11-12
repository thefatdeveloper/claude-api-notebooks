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

Notebooks 07 and 08 also need a free [Voyage AI](https://www.voyageai.com/) key for embeddings. Add it to `.env` as `VOYAGE_API_KEY`.

## Learning path

| # | Notebook | What it covers | Needs | Expected cost |
|---|---|---|---|---|
| 00 | [Setup and first request](notebooks/00_setup_and_first_request.ipynb) | Request flow, models, cost checks, response anatomy, errors | Anthropic key | About $0.005 |
| 01 | [Conversations and control](notebooks/01_conversations_and_control.ipynb) | Multi-turn chat, system prompts, streaming, stop sequences | Anthropic key | About $0.02 |
| 02 | [Structured outputs](notebooks/02_structured_outputs.ipynb) | Validated JSON with Pydantic | Anthropic key | About $0.01 |
| 03 | [Prompt evaluation](notebooks/03_prompt_evaluation.ipynb) | Test datasets, model and code graders | Anthropic key | About $0.11 |
| 04 | [Prompt engineering](notebooks/04_prompt_engineering.ipynb) | Clarity, specificity, XML tags and examples, each measured | Anthropic key | About $0.29 |
| 05 | [Tool use](notebooks/05_tool_use.ipynb) | Schemas, the tool loop, multiple tools, streaming, the tool runner | Anthropic key | About $0.07 |
| 06 | [Built-in tools](notebooks/06_built_in_tools.ipynb) | Text editor, web search, code execution, Files API | Anthropic key, web search enabled | Under $0.15 |
| 07 | [RAG basics](notebooks/07_rag_basics.ipynb) | Chunking, embeddings, semantic search | Anthropic and Voyage keys | Under $0.05 |
| 08 | [RAG advanced](notebooks/08_rag_advanced.ipynb) | BM25, hybrid search, reranking, contextual retrieval | Anthropic and Voyage keys | Under $0.15 |
| 09 | [Claude features](notebooks/09_claude_features.ipynb) | Thinking, images, PDFs, citations, prompt caching | Anthropic key | Under $0.30 |
| 10 | [Model Context Protocol](notebooks/10_model_context_protocol.ipynb) | Building an MCP server and client | Anthropic key | About $0.03 |
| 11 | [Agents and workflows](notebooks/11_agents_and_workflows.ipynb) | Chaining, routing, parallelization, evaluator-optimizer, agents | Anthropic key | About $0.08 |
| 12 | [Claude Code and computer use](notebooks/12_claude_code_and_computer_use.ipynb) | A guide to both, plus plugging in your own MCP server | Anthropic key | Free |
| 13 | [Capstone: board assistant](notebooks/13_capstone_board_assistant.ipynb) | A cited, self-checking assistant that combines the series | Anthropic key | Under $0.20 |

"About" costs were measured on a real run. "Under" costs are estimates, and each notebook prints its real spend as it runs. Running every notebook once costs roughly $1 to $1.50.

## Staying within budget

Running these notebooks spends real money on your API account. Three limits keep that under control:

1. **A spend limit on your account. Set this first.** In the [Claude Console](https://platform.claude.com/settings/billing), open **Billing**, then under **Spend limits** click **Set limit**. Anthropic enforces it, so it covers everything on your account.
2. **A budget in each notebook.** Each notebook states its expected cost at the top. A small `track()` function in its setup prints the cost of every call and stops the notebook at `BUDGET_USD`.
3. **`max_tokens` on every call.** This limits how much a single answer can cost.

Every notebook is self-contained: its client, cost tracking and helper functions are all written in the notebook itself. Costs are worked out from list prices, which can change, so check the [pricing page](https://platform.claude.com/docs/en/about-claude/pricing).

## License

[MIT](LICENSE)
