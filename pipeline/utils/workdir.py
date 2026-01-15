import os
from pathlib import Path

def get_workspace():
    """Returns a writable workspace path. Prefer environment override AI_BOARD_WORKDIR, otherwise use current working directory."""
    return os.environ.get("AI_BOARD_WORKDIR", os.getcwd())

# Legacy compatibility functions for notebooks
CONTENT_DIR = Path(os.environ.get("NBDEV_CONTENT_DIR", os.environ.get("CONTENT_DIR", get_workspace() / "content")))
CONTENT_DIR.mkdir(parents=True, exist_ok=True)

def get_content_path(*path_parts):
    """Get a path within the content directory."""
    return CONTENT_DIR.joinpath(*path_parts)

def ensure_content_dir(*path_parts):
    """Ensure a subdirectory exists within the content directory."""
    path = get_content_path(*path_parts)
    path.mkdir(parents=True, exist_ok=True)
    return path
