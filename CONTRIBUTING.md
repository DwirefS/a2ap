# Contributing to A2AP

Thank you for your interest in contributing to the Agent-to-Agent Protocol (A2AP)!

## How to Contribute

1. **Fork the Repository**  
   Click the 'Fork' button on GitHub and clone your fork:

   ```bash
   git clone https://github.com/your-username/a2ap.git
   cd a2ap
   ```

2. **Set Up Your Environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Create a Feature Branch**

   ```bash
   git checkout -b feature/my-new-feature
   ```

4. **Make Your Changes**  
   Ensure you write or update tests and run:

   ```bash
   pytest
   ```

5. **Lint Your Code**

   ```bash
   black .
   ```

6. **Commit and Push**

   ```bash
   git add .
   git commit -m "feat: describe your feature"
   git push origin feature/my-new-feature
   ```

7. **Open a Pull Request**  
   Go to the GitHub repo and create a PR. Add context and link to issues.

---

## Code Style
- Python 3.10+
- PEP8 + Black formatting
- Descriptive commit messages
- Include docstrings and type hints

---

## Communication

- GitHub Discussions: [A2AP Repo](https://github.com/DwirefS/a2ap/discussions)
- Discord Community: (Coming soon)

Happy contributing!
