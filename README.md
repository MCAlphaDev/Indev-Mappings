# Indev Mappings

The tools for creating the Indev MDK (Target Version: 2010-01-28). Not the MDK itself!

# Setup

These tools have been designed for windows so if you're on mac or linux you'll need to adapt some of the steps.

Run the following programs in order:

- download.py (This downloads minecraft 2010-01-28)
- remap_to_intermediary.bat (This uses the project's intermediaries which were generated with stitch & repackage.py. And with a couple lines manually edited to fix a couple mistakes in the output from a mistake in the regex I'd used, but we don't talk about that)

The next step depends on what you want to do.

If you want to edit mappings:

- run start_enigma.bat. This starts enigma up with the mappings and intermediary jar.
- also I recommend reading enigma_notes.txt. This contains some notes I jotted down while creating the mappings

If you want to decompile minecraft:

- lol I haven't done this yet. There will be a script similar to remap_to_intermediary which generates a named jar, and then uses forgeflower to decompile. Then we'll just have to apply some patches to fix decomp errors. Might use unpick or something for the OpenGL constants
