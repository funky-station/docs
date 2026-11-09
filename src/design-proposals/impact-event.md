
# New Major Game Mode, Station Impact Event

A new major threat faces the station in the form of an asteroid in deep space on a direct collision course! The station must use whatever means it can to avoid certain destruction and protect the costly NanoTrasen assets on board. 

| Designers       | Implemented                                                                             | GitHub Links    |
| --------------- | --------------------------------------------------------------------------------------- | --------------- |
| micmicmic| :information_source: Open PR | TBD |


## I. Summary

The idea of a life ending threat in the form of an asteroid hurtling towards you has historical precedents(Asteroid killing dinosaurs), science fiction representations(1998 Deep Impact), is a concern to people on Earth today, and poses a legitimate risk to space crafts(Admittedly tiny impacts instead of large). With such a large scale of science, media, and topical relevancy around this idea I believe it is deserving of its own, better, representation in Space Station 14.

## II. Problem

Space Station 14 is not without it's current implementation of this idea already, with meteor and debris showers being a common occurrence and the rare Kessler event. However meteor events on the station are a minor nuisance and considered a chore for engineering staff. Being low impact and not very engaging or fun for engineering staff or crew, the highlights of these are usually only seen in the rare events where a space faring crew-member gets sniped by an errant meteor and exploded. Very cool, but very very rare and sometimes frustrating/hilarious.

The scope of this is not to change anything with existing meteor showers/kessler events but instead to outline the framework and fleshing out the idea of space meteors into a game mode all its own, labeled here Impact Event going forward. 

In addition to solving the problem of current meteors being lackluster, this game mode will also solve a secondary concern regarding the Engineering and Salvage departments. 

Currently Engineering has very few instances of being directly involved or engaged with the main game modes outside of the scope of fixing things that are broken as a result of whatever events going on. The only time Engineering is engaged fully for the course of events on the station is usually during instances where they create situation themselves(During Teslalooses/Singuloose/SM Delaminations) or when an antagonist purposefully sets out to sabotage station faculties. 

Salvage, also, is in a weird position in general with their engagement with the station or main game modes. There are some who frown when salvage engages antagonists directly outside of their Salvage Magnet/Expedition lane. There are also instances where Salvage's normal operations keep them secluded from whatever business is going on the station and hidden away in space without engaging other departments or events. 

Whereas many game modes place our noble and glorious Security Department as the bulwark to deal with any station threats or mischief, Impact Event aims to empower the Engineering Department and the Salvage team to collaborate with the rest of the station and work towards evading imminent destruction.


## III. Intent

The intent of this is to highlight the value of a new game mode centered around giant asteroids and collision physics and to serve as a design draft for how this new game mode operates with its expected shift flow, end states, and other considerations. 

## IV. Game Mode Elements

    THE ASTEROID
A giant, space station sized asteroid is hurtling through space on a direct trajectory with the station! There is an estimated 75 minutes(Or a random range between 45-90) before impact. Spawned far enough in deep space that traveling at a fixed speed towards the station will result in it making impact at 60 minutes, give or take. The asteroid should move at a brisk 25 meters speed, enough that a craft could catch up to it if needed but still fast enough to obliterate anything stationary in front of it. Initially the asteroid is on a straight vector toward the station's current position in space. The Asteroid would ideally have a generative layout to prevent the mode from getting stale if people play it too often, with a few key features. Similar in design to the Red Roid with a large chunk of it being swathes of rock and attached to it a Syndicate outpost. The rock side of it should be infested with evil space fauna, fostered by the Syndicate's evil zookeepers of course. The outpost side should be manned by a few NPC syndicate guards....But I'm not sure if making these ghost roles would be more fun. At the heart of the Outpost should a large, evil machine called the Redspace Engine. As long as the Redspace Engine is operational, the Asteroid should maintain a fixed speed of 25 meters (Plus 10 meters for each active Asteroid Beacon on station). Once the Redspace engine is destroyed, the Asteroid should SLOWLY decay its speed over 5-10 minutes before finally coming to rest. Anything hit after this point will slow the Asteroid further with collision physics, whether that be debris, shuttles, or the station it was aimed at to begin with. 

    The Gorlex Infiltrators
There's more to play than simply the asteroid. Gorlex has sent 3-5 infiltrators onto the station who will activate after Central Command issues a station alert about an impending collision. The role of these infiltrators are to sabotage efforts of the crew and ensure that the asteroid removes the space station one way or another. The amount of TC supplied to these agents can act as one balance consideration, I recommend 40-50 to start. They should be guided as saboteurs and not soldiers/assailants. Still given some lethal options as it IS still the Gorlex, my hope is that they'll take an undercover spy or backstab instead of just buying an SMG. The Gorlex Infiltrators will also have available to them a unique item for this game mode: Asteroid Beacons.

    The Asteroid Beacons
Similar to a singularity beacon, this device is a large machine frame that needs to be anchored on the station and connected to an HV wire to receive power. When powered, the Asteroid Beacon will consume a large amount of energy and adjust the trajectory of the Asteroid to re-target the station's location. Each active Beacon will increase the speed of the Asteroid leading to an earlier impact if they remain operational. The beacon should not work off station to prevent strapping it to a shuttle if found. If an Asteroid Beacon is active it should trigger an automatic Central Command announcement about some strange anomalies with the Asteroid's trajectory and encourage the station to investigate. This should trigger 2-6 minutes after the first beacon is activated on the station. Only three Asteroid Beacons will be made available among the Gorlex Infiltrators. It will be for the Engineering team to investigate and get rid of these beacons. The Asteroid beacons serve as a challenge if the station attempts. Additionally, the Asteroid Beacons don't just effect the giant asteroid heading to the station....As long as they are active, meteor events will become much more common targeting the Asteroid Beacons directly. 


##  End States

    Crew Victory!
The crew manage through either engineering the station to survive the impact! By finding and destroying asteroid beacons, destroying the redspace engine on the asteroid through battling it off or arming the nuke on the asteroid, or just strapping a giant thruster to the shuttle and moving it someplace else, the day is saved! A mandatory audit of engineering and logistic channels will begin immediately upon arrival to Central Command. 

    Crew Defeat!
The crew fail to come together to surmount the challenge. After 75 minutes the Asteroid makes direct contact with the station and punches through it like a bullet. The Redspace engine on the Asteroid gives it the advantage in the shuttle collision physics, making it even more punchy than usual rock and stone tiles. Whatever shuttles orbit the station can only watch, packed like sardines, as their livelihoods get scattered in space. This should trigger an automatic round end. 

    Mixed/Neutral Ending
The crew manage to soften the blow somewhat but are still otherwise unable to avoid collision. Whether the Redspace engine is destroyed but too late to matter, or the Asteroid beacons on the station found and destroyed but the station's anchor still holding it in place as the aimless rock clips the station's broadside, or if the Captain's strategy of bankrupting Cargo by buying a dozen shuttles and slamming them into the rock manages to somehow kinda work.....Most of the crew are at least alive and the station is somewhat habitable. Not sure if this should be a round ending event. All of the station's command, engineering, and regular crew are detained for asset liability processing by Central Command. 


## V. Considerations

    Technical Consideration
This will require some understanding and leveraging of the station's collision physics implementation between grids. It may be necessary to be able to modify how structurally sound the Asteroid grid is to make it more or less destructive for balance concerns. There is also a lot of uncharted territory here with pushing collision physics into a core element of a game mode and performance on server architecture may also need to be tested and addressed. From what I've seen in other environments, it shouldn't be TOO terrible on performance having seen two trains rammed into Core station as a stress test with only a minor hiccup. But it should still be vetted first on the server's hardware before progressing with other elements of this game mode. 

Additionally, mapping or generation of the Asteroid itself will be a crucial element to the mode. The degree of the mode's effectiveness will be tied to the composition and layout of the asteroid.

    Player Consideration
The scenario presented to the station is in one sense very simple. A giant rock is coming to crush you and your station, good luck. The hope with this game mode is that enough 'apparent' options are made available to give the station a number of valid ways to respond. However it is also most likely possible that the crew may find given options too difficult or conversely may find some ways of trivially succeeding the game mode removing some of the challenge and fun. There are thus a few different mechanisms to be considered for balancing this game mode to make it more/less difficult. Those balance options are as follows: 

    * Asteroid Base Speed: Effecting the collision base destructibility and how easy or hard it is to access via shuttle(Can you safely land on it with moderate skill?)
    *Number of Gorlex Infiltrators: An easy number to adjust how many wrenches the station may need to deal with to succeed. 
    *Amount of TC for Infiltrators: same as above. 
    *Number of Asteroid Beacons : More beacons mean they're harder to route out. Fewer beacons means the infiltrators may have to bunker down and set up a defensive perimeter and traps. 
    *Speed boost per active Asteroid Beacon: This would determine how much of a role the Asteroid Beacons play on the overall speed of the round. 
    *Asteroid Size: How large is this rock? Ideally this would be a size to match the station it hits no larger/smaller but whether this actually matters in the end may be negligible depending on the technical performances. 
    *Asteroid Fauna/Syndicate Guard Density: How many beasties and bad guys does the salvage team have to fight through to get to the engine? If the teams NT sends to the asteroid keep falling to the monsters each round before reaching the engine that would be a signal to lessen them. 
    *Meteor Event Density: How often should meteors hit the station while beacons are active can determine how much it effects regular events on the station itself. 

Additional Player considerations are on the design of the game mode itself being a 'two sided' event. You will have those who are taking part on the Asteroid party(Salvage, mediics/engineers/security/clowns) alongside the station leftover. Command will have to step up its communication capabilities in order to keep up with the events on the station and the Asteroid to manage resources. Engineers will have to play an active role outside engineering checking power consoles and running down HV wires and dismantling barricades, probably with some security and medical staff to support them after the first one runs into a boobietrap. For Service/Science folks they could either be drafted into the departments that need them, be formed together to make Team B if Team A forgets to factor in intertia when approaching the Asteroid, or just do their own workcycles among the chaos. 


    Admin Consideration

Because of the two-sided nature of the game mode it may be more difficult for a single administrator to watch things on both sides simultaneously. Alert codes and colors as well as procedures may need to be readdressed to give the game mode more impact. If the shift was just forever Yellow when the asteroid came it may hold less weight. Also player conduct may need to be looked at if rounds devolve into anarchy too soon before the station has its chance to mount a reasonable defense. Expectations for the Chief Engineer and Quartermaster will also need to be looked at during these rounds as those are the two primary departments that will be engaged. 

