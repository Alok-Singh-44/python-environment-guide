# python-environment-guide

To understand why virtual environments are a non-negotiable standard in professional Python development, it helps to look at exactly how Python handles packages by default, and the specific scenarios where skipping a virtual environment will break your code.

## Prerequisites
To set up a virtual environment, make sure Python and pip are already installed on your system.

To check them, type the following commands in your terminal:

```bash
python --version
# Output example: Python 3.12.1 (It might vary, but try to use the latest)

pip --version
# Output example: pip 26.0.1 from /usr/local/python/... (python 3.12)
```

## How to Set Up the Virtual Environment

### 1. Create the Environment
Run this command in your project directory to create a localized environment folder named `.venv`:
```bash
python -m venv .venv
```

### 2. Activate the Environment
* **Linux / macOS / GitHub Codespaces (Bash):**
  ```bash
  source .venv/bin/activate
  ```
* **Windows (Command Prompt):**
  ```cmd
  .venv\Scripts\activate
  ```

Once activated, you will see a `(.venv)` tag appear at the beginning of your terminal line like this:
```bash
(.venv) @Alok-Singh-44 ➜ /workspaces/python-environment-guide
```

## Interactive Testing Scripts Included

This repository contains two scripts to help you see the environment in action:

1. **`main.py`**: Tests if a package (`requests`) is isolated inside your virtual environment. If you deactivate the environment, this script will fail—proving isolation works!
