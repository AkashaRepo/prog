Okay so my idea involves the spacrcraft being made up out of components which each have their own states and allow it to make various actions. 
Each component is controled by comands typed by the player, allowing them to interact with the rest of the world.

List of components,
  -Passive sensors (used to scan the planet for life signs and listen in on things)
  -Microwave laser (used to comunicate with people on the planet, or as a weapon)
  -Computer core (Used to process data collected by the sensors, also to save the game)
  -Torch drive (The main engine, used to fly between planets)
  -FTL drive (Used to leave the solar system and end the game, future aditions might add more solar systems, but for now lets keep it simple.)
  
For example the player could get a list of components and their current states by typing Status, and then use them by typing "Engage (ComponentName)" From their the player would be prompted for more specific options. Arguments could be added to the end of the comand for more advanced users "Engage (ComponentName) (InThisManner) (OnThisTarget)", but the minimum would be simply "Engage (ComponentName)" which would be followed by a prompt showing the possible options.

Movement,
Movement in space is abstracted as a series of nodes which the player can move between. Starting in a generic "Deep space" Node, they can transfer to orbit around any of the planets in the solar system, and then from there transfer to a polar, lunar or equatorial orbit.

List of locations in solar system.
  -Hyperspace (quit)
    -Deep space
      -Low Solar orbit
      -High above first planet
        -polar orbit around first planet
        -in low orbit around planet
      -High above second planet
          -in orbit around second planet's moon
        -polar orbit around second planet
        -in low orbit around second planet.
      -High above third planet
          -in orbit around third planet's first moon
          -in orbit around third planet's second moon
        -polar orbit around third planet
        -in low orbit around third planet
and so on and so forth.

The locations on this map are nested to show possible paths between them. From any given node the player can move to the parent node or one of the child nodes, but not to nodes on the same level of indentation, similar to moving through files on a computer. Most of the game will take place orbitng the second planet, with the others there for scenery. More things might be added to them latter.

A goal for a basic prototype would be to implement a system where the player can move between these locations and read discriptive text. From there we can work on other possible interactions and adding more detail.
