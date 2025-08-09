# Social Network Friend Recommendations 🌐

## Overview

This Python program recommends potential friends in a social network based on the number of common friends between users. The algorithm suggests the most likely new friend for a user, excluding current friends. 

### Features:
- **Friendship Network Creation**: Parse and structure friendship data from input files into a 2D list.
- **Friend Recommendation**: Suggest the best friend for a user based on shared friendships.
- **Common Friends**: Identify common friends between two users.
- **Statistical Insights**: Calculate the maximum, average, and minimum number of friends per user, users with the most friends, and users with a specified minimum number of friends.
- **Complete Connections**: Check if any user in the network knows everyone.

---

## Technologies Used

- **Python 3.x**: The program is built using Python and does not require any additional libraries.

  ![Python](https://img.shields.io/badge/Python-%233776AB.svg?logo=python&logoColor=white)

---

## How to Run 🚀

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Run the Program

## To Utilize This Program:

### 1. Run the `SocialNetwork.py` Script:
- Execute the main script to start the program. 
- The script will prompt you for a social network data file and a user ID for friend recommendations.

### 2. User Input:
- Input the desired **social network file** (e.g., `net1.txt`, `net2.txt`) when prompted.
- Provide a **user ID** to receive friend recommendations based on common connections.

### 3. Program Flow:
- The code will validate your input to ensure the correct file and user ID are provided.
- The program will then process the data and provide a **recommended friend**, excluding current friends.

---

## Functions Available:

You can test and utilize individual functions by running them directly in the Python shell or within the script.

### 1. **Friendship Network Creation**:
- Parse and structure friendship data into a 2D list.

### 2. **Friend Recommendation**:
- Suggest the best friend for a user based on shared friendships.

### 3. **Common Friends**:
- Identify common friends between two users.

### 4. **Statistical Insights**:
- Calculate the maximum, average, and minimum number of friends per user.

### 5. **Complete Connections**:
- Check if any user in the network knows everyone.

---

## Input Files:

The provided sample files (e.g., `net1.txt`, `net2.txt`) simulate social networks. Each line in the file represents a friendship relationship, e.g., `user_u < user_v`. These files will be used as input for the program to analyze and provide recommendations.

---

## Notes:

- **User IDs** may not be consecutive in the data.
- **Friendships are bidirectional**: If `user_u < user_v` appears, it means **user_u** is friends with **user_v** and vice versa.

---







