# Why not use Github's Web Editor?
I know it's tempting. Especially if you know that the change you want to make doesn't deal with actual C# code; maybe you want to fix a typo or rewrite one of the guidebook pages. Something small. 

**PLEASE DON'T!!!!!!!!!!!**

Part of this is for future proofing--learning how to use these tools on a small change helps prepare you to do larger changes later. Just because your changes are small now doesn't mean they will be later. 

The web editor, and Github in general, can not handle large changes. Plus, changes you might think are small might be larger than you think. As an example, try to open the 'Files Changed' tab of a PR that changes maps. Usually it crashes. 

Github also likes to fuck up files if you try to upload them through Github, rather than setting up a local host and doing all of this. Things like images getting lossy, audio getting bit crushed, et cetera. It sucks.
# Creating a Local Host
Please see Getting Started for information on how to get a local host on your computer. If you have an issues with this guide, you are always free to ask us in the Discord!

Similarly, if you want a more detailed version of the same guide, consider reading WizDen's [Setting up a Development Environment](https://docs.spacestation14.com/en/general-development/setup/setting-up-a-development-environment.html)

# Running a Local Host
At the end of Getting Started, you run `runserver.bat` and `runclient.bat` to run your local host. This works fine, but sometimes issues arise with these default settings. 

Most commonly, these two files open your local host in *Debug*. There are other .bat files to open your local host in different configurations (modes), however, there are other ways to do this that are generally a little better.

The most common way is to use your IDE (integrated developer environment, the program you use to code) of choice. Use your IDE to open `SpaceStation14.sln` and then navigate to the build button. In Jetbrains Rider, it's in the top right. 

If you don't have an IDE, you can also use command line to run and configure a local host. Git Bash works for this, just make sure you are in the correct directory. Then run:

- `dotnet build`
- `dotnet run --project Content.Server`
- `dotnet run --project Content.Server`

If you want to run your local host in a different configuration, add `--configuration Release/Debug/Tools` at the end of the two run commands. 
# Updating a Local Host

Assuming you followed the guide in Getting Started, you can just press the "Sync Fork" button on Github's website. Then it updates your fork! Yay! 

If you prefer to update things manually, then you can also add a *remote* to fetch and merge into your local version. Make sure you are on your master branch while doing this. 

A remote is a way for Git to know to go to that specific repository (a codebase) and grab changes and code from there. In this case, you'll need to add a remote for Funkystation's Github. You can do this in Git Bash by running:

- `git remote add funkystation https://github.com/funky-station/funky-station.git`

You can change `funkystation` to anything you want. This is just the name of the remote, so pick something you can remember easily! 

If you need to add a remote for a different repository (such as Wizden or Goobstation), you can run the same command with the name and link changed. The link you want can be acquired by going to the repository's Github page, clicking the green "Code" button and then copying the link there. 

After this, you need to *fetch* the remote. Fetching something means you are telling Git to go get everything on the remote and hold onto it:

- `git fetch funkystation`

Git Bash will spit out a lot of lines at you, assuming it's been a little while since you last updated your local host. This is good! If you get nothing, then that's also fine. It means whatever Git Bash is holding onto is up to date with Funkystation's repository. 
If you get an error, usually the error message is pretty obvious with what's wrong. If it's something like "Remote not found!" then make sure you typed in the name correctly. 

Then, you need to *merge* the remote into your local code:

- `git merge funkystation/master`

Notice the addition of `/master`! This just means that you are telling Git to merge specifically the master branch (the main code) of Funkystation into your code. There are other branches in Funkystation's repository, which we generally don't want. Git Bash will tell you it's updating, and then it's done! 