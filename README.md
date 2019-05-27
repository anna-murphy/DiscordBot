# DiscordBot

This is a bot designed to count point for entities on a server. It reads messages for specific keywords, and stores data to a file based on those keywords. Overall, the behavior isn't complicated.

## Running the Bot

```$ python bot.py```

This should have the keys set up right now, which *probably* isn't the best idea. But it's fine. Make sure you have the Discord API installed. 

## Features

To see the list of available commands, you can use the `!p h` command. This will display the following message:

```
I hear you're looking for help!
  !p              - tells you everyone's standing.
  !p l            - tells you the top 3 people.
  !p username     - gives the points for a specific user.
  !p username X   - updates the score for that user.
  !p r username   - removes the user from the scoreboard.
```

All of the commands follow this syntax. A note on the point update command: if the user is not being recorded, they are added with this command. 
