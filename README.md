# NPCS
Webpage database editor using **Python** and **PostgresSQL**.

To communicate **Python** and **PostgresSQL** I used **Psycopg2** Library and for the communication between **Python** and the **Website** I used the **Flask** Library.

## Project Idea

An ambitious video game developer has an idea to make their next video game more immersive and diverse, make the NPCs (Non-Player Character, video game characters not controlled by any person) unique. In this way the player will not find any NPC similar to another and the player will have an experience in a more realistic world.

To face this challenge they decided to create a database. In the database will be stored all the NPCs of the entire video game. Each NPC has a gender, a skin color, a name, a height, a certain face model and life which is a number between 0 and 100. If an NPC has life 0, it means that he is dead and has to be removed from the table. A face is defined by the file names of the 3D eyes model, nose, ears and mouth and is identified by an identifying number. Hair also has a 3D model and an identifying hair color.

An NPC lives in a certain world region and it is not possible for two NPCs with the same face to live in the same region, each region is limited by a set of coordinates, has a certain climate and a unique name. An NPC can be familiar with 0 to 5 NPCs.
A coordinate is a specific value given and identified by three variables, x, y, z.
There are two types of NPCs, enemies and villagers. Every NPC must belong to one type necessarily and only to one.

An enemy can attack any player, and any player can attack any NPC, and therefore any enemy. You want to have a record of which players have attacked each enemy, and which NPCs each player has attacked, and how much damage they have done to both. Both enemies and players consist of attack damage (amount of damage done in an attack) and movement speed (number of coordinates an element moves in x seconds). Both parameters are numbers between 1 and 100.
Villagers have a dialogue consisting of one sentence. Both inhabitants and players have an inventory with their objects and the quantity of each one.

Objects are identified with a name, it is not necessary to identify a specific object but the idea. They have a value measured in some monetary unit. Therefore players can exchange one object for another object with any villager. You want to have a history of all exchanges made containing the two objects exchanged, which NPC and player made it and when (date, hour, minute and second) it was made.
A player has a unique name, life as do the NPCs and inventory as stated above.


## Glossary
- Face: 3D model that is part of an NPC made up of 3D models of a nose, eyes, mouth and ears.
- NPC: video game element that is not controlled by any person.
- Region: surface of the video game delimited by coordinates.Boundary: coordinate that belongs to the boundary of 2 or more regions.
- Hair: colored 3D model that is part of a face.
- Enemy: type of NPC that attacks.
- Villager: type of NPC that exchanges with the player.
- Object: exchangeable video game element with monetary value.
- Player: video game element controlled by a person.


## **UML** Diagram of the project
Implemented part in red
![Copy of proj drawio (2)](https://github.com/Blondie-TheManWithNoName/NPCS/assets/58909117/3251e2c2-5db7-4d93-afe1-bee708ad5252)
