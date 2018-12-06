# Programming for Big Data I Final Project: Dota2 Prediction

Data Source: https://www.kaggle.com/devinanzelmo/dota-2-matches/data

## CSV Descriptions   
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


