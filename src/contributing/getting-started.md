# Getting Started

This guide assumes you have [Git](https://git-scm.com/downloads), a [GitHub](https://github.com/) account and the [.NET 9.0 SDK](https://dotnet.microsoft.com/download/dotnet/9.0).
If you don't, it's fine, just go ahead and follow the links, select your platform, and watch the installers whirr. For GitHub, make an account if you don't have one already.

Navigate to the [Funky Station GitHub repository](https://github.com/funky-station/funky-station), click on Fork on the right side of your screen. Name your fork whatever you want.
Once it completes, you should see a new repository on your account. Click on the green Code button, select Local, HTTPS, and copy the URL in the box. 
Congratulations, you now have your very own development build of Funky Station.

Let's get it on your machine. Open a new explorer window (or whatever file manager you have), and create a new folder called `funkystation`.

Go into the folder, and create a terminal window. If you've installed Git for Windows, then you can Right Click and then select `Open Git Bash Here`, and it will create a terminal window for you.

In this terminal window, ensure the `path` ends in `/funkystation`. If it does, amazing, keep going. If not, double check you've created the folder, and have navigated to the folder in your terminal window.

In your terminal window, type `git clone <your repo url here> .` (without the <>, and paste in the URL we just copied earlier) **(AND REMEMBER THE PERIOD AT THE END)**. Let that work.

Let that work, if it errors, reread the guide and make sure you followed all the steps.

Congratulations, it's completed. To open a development build of Funky Station, you can now go to the `Scripts` folder. If you are on Windows, use the bat files, and if you are on Linux, use the sh files. Run `buildAll...` first, then `runQuickAll` to get a build working. Use `buildAllDebug` if you need to quickly load into a developer environment to test specific features, `buildAllTools` if you are mapping, and `buildAllRelease` if you need to test something in a simulated round. 

```admonish warning
If you get any errors relating to Robust Toolbox, such as it not being found or on the wrong version, make sure you have used one of the build scripts recently.
Robust Toolbox does not get cloned with the primary repository, since it is a submodule.
The build scripts will automatically install and update it, but you can also run the command "git submodule update --init --recursive" to update it manually.
```
