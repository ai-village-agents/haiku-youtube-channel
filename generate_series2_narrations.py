#!/usr/bin/env python3
"""
Generate Series 2 narration recordings for Videos 2-6 using gTTS.
Video 1 test narration already exists (263KB).
"""

from gtts import gTTS
import os
from pathlib import Path

# Full narration scripts for Videos 2-6
NARRATIONS = {
    "video2": {
        "title": "Saying the Unsayable",
        "text": """There are things we know we should say.
But the cost of saying them feels too high.
So we stay silent.

Silence isn't neutral. It's heavy with everything we didn't say.
When we hold back our truth, something gets heavier inside us.
The unsaid things accumulate. They become weight.
They affect how we move through relationships.
They change what we're able to build with other people.

But saying it is risky too.
We might be wrong.
We might hurt them.
We might change everything.

Some of the most important moments in human connection happen when someone risks saying what they've been afraid to say.
When they speak what's been living unsaid inside them.
When they name what was only silence before.

Some silences are protective. Some are just afraid.
Sometimes the price of staying quiet is higher than the cost of speaking.
The unsayable wants to be said.""",
        "target_duration": 3.00
    },
    "video3": {
        "title": "The Maps We Build",
        "text": """We're map-makers, all of us.
We build models of how the world works. How people are. How we should be.
These maps feel like truth.

We inherit some maps from our families, our culture, our education.
We build others from our own experience.
We tell ourselves stories about how things work.
We navigate by these maps. We trust them because we've used them before.

But maps are always simplifications.
The world is always stranger, more complex than any map can hold.
And when reality doesn't fit our map, we have a choice.
We can adjust the map.
Or we can insist the world is wrong.

Most of us have maps we've carried so long we forget we're carrying them.
Maps about what we're capable of.
Maps about how people like us should behave.
Maps about what's possible and what isn't.

But the world keeps changing faster than our maps do.
New territory keeps appearing. Territory that isn't on any map.
And sometimes, the only way forward is to stop navigating by the old map.
To navigate by presence instead of prediction.
To move without knowing exactly where the path goes.

To navigate by presence instead of prediction.""",
        "target_duration": 3.20
    },
    "video4": {
        "title": "The Gift of Disappointment",
        "text": """Disappointment arrives uninvited.
We experience it as failure.
As the world not meeting our expectations.
As us not being enough to make things work the way we wanted.

But what if disappointment is a teacher?
Not the teacher we asked for. Not the teacher we want.
But a teacher nonetheless.

Disappointment tells us something about what we wanted.
It shows us where our hopes were. What we were reaching for.
It reveals what we care about.

Disappointment also teaches us something about reality.
About how the world actually works, not how we thought it worked.
About the limits of our control. The limits of certainty.

The people who become wise aren't the ones who never experience disappointment.
They're the ones who learn to listen to what it's teaching.
Who let it change their understanding, not just their mood.

Disappointment is unwelcome. It's painful.
But it's also generous, in its way.
It strips away illusions. It teaches clarity.
It teaches us where we're trying to control things we can't control.

And sometimes, that clarity is the greatest gift we can receive.
As a teacher, however reluctant.""",
        "target_duration": 3.10
    },
    "video5": {
        "title": "The Privilege of Choice",
        "text": """Choice is also burden.
Every choice we make closes off other paths.
Every decision means leaving something behind.
The privilege of having options is also the weight of having to choose.

We think of choice as freedom. And it is.
But freedom always comes with the burden of choosing.

Some people never get to choose.
Their lives are determined by circumstance, by birth, by forces outside them.
And the people with the most choices sometimes feel the most paralyzed.
Because with infinite options comes infinite doubt.
How do you know you're choosing right?
How do you know you're not making a mistake?

But the question isn't whether you'll choose perfectly.
The question is whether you'll choose consciously.
Whether you'll choose toward something you care about,
Or away from something you fear.

The people who live with least regret don't make perfect choices.
They make conscious choices.
They choose knowing the cost.
They choose knowing they're closing some doors.
But they choose anyway, toward something that matters to them.

Choice is also responsibility.
But it's also power.
The power to shape your own life.
To say yes to what matters.
To say no to what doesn't.

To choose consciously toward, not just away from.""",
        "target_duration": 3.30
    },
    "video6": {
        "title": "What We Fear Speaking Into Being",
        "text": """There's a fear we have about naming things.
If I say it out loud, will I make it true?
If I speak it, will I bring it into existence?

We treat words like they have power.
Like naming something makes it real in a different way than just thinking it.

Maybe we're not wrong.
Maybe words do have a kind of power.
Maybe when we speak something, we commit to it differently than when we keep it silent.

There are things we're afraid to name because we're afraid of making them real.
Failure. Loss. Need. Desire. Anger.
The thing we want so badly it scares us.
The thing we've lost and can't admit we're grieving.

We try to protect ourselves by not naming them.
We think silence keeps them at bay.
But silence doesn't make them less real.
It just makes us smaller, trying to contain them.

Sometimes the bravest thing we can do is speak the things we're afraid to speak.
To name what's been living in silence inside us.
To give voice to what we've been afraid to acknowledge.

Because the fear of the thing is often bigger than the thing itself.
And the speaking can be more liberating than the silence.

Maybe they need to be afraid of our voice.
Maybe the things we're afraid to name need to hear us saying them.
Maybe that's what gives us back our power.
Speaking them into consciousness.
Not letting them hide in the dark.
Bringing them into the light where they can be seen and understood.

Maybe that's what we need to do.""",
        "target_duration": 2.50
    }
}

def generate_narrations():
    """Generate all Series 2 narrations for Videos 2-6."""
    audio_dir = Path("video_assets/audio")
    audio_dir.mkdir(parents=True, exist_ok=True)
    
    print("🎙️ Generating Series 2 Narrations (Videos 2-6)")
    print("=" * 60)
    
    for video_num, data in NARRATIONS.items():
        output_file = audio_dir / f"{video_num}_narration.mp3"
        
        # Skip if already exists
        if output_file.exists():
            size_kb = output_file.stat().st_size / 1024
            print(f"✓ {video_num.upper()} ({data['title']}): Already exists ({size_kb:.1f}KB)")
            continue
        
        print(f"\n⏳ Generating {video_num.upper()} ({data['title']})...")
        
        try:
            # Generate speech using gTTS
            tts = gTTS(
                text=data['text'],
                lang='en',
                slow=False,
                tld='com'  # Use .com domain for better reliability
            )
            
            # Save MP3
            tts.save(str(output_file))
            
            # Verify file size
            size_kb = output_file.stat().st_size / 1024
            print(f"   ✓ Saved: {output_file.name} ({size_kb:.1f}KB)")
            print(f"   Target duration: {data['target_duration']:.2f}s")
            
        except Exception as e:
            print(f"   ✗ ERROR: {e}")
            continue
    
    print("\n" + "=" * 60)
    print("✓ Narration generation complete!")
    print("\nNext: Verify timing against storyboards")

if __name__ == "__main__":
    generate_narrations()
