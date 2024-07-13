# csesoc_feedback_process_bot
Improve collection of feedback from attendees by reminding CSESoc directors to send out feedback forms.

### What this Bot does
- Reads Feedback Master Sheet to see which Events have had their feedback filled out.
    - It does this by looking at the `Completed` column for the `Feedback Form` column.
- Pings relevant directors/roles on a daily basis until the feedback form is filled out (as per the columns).
    - Retrieving the relevant roles might be a bit difficult, as it is not build in.
        - Either do this by using confluence automation to message the bot in a channel that is only for the bot, and then the bot stores it in a dictionary that maps events to roles.
        - OR: Scrape the `pipeline` discord channel. This is way more sus since the titles can be inconsistent in the `pipeline` discord channel.

### Installs on your VM

- The packages will vary, refer to the `main.py` to see what is required.
- I installed with Oracle Cloud, which has a free teir. 
    - I use Bitvise SSH to access the Oracle Cloud system. You will need your private key (from the Oracle Cloud project page) to log into (through ssh) the system.
        - You will only need to upload the necessary files to run to the Oracle Cloud. At the time of writing, I only needed to put up `main.py`, and my `.env`.
    - Oracle Cloud uses python 3.6, you will need to upgrade to python 3.9 to get everything to work (the discord.py library doesn't work with python 3.6).
    - Once you do the install of python 3.9, make sure you install the packages for the python 3.9 verion.

### Running on your VM

- Use `tmux` to make the program keep running while you have the terminal closed.
- `tmux` will make a new `tmux` window thing. When you close the terminal, it will remain running.
    - Inside the `tmux` window, you can run the python script as you normally would. 
        - If you used Oracle Cloud and upgraded to python 3.9, make sure you launch it with the correct version.
- To see the open `tmux` windows, do `tmux ls`. 
- To access a `tmux` window, do `tmux a -t [terminal index]` (eg. `tmux a -t 0`).