# Datamodellering Prosjekt 2026

Group 151. 

This project contains database modeling tasks and scripts for the 2026 course project.

## Getting started
Run `Code/Python/app.py`, this will create database object with appropriate schema.  

## Use cases

**#1**  
To insert all dummy data, run command:    
`insert_dummy_data`.  
See `Code/SQL/db-inserter.sql` for list of all inserted data.   
**#2**  
To make Jhonnys booking, run command:    
`book TODO`   
**#3**  
To register Jhonnys attendance, two commands must be run:   
`attend_gym TODO`   
`attend_class TODO`   
TODO this will give jhonny dots no? Must attend_gym contain time? Or should it have default value perhaps.    
**#4**  
To get weekly schedule for week 12, run command:    
`weekly_schedule 2026-12`   
**#5**    
To get Jhonnys visit history for 2026, run command:    
`visit_history TODO`    
**#6**  
To blacklist Jhonny, we must first give him three dots. We can do this by making him arrive late three times:    
TODO    
Then Jhonny becomes blacklisted until the oldest dot is more than 30 days old. During this period Jhonny can make no group lesson bookings.
Therefore following command fails:    
`book_lesson TODO`    
**#7**  
To get the persons(s) that have arrived to the most group lessons for a given month, for example March, run command:   
`most_group_lessons 2026-03`    
**#8**  
A way to find this out is by TODO   

## Structure
- `Code/`: 
  - `Python/`: 
    - `app.py`: Main application entry point and loop.
    - `dbfunctions.py`: Handler functions for database-related commands.
    - `dispatcher.py`: Command dispatcher that parses user input and routes to handlers.
    - `support.py`: Non critical support functions.
  - `SQL/`:
    - `db-creator.sql`: SQL script to create the database schema and tables.
    - `db-inserter.sql`: SQL script to insert dummy/test data into the database.
    - `trigger-creator.sql`: SQL script to create database triggers.

## Implemented logic