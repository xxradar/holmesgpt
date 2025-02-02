import os
import subprocess
import sys

# For relative imports to work in Python 3.6 - see https://stackoverflow.com/a/49375740
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

# This is patched by github actions during release
__version__ = "0.0.0"


def get_version() -> str:
    # the version string was patched by a release - return __version__ which will be correct
    if not __version__.startswith("0.0.0"):
        return __version__
    
    # we are running from an unreleased dev version
    try:
        # Get the latest git tag
        tag = subprocess.check_output(["git", "describe", "--tags"]).decode().strip()

        # Get the current branch name
        branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode().strip()

        # Check if there are uncommitted changes
        status = subprocess.check_output(["git", "status", "--porcelain"]).decode().strip()
        dirty = "-dirty" if status else ""

        return f"{tag}-{branch}{dirty}"
    
    except Exception:
        return f"dev-version"
