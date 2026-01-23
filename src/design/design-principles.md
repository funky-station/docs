# Design Principles

Riffing off of what the Space Wizards have done with the game, these design principles go over what we should consider when designing
new features for Funky Station.

Questions about game design should be discussed in Discord and requesting the presence of a maintainer or Tay.

For cool and fun features that you would to add (that aren't exactly a simple pull request), we suggest creating a design document using [this template](template.md).

# Caveats

* Just like WizDen says, these are living documents and will change over time.
* These documents are Funky Station's interpretation of what SS14 should be, and only reflects Funky Station's direction.
* Ideas should be discussed with the mindset of the games roleplay features being held above anything else.

# What is MRP?

MRP, Medium Roleplay, is a version of the game where players are encouraged to take things straight and as they are. 

The statement that a clown has ran into the supermatter should both be tragic and hilarious. A chemist blowing off all their limbs in an accident to make space meth should also be just as tragic and hilarious. Medium Roleplay is a stage where one player controls one character, and the players behind those screens are the audience. In-character actions have consequences, and sometimes the consequences are funnier than whatever gimmick the player might have thought up that round. 

# What is Funky Station?

Funky Station is a fork of Goob Station designed around being explicitly MRP.     

# Core Principles

Creating new features for Funky Station should not violate these core principles.

## Seriously Silly

Funky Station is a play, with each round being a scene. The entire play revolves around a chartered corporation who's only interest is to keep their shareholders rich. Each character in that play, either directly or in-directly, is exposed to danger by other characters.

Increasing the chances of interactions like these playing out is essential when creating new features. Sometimes, something can be hilarious just for the sake of it (see the smoking on a bed may set you on fire PR.) Constantly players are having to poke death every 10 minutes or so, whether knowingly and unknowingly, which is the beauty of Funky Station.

Crazy situations happen, and must be embraced. When designing new features, think of possible outcomes and other systems your feature might interact with. And also consider how such a feature might be interacted with in a roleplay scenario. If the answer is very funny, it's probably a winner.

Maximize these silly situations whenever you possibly can.

## There is no Winning or Losing

Space Station 14 is a game that can be ruined for someone very easily if they approach it with the wrong mindset. If you approach Space Station 14 in the same way you would approach Among Us or other social deduction games, you WILL become bored VERY quickly.
Rather, ask yourself, what would my Felinid-Lizard-Moth abomination be thinking in this exact moment? Would they be thinking about winning? Or rather, thinking about when their next smokebreak is?

When designing a feature, ask yourself that question. Will this encourage players to engage with my feature with this win or lose mindset? Or does it help maintain the story telling and flow of a round?

This is especially true when designing new antagonist objectives. Sometimes, an objective is MEANT to be difficult to do, and is MEANT to be accomplishable by a manner that would be considered violent. Funky is a Space Opera, and a win or lose mentality only serves to compromise the fun. There is great fun to be had in failure, just like there is with success.

## Maintaining Authenticity

Interactions should feel authentic, there is a reason why it is around 7 steps to light a cigarette in this game.

Making a feature feel authentic to real life does not always mean realism. Realism is a different goal that some other forks have in mind, but Realism =/= Authenticity.

Take for example reloading in games, there are more steps to reloading a gun in real life than there is on a game. You can get as granular as you want, even going as far as identifying individual muscle fibers to flex or whatever to achieve a reload. But most games, of course, don't do that. Sure, it'd be realistic, but would it be authentic? No. It would be annoying and tedious.

Just because something happens in real life, doesn't mean it should happen in game, if it takes away that feeling of authenticity.

Again, a cigarette taking 7 steps to light is authentic. The Supermatter being crazy as hell to maintain is also authentic. People getting up instantly after being exploded twice isn't.

## Take Things Slow

Funky Station is built around 2 - 2:30 hour rounds. Many other servers balance their content and gameplay around an hour of gameplay. Thus, when designing new features, consider how much effort a player will have to put into interacting with your system. Things are meant to be complicated and difficult to understand, but first grasping the concepts shouldn't. The expectation players have when joining is that the round will go on for this long, so use this to your advantage.

Atmospherics is an example of this. An atmosians job is to make sure the station has a consistent (roughly) 80/20 mix of nitrogen and oxygen, at around 101KPA. This simple concept is easy for players new to atmospherics to understand, but the additions to atmospherics Funky Station has done has made the barrier to entry rather low, but full of mechanical depth and skill. The same goes with Chemistry, and other departments on Funky Station. See also the section on Maximizing Roleplay Potential, as these two things are very intertwined when considering regular department gameplay.

If you are adding a new gamemode or a weapon, consider TTK and think about how your feature can interact with added or in-progress medical systems. Not everything has to be survivable, but not everything has to be an instakill either. Consider using TTK for weapons or potential RR as deterrents for certain features, as this is one way to communicate to the player OOC that the thing you're working on is dangerous, and should be taken seriously.

Delimbing, targetting specific body parts or organs, or other things related should be considered with antagonists or weapon balance. People don't die in real life because they took 200 brute damage, people die in real life for specific causes, even if unknown. Consider the time investment a player has put into a round when considering antagonist or weapon balance. If death must occur, make sure it is a spectacle in its own right. In this regard, the aesthetics of dying matter.

When designing other features, consider the story you want to tell, and ask yourself if it is a worthwhile story a player wants to engage with for more than 15 minutes. Try justifying why it's worth it for an engineer to take 15 minutes to setup a single power engine, or why a chemist should spend 15 minutes creating a chemical. This is a co-operative game, so when designing things around regular department gameplay, leverage the social aspect of it all, and have people depend and rely on each other where ever it makes sense.

Being respectful of peoples time when they join Funky Station is important when designing a new system.

## Maximizing Roleplay Potential (Avoid QOL slop)

When developing a new feature that is set to "optimize" a certain aspect of gameplay, think about the feature as a vector for roleplay. Does the previous feature introduce more ways for people to interact with each other? Or does this feature take away a vector for people to interact? If it does take away, is it a positive change in the long run?

These questions can be applied like so:

Say for instance you are changing the ChemMaster to have a way to produce bottles en masse, filled with a reagent of a chemists choosing. This, in our eyes, is a positive change that encourages healthier RP, as the previous method for chemists to distribute chemicals en masse to doctors and other crew members, is via jugs, which only serve as an intermediary tool and are rarely thought of. Bottles adds to the immersion that this is an actual item that someone made, and not just a bunch of reagents in a container. In this instance, aesthetics matter.

An instance where a feature would take away a vector for roleplay is the Stationwide Material Silo. Apply the questions like so:

"Does the previous feature introduce more ways for people to interact?" - The previous feature was cargo delivering materials to departments as ordered. While sloppy, it did encourage a lot of small talk and smaller interactions with characters, which is a positive.

"Does this new feature take away a vector for people to interact?" - Yes, cargo players can just deliver materials to a central point in the station, while not communicating with anyone at all.

"If it does take away, is it a positive change in the long run?" - No, hyperoptimizing a crucial part of the gameplay for a cargo tech, talking to random people on the station, is not healthy for the game. Having players be more entrenched in their departments is generally not good for the culture, and stationwide material silos, from the questions we just asked, encourage that very thing.

## Dynamic Environment

Anything should be possible. Just like Wizard's Den, we feel that building an entire, functional station should be possible to do, if there is a considerable effort put into this undertaking.