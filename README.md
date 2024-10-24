## About Diji

This is Diji! 

Diji is a short game created using Python's pygame library that generates random paths towards several target objects. The main objective of the game is to collect all targets using the most efficient route based on the user's order of collection. The paths are stored in a graph as vertices and edges after the random generation. In the background, "Diji" will be running Dikjstra's algorithm to compare the algorithm's optimal path in pixels to the player's path. The final score is calculated as a percentage.

> [!NOTE] 
> this game is not meant to be challenging and is meant to display Dikjstra's capabilities in a game-like context.

![dijipic](https://github.com/user-attachments/assets/ba6d0384-718a-4a58-8680-83285016ff3e)

<img src="https://github.com/user-attachments/assets/ba6d0384-718a-4a58-8680-83285016ff3e" alt="My Image" width="300"/>

## Technologies Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Pygame](https://img.shields.io/badge/pygame-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Prerequisites

Before attempting to clone the repo, make sure you have installed the necessary tools:

1. Python 3.x: You can download Python from the official [Python website](https://www.python.org/).
2. Pygame Library: Install Pygame using **pip install pygame**.

# Installation Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/alecreates/DIJI.git
    cd DIJI
    ```

2. (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Mac/Linux
    venv\Scripts\activate     # For Windows
    ```

3. Install dependencies (if not done already):
    ```bash
    pip install pygame
    ```

4. Run the game:
    ```bash
    python game.py
    ```

# Additional Notes
Exiting the Game: You can usually exit the game by closing the game window or pressing Esc.<br>
Troubleshooting: If you encounter any issues with running the game, ensure you have the correct version of Python and that Pygame is properly installed.<br>
>[!NOTE]
> To play again, press escape and run **python game.py** again in the terminal.


