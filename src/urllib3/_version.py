# Pinned by ActiveState for the 2.6.3.x security line (package version
# 2.6.3.post2, see pyproject.toml). Kept at three components on purpose:
# requests unpacks urllib3.__version__ as major.minor.patch and emits
# RequestsDependencyWarning for anything longer.
from __future__ import annotations

__version__ = version = "2.6.3"
__version_tuple__ = version_tuple = (2, 6, 3)

__commit_id__ = commit_id = None
