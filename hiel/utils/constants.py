PYTHON_GITIGNORE = """*.pyc
__pycache_/
.DS_Store
.env
ngrok
.vscode

*.egg-info

build
generated
dist

.tox
.coverage

.mypy_cache
meeple.json
sample.py
sample
logs
"""

PYTHON_EDITOR_CONFIG = """root = true

[*.py]
indent_style = space
indent_size = 4
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.md]
trim_trailing_whitespace = false
"""

JAVASCRIPT_GITIGNORE = """node_modules
sample
sample.js
.env
.vscode
yarn-error.log
.DS_Store
logs
"""

JAVASCRIPT_EDITOR_CONFIG = """root = true

[*.js]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.md]
trim_trailing_whitespace = false
"""
