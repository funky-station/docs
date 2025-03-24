# Pull Requests

A *pull request* is a way for you to showcase your changes and ask for them to be merged into the main codebase. You are *requesting* that your changes be *pulled.* A little bit of a confusing term if you don't know the prerequisite jargon. 

The last section of *Branching* tells you how to navigate Github and start your actual pull request. From here, you can select which branch you are PRing to. By default it is Funkystation's master branch, and you usually want to keep that the same. 
You can also see the *diff* (the difference in files between your changes and the original codebase) here. Please make sure to review this, as you don't want any other changes sneaking into your PR. 

Similarly, you'll want to fill out the description of your actual PR. Each section has an explanation in its comments, which are the sections enclosed with `<!-- -->`. PRs are more likely to be reviewed and merged if these sections are properly filled. 
# Changelog Formatting

Enclosed in comments is a sample changelog for your usage. Please make sure your changelog is formatted completely correctly, otherwise it won't appear in game.

The format is as follows: 
```
🆑Username
- add: 
- remove: 
- tweak: 
- fix: 
```

For the username section, please make sure there are no special characters at all. Hyphens and exclamation points will break the changelog. You can also leave it blank if you prefer it to autofill your Github username. 
# Reviews

Once we receive a properly made PR, the maintainers will review your PR! We first look at things like test fails (CRLF check, YML linter, Content.Integration tests). Any related test fails will have to be corrected prior to being merged. 

If the tests pass, great! We then review the code, discuss how it would impact the server, and then we either request changes, merge the PR, or close the PR. If you would like to know more about why or why not a PR was merged, please see our Design Principles. 