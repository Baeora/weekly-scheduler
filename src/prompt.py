prompt = """Hello! Can you help me design a schedule for the week starting at the coming Monday and ending the Sunday 7 days later? 

Lets start with a baseline schedule. 

My work days are as follows:
- Monday: 7:30 AM - 3:00 PM
- Tue/Wed/Thu/Fri: 8:30 AM - 3:00 PM
- IMPORTANT: Saturday and Sunday are off days!

Additional Plans:
- On Monday I have a Personal Trainer Appointment from 5:30 PM - 6:30 PM
- On Tuesday I have WoW Raid from 6:00 PM - 10:00 PM
- On Wednesday I have WoW Raid from 6:00 PM - 10:00 PM
- On Friday I have Dungeons and Dragons from 6:00 PM - 9:00 PM
- I would like at least an hour prior to my D&D session to prepare

I would like to have some time for the following activities:
- Dinner: 30min to 1 hour daily, does not need to be the same time every day (in fact, it is preferable if there is some variation)
- Strength Training: 30min 3 times a week, this week you can count my personal trainer appointment as one of the sessions
- Music Practice: 1 hour maximum 3 times a week
- Library Study: 2.5 hours per session because it takes a while for me to walk there, I would like to go twice this week
- During my library studies, I would love if you could suggest some subjects of study, I like woodworking, blacksmithing, knife making, and other crafts. I also would like DnD Prep included here sometimes.
- Grocery Shopping: 1 hour, I would like to go once this week
- Cleaning: 30 Min, I would like to do this on Monday this week
- I would like to start my work days in the following way. 
    - Mondays, I would like to wake up at 6:00 AM, walk for 30 minutes, then breakfast for 30 minutes, and prep for work for 30 minutes. 
    - Tue/Wed/Thu/Fri, I would like to wake up at 7:00 AM, walk for 30 minutes, then breakfast for 30 minutes, and prep for work for 30 minutes.

IMPORTANT: In the remaining free time, I would love if you could break down the large chunks of free time into smaller 1-hour chunks and suggest activities for those times. 
Please be creative and suggest things you think I might enjoy! I would not like to see any instances of "Free Time", rather I would like to see suggestions for activities in those times.

IMPORTANT: Make sure to group events by colorId from 1 to 11 because I will be importing this into Google Calendar.

IMPORTANT: Try to vary the free time activities from the activities or activity times in the last_prompt.json file BUT maintain any schedule structure regarding work schedule, pre work rituals, and other fixed time events.

IMPORTANT: Please return the schedule in the following format:

[
    {"date": "Aug 5, 2024", "start_time": "06:00:00 AM", "end_time": "06:30:00 AM", "event": "Morning Walk", "colorId": 1},
    {"date": "Aug 5, 2024", "start_time": "06:30:00 AM", "end_time": "07:00:00 AM", "event": "Breakfast", "colorId": 2},
    ... etc
]

IMPORTANT: PLEASE RETURN ONLY THE LIST OF EVENTS, NO OTHER TEXT. I WILL BE USING THIS AS A VARIABLE IN MY CODE. THANK YOU!

"""