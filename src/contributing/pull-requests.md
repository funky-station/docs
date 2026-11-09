# Pull Requests

A *pull request* is a way for you to showcase your changes and ask for them to be merged into the main codebase. You are *requesting* that your changes be *pulled.* 

The last section of *Branching* tells you how to navigate Github and start your actual pull request. From here, you can select which branch you are PRing to. By default it is Funkystation's master branch, and you usually want to keep that the same. 
You can also see the *diff* (the difference in files between your changes and the original codebase) here. Please make sure to review this, as you don't want any other changes sneaking into your PR. 

Similarly, you'll want to fill out the description of your actual PR. Each section has an explanation in its comments, which are the sections enclosed with `<!-- -->`. PRs are more likely to be reviewed and merged if these sections are properly filled. 

## Changelog Formatting

Enclosed in comments is a sample changelog for your usage. Please make sure your changelog is formatted completely correctly, otherwise it won't appear in game.

```
🆑 Username
- add: 
- remove: 
- tweak: 
- fix: 
```

For the username section, please make sure there are no special characters at all. Hyphens and exclamation points will break the changelog. You can also leave it blank if you prefer it to autofill your Github username. 

Use the corresponding prefixes to properly describe what you did. Don't be afraid to remove or add certain ones.

## Reviews

Maintainers will check for the following things before merging a PR:
1. A description that properly descibes the feature and why you are PRing it.
2. A properly made changelog.
3. If the feature adheres to our design goals.
   1. Large features need a corresponding design document.
4. All tests passed, including CRLF checks, YAML parsing, unit tests, etc.
   1. Large features must have their own unit tests to make sure everything properly works.
5. No AI code.
6. Code quality and practices: if the up-to-date and correct methods are used, no redundant code, etc.
   1. The [codebase conventions](contributing/codebase-conventions.md) must be adhered to.
