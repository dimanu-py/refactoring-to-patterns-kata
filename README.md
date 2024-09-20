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

## Learnings:

1. Compose method pattern

We begin extracting methods from the deepest branches of the method because they are the most decoupled from the rest of the code.

The initial methods leaves as an orchestration method that calls the extracted methods. By doing this we are giving a high level semantic to
the method, making it easier to understand. If we want to understand the details of the method, we can go to the extracted methods.


### Visit my GitHub profile to see all solved katas 🚀

[![Web](https://img.shields.io/badge/GitHub-Dimanu.py-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/dimanu-py/code-katas)