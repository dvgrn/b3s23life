Test walkthrough:

* Run populate-sample-library.py in Golly . This should report that it has populated the recognizer-library folder.
* Run create-G-to-W-to-G.py . This should display a working glider-to-weekender-to-glider converter.
* Run recognizer1.3.py. This should progressively recognize and erase all the pieces of the G-to-W-to-G pattern, starting at the top.
* Optionally, re-run populate-sample-library.py, then add one or more new objects to the pattern -- blinkers, let's say.
* Run recognizer1.3.py.  It will fail to recognize the blinkers-or-whatever that you added.
* Select a blinker, then run register-selection.py and type in "blinker" (or the name of whatever you added).
  No need to specify ticks to run or match type --
  that's only if you want to recognize something non-oscillatory,
  like all the phases of a pi explosion or something like that.
  Another example is that *glider* is defined in the library with maxticks = 1,
  because if you have the 0 and 1 phases of a glider,
  you can recognize (some rotation or reflection of) any glider you might encounter.
* The optional *matchtype* parameter defaults to 0,
  meaning it will recognize any orientation of a pattern;
  other possible values of matchtype are 1 (no rot/ref) or 4 (rotation only)
* Run recognizer1.3.py.  Now your new modified pattern will be recognized successfully.
* Run export-library.py.
  This will make a new populate-sample-library.py that contains your new blinker-or-whatever definition.

Explanation
-----------

The converter is looking in the library for subpatterns to match, and each time the upper-left live cell matches something,
  and all cells in some orientation of some phase of one of the library patterns are also present in the pattern,
  the script removes every matching cell from the Life universe and continues.

As soon as the script finds an upper-left live cell that it doesn't recognize
  (i.e., it doesn't match the upper-left cell of any library pattern)
  the script will stop and complain.

If the script succeeds in emptying the universe,
  it will write out a new Python script called PatternBuildScript.py,
  which re-creates the recognized pattern using the known pieces from the library,
  to Golly's current Scripts directory.

Side note: this turns out to be a really efficient compressed format for most large circuit patterns,
better than mc.gz or rle.gz, as long as the pattern isn't something like the Demonoid and mostly made
out of gliders or other tiny pieces. Even the Demonoid might do quite well if the library grouped
the gliders into repetitive chunks (the elbow-op recipes).
