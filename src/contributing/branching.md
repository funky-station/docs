# What Next?
So you've got a nice and updated local host, then obviously you want to jump in and figure out coding and your changes. However... you're not quite there yet! 

If you make changes now, you'll be doing so on your *master branch.* Your PR will automatically be closed if it comes from your master branch, so first, you need to figure out how to use Git and make a new *branch.*

If you want a more in depth explanation of Git, please see Wizden's [Git for the SS14 Developer](https://docs.spacestation14.com/en/general-development/setup/git-for-the-ss14-developer.html). This also has some information on how to use TortoiseGit and SmartGit, if you prefer those over Git Bash. 

```admonish warning
DO NOT SUBMIT PRS FROM YOUR MASTER BRANCH. 

Your PR will be closed automatically if you submit from your master branch. 

It can also cause issues for you later, so don't do it! PLEASE!!

```
# What is a Branch?

A branch another copy of your codebase, which you make your changes onto. You are "branching" off of the main tree in order to develop and test your changes. When these changes are done, we can then merge them into the main branch--also known as a *pull request.* 

We do this in order to help organize development. If you end up doing multiple projects at once, or even something like a minor bug fix while you are working on something else, branches help keep everything neat and separate. If you prefer to see things visually, there are many resources online explaining branches with visual guides. 

# Working with Git
Now, you have to actually make a branch. To get started, open Git Bash in your directory (the /funkystation/ folder created prior). Unless you've worked with Git Bash before, this will open it on your master branch. You can tell what branch Git Bash is currently on by the cyan text in parenthesis, it should say "(master)."


The first command you need to know is `git checkout`. This is how you move between branches, you are checking out from one to the other. To make a new branch, you can simply do:

- `git checkout -b branch-name`

The -b tag means you want to make a new branch. You can replace `branch-name` with anything you want, just make sure it's unique. 

After that... You're on a new branch! You can actually start coding now. After you finish your work, or need to save your work, you'll need to do two commands to *commit* your changes:

- `git add -A`

This "stages" the files to be committed. Basically you're telling Git that these are the files you edited and *want* to commit. The -A tag means all files, but you can remove it and individually add files for staging if you prefer.

- `git commit -m "commit message here"`

A commit basically an entry in your log of changes. The -m tag is so Git knows that you're attaching a message to the commit. If you don't add the tag, Git will probably open VIM (or whatever command line text editor you have installed. If you don't know what that is, it's probably VIM). 

The message is so you know what was edited at a glance, but Git helpfully saves detailed information about what was edited in a commit. 

```admonish warning
HELP IT OPENED VIM!!
VIM looks like some yellow text on top, a bunch of blue text, and a fuck ton of ~s everywhere. 

It's terrible to use and you'll probably struggle to use it without someone telling you how to.

First, see if it says "---INSERT---" at the bottom. If it does, great, if it doesn't, press `i`.

Then type your commit message, press escape, and then type `:x`. Then boom! VIM is gone!
```


After you've finished all of your changes and committed them, the last step is to push them to your origin, GitHub:

- `git push origin branch-name`

Origin refers to Github, and `branch-name` would be the name of your current branch. After you do this, go to Github's website find your forked repository (you can click your PFP and then "My Repositories"). 

Usually a nice little popup that says that the branch you were just working on had new changes. You can click "make a pull request" from there, or navigate to your branches and do the same thing. 
Then, you can make a pull request!