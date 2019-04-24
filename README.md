# DotA 2 Prediction Platform
The objective of this project is to develop a Machine Learning model that can be served reliably and scalably on Amazon Web Services. In working on this project, I hope to develop my skills in building Serverless Services and developing a model which is constantly improving.

This project is a work-in-progress. Below, I have described my project as I see it developing over the coming weeks.

## Introduction
This project started as a group project for my Big Data Programming class during my Masters'. The dataset used to initially train the Spark model can be found below. For that project, we only developed the model to run locally for predictions. I wanted to take a similar model and make it available for others to use by hosting it on the cloud.

Data Source: https://www.kaggle.com/devinanzelmo/dota-2-matches/data

DotA 2 is a massively popular online game enjoyed by millions around the world. The basics of the game are as follows: 2 teams of 5 "heroes" face off in a battle to destroy the opposing team's base. Each of these heroes have unique spells and abilities that help them defeat enemies. Each hero has their own strengths, weaknesses, and synergies with other heroes.

By using the heroes chosen at the beginning of any match, we developed a model that could predict who would win that match.

## Backend
As of now, the predictions are made available to the world as a Flask application hosted by an Amazon Lambda function. By sending a GET request to API Gateway, the Lambda function will trigger, run the model on the request, and send a response containing the win prediction.

The model itself is hosted on an Amazon S3 bucket as a JSON file, containing the parameters for the model to run.

Eventually, I will write a service that will query the official DotA 2 API for fresh, new games to include in the training data. All the historical games and these new games will be stored in a DynamoDB table.

A Scala script will trigger once a week to rebuild the Spark model with the data from the database.

## Frontend
The frontend is a work-in-progress.

The frontend is being built with the React web framework. The goal is to have a list of all the heroes available to choose in DotA 2 as buttons, which the user can click to form the two opposing teams for the match.

Once the two teams are validated (cannot have duplicate heroes in a match), the frontend sends a GET request to the Lambda function through API Gateway. The response contains the win prediction.

## The training data
(based off of the csv metadata from the data source)  

### Data from Kaggle

 - `hero_names.csv` 
       * `name`: NPC Hero Name
       * `hero_id`: Hero ID
       * `localized_name`: In-game name
 - `cluster_regions.csv`
       * `cluster`: server ID
       * `region`: world region name
 - `match.csv`
       * `match_id`: Unique match identifier
       * `start_time`: Time match started (seconds from time 0) (post-game stat)
       * `duration`: Duration of match (in seconds) (post-game stat)
       * `tower_status_radiant`: In-game tower status (after match begins)
       * `tower_status_dire`: In-game tower status (after match begins)
       * `barracks_status_dire`: In-game tower status (after match begins)
       * `barracks_status_radiant`:In-game tower status (after match begins)
       * `first_blood_time`: In-game stat (after match begins)
       * `game-mode`: numeric game mode ID
       * `radiant_win`: Target variable (true = radiant team win, false = dire)
       * `negative_votes`: Post-game stat
       * `positive-votes`: Post -game stat
       * `cluster`: cluster server ID (relates to region)
 - `players.csv` (relevant columns used)
       * `match_id`: unique match identifier
       * `account_id`: Player account id
       * `hero_id`: Hero this player played in this match
       * `player_slot`: Determines team played for (0,4): Radiant, (128:132): Dire
       *  (many other in-game and post-game stats not used in the analysis)
      
 - `player_ratings.csv`
       * `account_id`: Player account ID
       * `total_wins`: Total number of wins according to player history
       * `total_matches`: Total matches played
       * `trueskill_mu`: Average trueskill for this player
       * `trueskill_sigma`: Trueskill standard deviation for this player
       * This csv contained many account ids not found in our set and contained many of the accounts ids that were. 
         Anonymous users have the standard imputed value of 25 for `trueskill_mu` and 25/3 for `true_skill_sigma` 

### Created/ Additional Data

 - `hero_grouped.csv`
       * `hero_id`: Hero ID
       * `prediction`: Result of k-means clustering into 7 groups (ranged 0 to 6)
 - `hero_chars.csv` (scraped from dotateam.me) 
       * `name` : NPC Hero Name
       * `hero_id`: Hero ID
       * `localized_name`: In-game hero name
       * `carry`: hero carry ability (Range (0,4))
       * `disables`: hero disable ability (Range (0,4))
       * `initiation`: hero initiation ability (Range (0,4))
       * `nukers`: hero nukers ability (Range (0,4))
       * `pushers`: hero pushers ability (Range (0,4))
       * `support`: hero support ability (Range (0,4))
       * `durable`: hero durability (Range (0,4))
 - `rules.csv` (created from Association rules)
       * `antecedent`: Right side of association rules ("if")
       * `consequent`: Left side of association rules ("then")
       * `confidence`: Level of conifdence associated with the rule


