
# Lab 5 — Reflection

## 1. What is static code analysis, and how is it different from testing?

Static code analysis examines source code without executing the program as part of the analysis. It can identify potential security vulnerabilities, programming mistakes, and style violations early in development. Testing executes the program to check its behaviour for particular inputs and scenarios. Both approaches complement one another because static analysis cannot establish that every possible execution behaves correctly.

## 2. What are the differences between Pylint, Bandit, and Flake8?

Pylint focuses on code quality, programming practices, documentation, naming conventions, and potential logical problems. Bandit focuses on identifying potentially insecure Python coding patterns. Flake8 checks style and formatting issues and detects certain programming errors. Using all three provides broader coverage than relying on only one tool.

## 3. Which issues were important, and how were they resolved?

The most significant issues included unsafe SQL string construction and the use of `eval()`. SQL queries were changed to use parameterized statements. The unrestricted evaluator was replaced with an AST-based arithmetic evaluator that permits only explicitly supported numeric operations. A mutable default list was replaced with a `None` default and a fresh list per call. Broad exception handling, inconsistent return behaviour, missing documentation, and style violations were also addressed.

## 4. How did static analysis improve the program?

Static analysis provided actionable findings that helped improve security, readability, maintainability, and consistency. Running the tools again after the fixes allowed the changes to be verified against the original findings. The exercise also demonstrated that clean tool reports are useful evidence of code quality, although they do not replace functional testing or a security review.
