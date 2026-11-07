# What is This?

This is meant to be both a guide of how to get started contributing for SS14 and an introduction to development as a whole. The end goal is that you not only have successfully made a pull request (PR), but that you also have a decent understanding of what, why, and how you do so.

People with any sort of development experience may find sections of this guide redundant; please keep in mind that it is written with new developers in mind.

## What's in This Guide?

This primarily focuses on introducing the tools you will be using to create a PR, rather than the nitty gritty of developing as a whole. Please consider looking at WizDen's [developer docs](https://docs.spacestation14.com/index.html) if you want to learn more about the finer details.

## Prerequisites

You will need:
- [Git](https://git-scm.com/downloads)
    - There's many third-party visualizers to make working with Git a little easier. You can try them out if you want, but this will guide you through the basic commands before that. I recommend learning the very basic commands, then switching to a visual program later.
- A [GitHub](https://github.com/) account
- The [.NET 9.0 SDK](https://dotnet.microsoft.com/download/dotnet/9.0)
- [Python](https://www.python.org/downloads/)
    - Note that Python is notoriously finicky to install on Windows, there's issues with the Microsoft store and downloading it through the python website. You *can* go through a bunch of stuff to try and fix this, but there's one thing you need to use Python for. If this is your first time ever doing development work, I recommend just skipping the Python install.
- Optionally, an Integrated Development Environment (IDE). Either of the following will work:
    - [Rider](https://www.jetbrains.com/rider/) is the one most SS14 developers use. It's a bit heavier, so low-end computers might struggle to run it, but it will make your life a lot easier.
    - For Windows exclusively, [Visual Studio 2026 Community](https://visualstudio.microsoft.com/). When you install it, you at-minimum need the .NET desktop development workload, the C# compiler, C# support, NuGet package manager, MSBuild and the .NET 10 SDK (look in the individual components tab rather than the workloads). Probably. I don't use this.
    - [Visual Studio Code](https://code.visualstudio.com/) with the C# extension.
    - [Visual Studio Codium](https://vscodium.com/) with the C# extension.
        - For VS Code and VS Codium there's the [Robust YAML](https://marketplace.visualstudio.com/items?itemName=slava0135.robust-yaml) and [YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) extensions. They'll make your life easier, so consider installing them too.
        - Yes I know three of these all start with the words "Visual Studio." Yes it is confusing. If you pick one of those, remember which one it specifically is so we can help you later.
    - Notepad++ / Notepad / VIM / Nano / Whatever
        - If you want something that just shows you the text in a file, you can just use whatever. It works. I guess.

## Setting Up A Development Environment

Now, you're going to clone the repository. This is basically installing everything, we're doing it in a fancy way so that we can later use Git to communicate our changes to other people. You also have to do it this way because downloading the straight files off of Github does not include any submodules (think of the engine--it's connected to the files, but doesn't inherently come with them) or other libraries.

First, navigate to the [Funky Station GitHub repository](https://github.com/funky-station/funky-station).

In the top right of your screen, you'll see a button labelled "Fork." Click it, then "Create a New Fork." Name it whatever you want.
[asset]

Once it completes, you should see a new repository on your account. Click on the green Code button, select Local, HTTPS, and copy the URL in the box.
[asset]

Open a new explorer window (or whatever file manager you have), and create a new folder. You can call it `development` or `funkystation` or whatever you want. If you're on Windows, do NOT put this into any sort of OneDrive folder. OneDrive likes to Do Things to development environments, you should disable it or put your files somewhere else.

Go into the folder, and create a terminal window. If you've installed Git for Windows, then you can Right Click and then select `Open Git Bash Here`, and it will create a terminal window for you.

In this terminal window, ensure the `path` ends in the folder you just made. For example, if you named your folder `funkystation` and put it in your Documents, then it should say `~Documents/funkystation` in your terminal.

In your terminal window, type `git clone <your repo url here>`. Then, type `cd <your repo name>`. When you clone something, it creates a new folder with your repository's name. To keep going, we need to point our terminal to the folder it just created, not the one we're still in.

Let that work, if it errors, reread the guide and make sure you followed all the steps.

Next, we need to get all of the submodules and extra files we need to be able to build the game. If you install python, you can either do `python RUN_THIS.py` in your terminal or run it through your file explorer (double click the file!). If you didn't install python, don't worry! It does two commands that we can just do ourselves. In your terminal, run `git submodule update --init --recursive`.

Congratulations! It's completed.

If you just want to run a local host, you can either use the scripts or the command line. `runserver` and `runclient` (use one ending in `.bat` if you're on Windows, and `.sh` if you're on Linux) will run everything for you.

```admonish warning
If you get any errors about Robust Toolbox not being found, make sure you've ran RUN_THIS.py or it's related command recently. Robust Toolbox is a submodule, so it isn't included when you do a fresh clone. 
```
