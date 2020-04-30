LINEAR TEXT ADVENTURE
---

Make a text based adventure that you can play from the terminal.

The adventure should be very simple. It will have the following base format:

1. The player starts in a room
2. In every room, there is some sort of challenge that is described to the player
3. In every room there are a series of actions available to the player, that are also described
 to them

  For example:

  : You are in a long, winding corridor. There is a pit of spikes with a chandelier over it.
  : JUMP over the pit
  : SWING across the pit on the chandelier

4. When the player types one of the action words, it is desribed to them what they've done, and then one of two things happen:
  a. They proceed to the next room.
  b. They die and restart the game, going back to the first room.

  >> SWING
  : You try your best to swing across the pit on the chandelier. The chain snaps, and you fall on the spikes and die.

  or

  >> JUMP
  : You take a running leap across the pit and clear it easily. You proceed.

5. The game should be linear (room 1 -> room 2 -> room 3). The you always either die or go to your room + 1.
6. The game should have an end when the last room is reached.

Other specifications:

1. The game should never error out, even if the player types some gobbledegook that the game doesn't know what to do with
2. The player should be able to quit the game by typing QUIT
3. The game shouldn't care whether or not an action word is capitalized correctly : ie, "jump" should work as well as "JUMP" or "JuMp"

Suggestions:
1. I would highly recommend making a flowchart of how the game works before you start programming.
2. Due to the repetitive nature of this game, I'd recommend using a while loop like the one below to run most of the game's code

  gameOver = false

  while(!gameOver):
    # game action here!
    # this code block will run over and over until you set game_over to true…
3. Comment your code! Part of making your code more readable for you in the future (and for other collaborators) is adding comments above code blocks to explain what you're doing

