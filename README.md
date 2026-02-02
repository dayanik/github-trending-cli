# 🚀 github-trending-cli

> A fast and minimal command-line tool to fetch and display the GitHub trending repos.
> 📌 Inspired by [a project idea from roadmap.sh](https://roadmap.sh/projects/github-trending-cli).

---

## ✨ Features

- 🔍 Retrieves trending public GitHub repositories  
- 🖥️ Simple terminal output
- ⚡ Lightweight and quick to install  

---

## 📦 Installation

> **Requires Python 3.13 or newer**

### 1. Install `pipx`  
_pipx_ lets you install and run Python CLI tools in isolated environments:

```bash
python3 -m pip install pipx
```

### 2. Install the project:

```bash
pipx install git+https://github.com/dayanik/github-trending-cli.git
```

---

## 🛠️ Usage

Run the CLI tool from anywhere using:

```bash
trend-repos --language python --duration month --limit 3
```

---

## 🧪 Development

In the project directory, create a virtual environment and install the project in editable mode:

```bash
uv sync
```

> `uv` is a fast Python package manager compatible with `pip` and `venv`.

---

## 📋 Requirements

- Python 3.13+
- requests >= 2.32.4
- rich>=14.3.2 -- python cli output modul

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for details.

---

## 👤 Author

- [Dayan Iskhakov](https://github.com/dayanik)