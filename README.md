# Datamodellering Prosjekt 2026

Group 151. 

This project contains database modeling tasks and scripts for the 2026 course project.

## Getting started
Run `Code/Python/app.py`, this will create database object with appropriate schema.  
To insert data use command `insert_dummy_data`

## Example use case
TODO

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

