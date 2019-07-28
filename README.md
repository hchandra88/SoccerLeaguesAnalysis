# Soccer Leagues Analysis

### About
This project serves as an exploration of web scraping, data analysis, and visualization using Python. Team performance data from several of the most competetive European soccer leagues will be used to investigate and study the world's best clubs.

### Project Introduction

Sit down with a non-soccer fan and ask them what their least favorite thing about soccer is. More likely than not, they'll say, "You could sit in front of your television for 90 minutes and watch a game which ends 0-0. What's the fun in that? Who's the winner?" So that begs the question...

Q: How do you win a game of soccer? What's important? What will change the game?

A: Goals. Goals. Goals.

To show this, let's try to devise a strategy from a coach's standpoint...
1. Instruct all your players to spend the game defending and attempting to prevent the opponent from scoring?
2. Prevent your opponent from coming close to your goal by committing fouls? But you can only commit so many fouls before the referee steps in to issues punishment, which limits our scope for future fouls. 
3. Minimize the amount of time for which the ball is "in play" by constantly putting it out-of-bounds?
4. Spend all our energy attacking and try to out-score our opponent?

In an ideal world, strategies 1, 2, and 3 prevent our opponent from scoring. However at best, we still end up with our dreaded 0-0 so we should pick strategy 4 -- go for goals.

### Project Summary

#### Part 1

In this part I will take a look at the best teams from each of the top 5 leagues in Europe (England, Spain, Germany, Italy, and France) and how they "go for the goals". This comparison will give us an idea of how these teams perform domestically and what makes them so good. At a basic level, we will see how many chances these teams generate, and how good they are at converting them into goals. For three of the leagues (England, Spain, and Germany) I have done a written analysis of the statistics presented to further explain them. I chose to omit this section from the other two leagues (France and Italy) because they do not have as large a relevance in Part 2. In addition, the purpose of these analyses was simply to translate the graphics into words and draw attention to certain teams and as such I wanted to avoid repetition.

#### Part 2

This section will take a look at historic data from the UEFA Champions League. For those unfamiliar with soccer, the UCL is an annual tournament in which the top teams from several leagues across Europe vie for the title of "Best Team in Europe".  For the better part of the past decade the tournament has been primarily dominated by Spanish and German teams which has prompted soccer fans to ask what prevents teams from other leagues from winning on the European stage despite boasting great numbers domestically. The English Premier League (EPL) is considered by many soccer fans to be the most competitive and best league around the world so it is surprising to see English teams fail on a regular basis in comparison to their Spanish and German counterparts. This year, however, three of the four teams in the semi-final were English, leading to an all-English Final. As such, the last part of this project will be an analysis of the play-style of Premier League teams to identify what has changed in the last year to cause such a drastic change in English fortunes in the UEFA Champions League.

### File Structure

#### Part 1
Within the Part1 folder, the data used in the analysis is stored in the TopGoals folder. In addition, the following files contain goalscoring analytics for each of the top 5 leagues in Europe...
1. EPL.ipynb (England)
2. LaLiga.ipynb (Spain)
3. Bundesliga.ipynb (Germany)
4. SerieA.ipynb (Italy)
5. Ligue1.ipynb (France)

#### Part 2
UCL.ipynb contains similar historic data about the UEFA Champions League. PlayStyle.ipynb contains a comparison of play styles of the English teams that have seen recent success in the Champions League.

Created by: Harish Chandrasekaran