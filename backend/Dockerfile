FROM python:3.13-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app/backend
COPY . .

# COPY pyproject.toml uv.lock ./
RUN uv sync --frozen
ENV PATH="/app/backend/.venv/bin:$PATH"
ENV PYTHONPATH="${PYTHONPATH}:/app/backend"

CMD ["/app/backend/.venv/bin/fastapi", "run", "app.py", "--port", "8000", "--host", "0.0.0.0"]
