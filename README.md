# :wrench: Refactoring to Patterns :wrench:

[![Python](https://img.shields.io/badge/Python-3.12+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)

## Resources

These instructions where extracted from Raul Villares GitHub. The link to the original instructions can be found in the link bellow.

[![Web](https://img.shields.io/badge/GitHub-raulvillares-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/raulvillares/refactoring-to-patterns/tree/master)

## Description

The idea of the following exercise is to get experience with real life scenarios, where we don't apply directly a design pattern to a solution,
but we refactor the code to make a pattern emerge.

1. Compose method: we have a very large method that has many responsibilities. We want to refactor the code to be able to apply 
the Compose method pattern, which consist in breaking the method into smaller methods and call them from the main method.
2. Creation method: we have a class that can combine different parameters when being created. We want to refactor the code to be able to add
new combinations without creating a new constructor.
3. Command pattern: we have a method tha process commands with several if-else statements. We want to refactor the code to be able to apply
the Command pattern, which consist in creating a class for each command and call the execute method.

## Objective

The main objective is to apply design patterns and apply automatic refactors when possible.

## Configuration

The project can be configured with `pdm`.

1. Install pdm:
    ```bash
    pip install pdm
    ```
2. Install required python version:
    ```bash
    pdm python install 3.12
    ```
3. Create a virtual environment and install dependencies:
    ```bash
    pdm install
    ```
   It will create the .venv folder inside the project automatically.
4. You can activate the virtual environment manually running `source .venv/bin/activate` on Unix systems or `source .venv/Scripts/activate` on Windows.

## Running the tests

To run the tests, execute one of the following commands:

```bash
pytest
```

or

```bash
pdm run pytest
```

## Learnings

### Visit my GitHub profile to see all solved katas 🚀

[![Web](https://img.shields.io/badge/GitHub-Dimanu.py-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/dimanu-py/code-katas)