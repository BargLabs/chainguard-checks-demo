# chainguard-checks-demo

A small public repository used by Barg Labs to test how [Dunstan](https://github.com/BargLabs/dunstan) checks a coding agent's report of its work against a pull request whose CI runs on [Chainguard Checks](https://www.chainguard.dev/docs/chainguard/checks).

Chainguard Checks runs the CI in isolated microVMs and reports the results on the pull request as GitHub checks. Dunstan reads those check runs as the record when it settles an agent's claim that "all checks passed".

Nothing here is production code.
