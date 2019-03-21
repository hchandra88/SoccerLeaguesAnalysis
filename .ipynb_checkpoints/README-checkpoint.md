# Soccer Leagues Analysis

### About
This project serves as an exploration of web scraping, data analysis, and visualization using Python. Team performance data from several of the most competetive European soccer leagues will be used to investigate and study the world's best clubs.

### Project Introduction

Sit down with a non-soccer fan and ask them what their least favorite thing about soccer is. More likely than not, they'll say, "You could sit in front of your television for 90 minutes and watch a game which ends 0-0. What's the fun in that? Who's the winner?" So that begs the question...

Q: How do you win a game of soccer? What's important? What will change the game?

A: Goals. Goals. Goals.

To show this, let's try to devise a strategy from a coach's standpoint...
1. Instruct all your players to spend the game defending and attempting to prevent the opponent from scoring?
2. Prevent your opponent from coming close to your goal by commiting fouls? But you can only commit so many fouls before the referee steps in to issues punishment, which limits our scope for future fouls. 
3. Minimize the amount of time for which the ball is "in play" by constantly putting it out-of-bounds?
4. Spend all our energy attacking and try to out-score our opponent?

In an ideal world, strategies 1, 2, and 3 prevent our opponent from scoring. However at best, we still end up with our dreaded 0-0 so we should pick strategy 4 -- go for goals.

### Project Summary
In this project I will take a look at teams from the top 5 leagues in Europe (England, Spain, Germany, Italy, and France) and how they "go for the goals". This comparison will give us an idea of how these teams perform domestically and what makes them so good. Next, we will look at how these same teams perform in the UEFA Champions League (UCL). For those unfamiliar with soccer, the UCL is an annual tournament in which the top teams from several leagues across Europe vie for the title of "Best Team in Europe". In the past decade the tournament has been primarily dominated by Spanish and German teams which has prompted soccer fans to ask what prevents teams from other leagues from winning on the European stage despite boasting great numbers domestically. The English Premier League (EPL) is considered by many soccer fans to be the most competetive and best league around the world so it is surprising to see English teams fail on a regular basis in comparison to their Spanish and German counterparts. As such, the last part of this project will be an analysis of the play-style of Premier League teams to idetnify what prevents them from succeeding in the UEFA Champions League.

### File Structure

The following files contain goalscoring analytics for each of the top 5 leagues in Europe...
1. EPL.ipynb (England)
2. LaLiga.ipynb (Spain)
3. Bundesliga.ipynb (Germany)
4. SerieA.ipynb (Italy)
5. Ligue1.ipynb (France)

UCL.ipynb contains similar goalscoring statistics for the top teams in the UEFA Champions League. Meanwhile, webscraping.py contains several methods to automate the data collection process of this project where data was taken from Fox Sports. Finally, the CSV files in this repository contain said data taken from Fox Sports.

Created by: Harish Chandrasekaran