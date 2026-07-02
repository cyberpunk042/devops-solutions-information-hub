#!/usr/bin/env python3
"""Referential-integrity gate for wiki/config/model-catalog/ (thin alias).

The logic lives in ``tools.model_catalog``; this remains as the documented entry
point. Equivalent to ``python3 -m tools.model_catalog validate``.
"""

from __future__ import annotations

import sys

from tools.model_catalog import main

if __name__ == "__main__":
    sys.exit(main(["validate"]))
