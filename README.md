# Gym Tracker
tracks your weight, reps, sets and the total volume you did at the gym
asks for the lift that you did, how much weight, how many reps, and how many sets
you type python3 log.py and you answer the questions it gives you
when your done answering questions it shows you your saved gym stats
.gitignore is a list telling git dont upload savedlifts.txt.
gym tracker shows the date when it runs, and saves the date each time you complete the questions
every lift you complete gets saved to savedlifts.txt
you can log mutiple lifts instead of doing it one at a time if needed, and when logging, you type done when theres no other lifts to type
if you add a letter number to a questions that needs a number, it tells that you made a mistake and instead of crashing you type it again without restarting
lift counter shows how many total lifts you did in that session
total volume shows how much weight you lifted throughout your entire lift
what save_lift function does is it saves each lift right after your done typing it, it saves everything to the file.
what the box logs does is it shows how many lifts you did in one session
and what calc_volume does weight times reps times sets for a single lift. then repeats until your done