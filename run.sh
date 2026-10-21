#!/bin/bash
set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log_info() { echo -e "${GREEN}[INFO]${NC} $*"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $*"; }
log_err()  { echo -e "${RED}[ERR]${NC}  $*"; }

# Project root
cd "$(dirname "$0")"

# ---- 1. Start Docker dependencies (chromadb, searxng, ntfy) ----
# log_info "Starting Docker services (chromadb, searxng, ntfy)..."
# docker compose up -d chromadb searxng ntfy
#
# # ---- 2. Wait for ChromaDB to be ready ----
# log_info "Waiting for ChromaDB on localhost:8100..."
# for i in {1..30}; do
#     if curl -sf http://localhost:8100/api/v2/heartbeat >/dev/null 2>&1; then
#         log_info "ChromaDB is ready"
#         break
#     fi
#     sleep 1
#     if [[ $i -eq 30 ]]; then
#         log_err "ChromaDB failed to start after 30s"
#         exit 1
#     fi
# done
#
# # ---- 3. Wait for SearXNG to be ready ----
# log_info "Waiting for SearXNG on localhost:8080..."
# for i in {1..60}; do
#     if curl -sf http://localhost:8080/ >/dev/null 2>&1; then
#         log_info "SearXNG is ready"
#         break
#     fi
#     sleep 1
#     if [[ $i -eq 60 ]]; then
#         log_warn "SearXNG not ready after 60s (search may not work)"
#         break
#     fi
# done

# ---- 4. Verify Ollama is running for embeddings ----
# log_info "Checking Ollama for embeddings on localhost:11434..."
# if curl -sf http://localhost:11434/api/tags >/dev/null 2>&1; then
#     log_info "Ollama is reachable"
#     # Check if an embedding model is available
#     if curl -sf http://localhost:11434/api/tags | grep -qiE 'all-minilm|nomic-embed|bge|e5|mxbai'; then
#         log_info "Embedding model detected in Ollama"
#     else
#         log_warn "No obvious embedding model found in Ollama. You may need: ollama pull nomic-embed-text"
#     fi
# else
#     log_warn "Ollama not reachable on localhost:11434 — embeddings will fall back to FastEmbed (local ONNX)"
# fi

# ---- 5. Activate venv and start Odysseus ----
# APP_PORT must match the uvicorn port: in-process loopback tools
# (src/tools/_common.py -> internal_api_base) dial 127.0.0.1:$APP_PORT.
# Without it they default to 7000 and fail with "All connection attempts
# failed" whenever the server runs on any other port.
log_info "Activating venv and starting Odysseus on 127.0.0.1:7001..."
source venv/bin/activate
export APP_PORT=7001
exec python -m uvicorn app:app --host 127.0.0.1 --port "$APP_PORT"
