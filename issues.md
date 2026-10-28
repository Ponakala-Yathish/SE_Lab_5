
# Lab 5 — Static Code Analysis

## Project
Society Dues Management (`society_dues.py`)

## Tools Used
- Pylint — code quality and programming practices
- Bandit — security analysis
- Flake8 — style and formatting

## Issue Analysis and Fixes

| Issue | Type | Original line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Unsafe SQL construction | Security | 9 | User-provided values were inserted directly into an SQL statement, potentially allowing SQL injection. | Replaced string interpolation with parameterized SQL queries. |
| Unsafe `eval()` | Security | 21 | `eval()` could execute arbitrary Python code supplied as an expression. | Replaced it with an AST-based evaluator that permits only specified arithmetic operators and numeric constants. |
| Hardcoded password | Security | 5 | A password-like string was stored directly in the source code and was not used by the program. | Removed the unused hardcoded credential. |
| Mutable default argument | Bug / code quality | 8 | The default list could be shared across calls, causing unexpected history reuse. | Changed the default to `None` and initialized a new list inside the function. |
| Broad exception handling | Code quality | 22 | Catching every `Exception` could hide unexpected programming errors. | Restricted exception handling to expected parsing and arithmetic errors. |
| Inconsistent return statements | Code quality | 12–17 | The collection function returned an amount when a record existed but implicitly returned `None` otherwise. | Added an explicit `return None` for a missing due. |
| Missing docstrings | Code quality | Multiple | The module and functions lacked documentation. | Added a module docstring and function docstrings. |
| Invalid function naming | Style | 8 | `addDue` did not follow the conventional `snake_case` style. | Renamed it to `add_due` and updated its call sites. |
| Long lines and spacing | Style | 4, 12–15 | Some lines exceeded style limits and function spacing was inconsistent. | Reformatted SQL statements and function definitions. |
| Unnecessary `None` comparison | Style / code quality | 29 | The code compared a `fetchall()` result with `None`, although it returns a list. | Returned the list of unpaid flats directly. |
| Unconditional demonstration execution | Maintainability | 42 | Importing the module executed the demonstration immediately. | Added a `__main__` guard. |

## Verification

The original reports are saved separately from the after-fix reports.

- Original Pylint score: 5.81/10
- Original Pylint score: 5.81/10
- Final Pylint score: 10.00/10
- Final Bandit result: No issues identified.
- Final Flake8 result: No violations reported.

The updated program was executed successfully, and the expected demonstration output was preserved.

Only mark the findings as resolved after confirming the corresponding after-fix reports.
