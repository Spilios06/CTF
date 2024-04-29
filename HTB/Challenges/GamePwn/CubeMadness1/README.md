# First look at things

First I saw that there is a game executable so I tried running it, additionally I saw a UnityCrashHandler file so I knew we were working with Unity and IL2CPP.

# Understanding the game

The game is a mini 2D platformer in which you collect boxes, as shown by the indicator on the screen the player is meant to collect 20 boxes but only 5 can be found within the bounds of the map. I loaded up CheatEngine to see whether I could simply find and modify the address at which the box counter was kept at.

# Solution

Indeed it was as simple as doing a handful of scans in order to find the correct address, modifying it to 20 and the flag appeared on the background. Below is a screenshot from Cheat Engine with the box counter address.

<img src="CheatEngineScreenshot.png ">