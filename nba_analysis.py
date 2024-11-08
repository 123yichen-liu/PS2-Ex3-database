# Import necessary libraries
import pandas as pd
from pathlib import Path

# Set the path to the data directory
DATA_PATH = Path.cwd() / 'data'

def create_and_populate_tables():
    # Set the data path
    DATA_PATH = Path.cwd() / 'data'

    # Connect to SQLite database (creates the database file if it doesn't exist)
    con = sql.connect(DATA_PATH / 'nba_database.sqlite')

    # Load CSV files into DataFrames
    game = pd.read_csv(DATA_PATH / 'game.csv')
    player_stats = pd.read_csv(DATA_PATH / 'player_stats.csv')
    team = pd.read_csv(DATA_PATH / 'team.csv')
    line_score = pd.read_csv(DATA_PATH / 'line_score.csv')
    game_summary = pd.read_csv(DATA_PATH / 'game_summary.csv')

    # Write each DataFrame to the SQLite database as a separate table
    game.to_sql('game', con, if_exists='replace', index=False)
    player_stats.to_sql('player_stats', con, if_exists='replace', index=False)
    team.to_sql('team', con, if_exists='replace', index=False)
    line_score.to_sql('line_score', con, if_exists='replace', index=False)
    game_summary.to_sql('game_summary', con, if_exists='replace', index=False)

    print("Tables created and data imported into the SQLite database.")
    con.close()

# Display the first few rows of each table to understand the data structure
print("Game Table:")
print(game.head())

print("\nPlayer Table:")
print(player.head())

print("\nTeam Table:")
print(team.head())

print("\nLine Score Table:")
print(line_score.head())

print("\nGame Summary Table:")
print(game_summary.head())

# Check the columns and data types of each table to understand their structure
print("\nGame Table Columns:", game.columns)
print("Player Table Columns:", player.columns)
print("Team Table Columns:", team.columns)
print("Line Score Table Columns:", line_score.columns)
print("Game Summary Table Columns:", game_summary.columns)

# Analysis 1: Find the highest scoring player in a single game
# Assuming 'line_score' table has columns 'player_id' and 'points'
top_scorer = line_score[['player_id', 'points']].sort_values(by='points', ascending=False).head(1)
print("\nTop Scorer in a Single Game:")
print(top_scorer)

# Analysis 2: Find the team with the most wins
# Assuming 'game_summary' table has columns 'team_id' and 'win' (where 1 indicates a win)
team_wins = game_summary[game_summary['win'] == 1].groupby('team_id').size().sort_values(ascending=False)
print("\nTeams with the Most Wins:")
print(team_wins.head())

# Analysis 3: Calculate the average points scored per game by each team
# Assuming 'line_score' table has columns 'team_id' and 'points'
average_team_score = line_score.groupby('team_id')['points'].mean().sort_values(ascending=False)
print("\nAverage Points per Team:")
print(average_team_score)

# Analysis 4: Find the most common game location
# Assuming 'game' table has an 'arena' column
arena_counts = game['arena'].value_counts()
print("\nMost Common Arenas:")
print(arena_counts.head())


import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Function for connecting to the SQLite database
def connect_to_db(db_path):
    return sqlite3.connect(db_path)

# Data wrangling function to execute a query and return a DataFrame
def fetch_data(con, query):
    return pd.read_sql(query, con)

# Function to visualize data
def plot_bar_chart(df, x_col, y_col, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.bar(df[x_col], df[y_col], color='skyblue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.show()

# Example query functions for specific insights
def get_top_scorer(con):
    query = """
        SELECT player_name, MAX(points) AS max_points
        FROM player_stats
        GROUP BY player_name
        ORDER BY max_points DESC
        LIMIT 1
    """
    return fetch_data(con, query)

def get_top_team_wins(con):
    query = """
        SELECT team_name, COUNT(*) AS win_count
        FROM game
        WHERE win='1'
        GROUP BY team_name
        ORDER BY win_count DESC
        LIMIT 1
    """
    return fetch_data(con, query)

def get_avg_team_scores(con):
    query = """
        SELECT team_name, AVG(points) AS avg_points
        FROM game_stats
        GROUP BY team_name
        ORDER BY avg_points DESC
    """
    return fetch_data(con, query)

def get_common_arenas(con):
    query = """
        SELECT arena, COUNT(*) AS game_count
        FROM game
        GROUP BY arena
        ORDER BY game_count DESC
        LIMIT 1
    """
    return fetch_data(con, query)
