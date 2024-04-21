set -e

python3 -m venv .venv
source .venv/bin/activate

reflex run --loglevel debug
