# Dash-Master
DASH MASTER:-

A Multi-agent game using the Pygame library where four players navigate a grid, attempting to accumulate the highest score by "dashing" into other players. The game employs reinforcement learning (Q-learning) to train the players over multiple episodes, refining their strategies based on rewards and penalties. The grid, players, and scores are visually displayed in a Pygame window. The project explores basic game development concepts, RL principles, and graphical representation using the Pygame library. The script concludes by displaying the winners and their scores, along with a plot depicting the winner's score over different episodes.



CONTENTS:-

1.) AI.ipynb file           - consists of whole code, its training output that is running of 1000 episodes and finally the RL plot between Episodes and Highest score of each episode.
2.) Environment.py file     - consists of only the designing of the code and its environments.
3.) main_final_code.py file - consists of the whole code including the environment and its training using Q-learning.
4.) Images of players(player1.png, player2.png, player3.png, player4.png)



EXECUTION OF THE FILES:-

1.) Execution of Environment.py file     - open the Environment.py file in VSCode and open a new terminal and navigate to the directory where the file exists and run this command: 
"python Environment.py", the output shown is the running of the dash master(pygame) for 40seconds in which after termination of the time it displays the winner with highest score.
2.) Execution of main_final_code.py file - open the main_final_code.py file in VSCode and open a new terminal and navigate to the directory where the file exists and run this command:
"python main_final_code.py", the output shown is the running of 1000 episodes(training the game using Q-learning) each episode duration is 15seconds for each and every episode after the termination of the time it displays the winner with highest score.
3.) Execution of AI.ipynb file           - open the AI.ipynb file in google colab (or) jupyter notebook, and also upload the images of the players in that and run the code, the output shown is similar to the execution of main_final_code.py file and including RL plot between Episodes and Highest score of each episode.    
