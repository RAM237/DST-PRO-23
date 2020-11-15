# Skillfactory: DST-PRO

## Unit 0. Introduction to Data Science
## Project 0. GitHub. "Guess the Number" game.

### Task
Given the number "imagined" by computer,  
implement the algorithm that finds out this number  
with as less iterations as possible,  
being able to ask only one question at a time  
(whether number is less, equal or greater that "your guess").

### Solution
After examining several possible solutions, binary search was chosen  
as a primary concept of guessing the number, since it gives  
the least number of tries in average - 5.

For more info on a few other tested algorithms see further section.

Basically, the main logic is implemented in `game_core_v4` function.  
Then it is used as an argument in `score_game`, just to collect stats.

### Other tested algorithms
1. Pick up random number, then apply binary search.  
-- gives 6 attempts in average.
2. Binary search with random on each iteration.  
-- gives 8 attempts in average.
