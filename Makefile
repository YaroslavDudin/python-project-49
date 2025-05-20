install:
	uv sync
package-install:
	uv tool install dist/*.whl
brain-games:
    uv run brain-games
 make lint:
	uv run ruff check brain_games