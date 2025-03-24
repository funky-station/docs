# Getting Started

```admonish warning
If you get some strange issues with Windows regarding Python, be sure to check these two during your Python install.
<img src="/assets/getting-started/python_for_windows.png" width=512 style="margin-left:auto;margin-right:auto;display:block"/>
```

This guide assumes you have [Git](https://git-scm.com/downloads), a [GitHub](https://github.com/) account, [Python](https://www.python.org/downloads/) and the [.NET 9.0 SDK](https://dotnet.microsoft.com/download/dotnet/9.0).
If you don't, it's fine, just go ahead and follow the links, select your platform, and watch the installers whirr. For GitHub, make an account if you don't have one already.

Navigate to the [Funky Station GitHub repository](https://github.com/funky-station/funky-station), click on Fork on the right side of your screen. Name your fork whatever you want.
Once it completes, you should see a new repository on your account. Click on the green Code button, select Local, HTTPS, and copy the URL in the box. 
Congratulations, you now have your very own development build of Funky Station.

Let's get it on your machine. Open a new explorer window (or whatever file manager you have), and create a new folder called `funkystation`.

Go into the folder, and create a terminal window. If you've installed Git for Windows, then you can Right Click and then select `Open Git Bash Here`, and it will create a terminal window for you.

In this terminal window, ensure the `path` ends in `/funkystation`. If it does, amazing, keep going. If not, double check you've created the folder, and have navigated to the folder in your terminal window.

In your terminal window, type `git clone <your repo url here> .` (without the <>, and paste in the URL we just copied earlier) **(AND REMEMBER THE PERIOD AT THE END)**. Let that work.

After it's done (you'll know when), type `python RUN_THIS.py`. Let that work, if it errors, reread the guide and make sure you followed all the steps.

Congratulations, it's completed. To open a development build of Funky Station, you can now run the `runclient.bat` file, as well as the `runserver.bat` file to get a local server and client up.

```admonish warning
If you are using Windows and you get the following error:
"Python was not found; run without arugments to install from the Microsoft Store,
or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases"

Fuck Microsoft. Go into the settings it tells you to and disable the duplicate execution alias. 
Or just double click RUN_THIS.py. Whatever works. 
```