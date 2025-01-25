
#### Social Network Friend Recommendations
This repository contains a Python program to recommend potential friends in a social network based on the number of common friends between users. The algorithm suggests the most likely new friend for a user, excluding current friends.

#### Features
The program processes social network data files, performs various analyses, and offers the following functionalities:

Friendship Network Creation: Parse and structure friendship data from input files into a 2D list.
Friend Recommendation: Suggest the best friend for a user based on shared friendships.
Common Friends: Identify common friends between two users.
Statistical Insights: Calculate the maximum, average, and minimum number of friends per user, users with the most friends, and users with a specified minimum number of friends.
Complete Connections: Check if any user in the network knows everyone.

#### How to Run
Dependencies: Python 3.x (no additional libraries required).
Clone Repository:
git clone <repository_url>  
cd <repository_directory>  

#### Run the Program:
To utilize this program, users can run the run SocialNetwork.py function, inputting the desired social network file and user ID for friend recommendations. The code validates user input and provides a recommended friend based on common connections

Functions:
Test individual functions using the Python shell or within the script.
Input Files: Provided sample files (net1.txt, net2.txt, etc.) simulate social networks.
SocialNetwork.py: Main script containing all functions and logic.

Notes
User IDs may not be consecutive.
Friendships are bidirectional and listed once (user_u < user_v).


Feel free to explore the functions and modify the script for different use cases!







