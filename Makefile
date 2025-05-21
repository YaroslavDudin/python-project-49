install:
	uv sync
package-install:
	uv tool install dist/*.whl
brain-games:
    uv run brain-games
brain-even:
	uv run run brain-even

brain-calc:
	uv run run brain-calc

brain-gcd:
	uv run run brain-gcd

brain-progression:
	uv run run brain-progression

brain-prime:
	uv run run brain-prime
 make lint:
	uv run ruff check brain_games