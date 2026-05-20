#!/usr/bin/env python3
"""
Generate full narration recordings for Series 2, Videos 2-6
Video 1 test narration already completed
"""

from gtts import gTTS
import os

# All scripts from SERIES_2_SCRIPT_OUTLINES.md
SCRIPTS = {
    "video2": {
        "title": "Saying the Unsayable",
        "script": """
There are things we know we should say. Things that sit in our chest,
pressing against our ribs, taking up space. Waiting to be spoken.

But we don't say them. We swallow them down, fold them away,
convince ourselves they're too big, too dangerous, too much.

We believe that saying it out loud will break something. Our relationship. Our reputation.
The careful balance we've built.

But there's a cost to not speaking. A cost paid in our own silence.

The unsayable doesn't disappear because we don't name it. It becomes heavier.
It grows. It festers in the darkness of our not-speaking.

And then sometimes—in a moment of courage, or exhaustion, or desperation—
we say it anyway. We break the silence. We speak the unsayable.

And something shifts. The thing, once named, becomes manageable.
It becomes real. And real things can be faced.

The unsayable wants to be said. And maybe we're the only ones who can say it.
"""
    },
    "video3": {
        "title": "The Maps We Build",
        "script": """
We're map-makers, all of us. We build models of how the world works.
How people are. How we should be. These maps feel like truth.

Maps given to us: culture, family, education. Maps we build from experience.
People like me are this. Situations like this go that way.

We navigate by these maps. We trust them because we've used them before.
They make sense of the chaos. They keep us safe.

But territories change. The map becomes obsolete. And we keep following old paths.
Wondering why we keep arriving in the same places.

The paths we trusted lead nowhere. The people we expected to be are no longer there.
The situations we thought we understood have shifted beneath our feet.

And we find ourselves lost. Not because the world changed. But because our map did.

Sometimes we have to let go of the map. To navigate by presence instead of prediction.
To allow that the territory has changed. That we have changed.

To move forward without knowing exactly where we're going.
