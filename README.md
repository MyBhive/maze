## ***[]()MAZE:*****

> (It is a on level maze)
> Help MacGyver to escape the maze!

`Size:`
It’s a 15x15 maze.

1 sprite = 30x30 pixels

`Uses:`
**Use the arrows from your keyboard to move** the player inside the structure.

`Goal:`
**You need to collect all of the 3 items** (a needle, a pipe and ether) to build a syringe and put the guard to sleep. That’s his only way to go out! 
You just need to go on the top of an item to collect it. It will directly go to your inventory (your inventory is visible below during the game).

**If you meet the guard without all 3 items, the guard will kill you.** 
At the moment that your player is at the same position as the guard, the game stops. You need to close the window and restart the game to play one more time.
The items change their places at each new start of the game.

---------------------------------------------------------------------------------------------
[]()**RUN THE GAME:**

`Installation required:`

Inside the folder "setting" open the file "install.py"
!! Don’t forget to run cmd or powershell as administrator !

To start the game after that, inside the folder "game" open the file "Run_game.py"

----------------------------------------------------------------------------------------------
[]()**FEATURES:**

`Encoding:`
Python 3

`Launched:`
Pygame
(works with Pygame 1 and 2)

`Fork:`
https://github.com/MyBhive/maze.git

-----------------------------------------------------------------------------------------------
[]()**DESCRIPTION:**

`Folder`

| Resource | Contain all the necessary images to build the project |
| -------- | ----------------------------------------------------- |
|          |                                                       |

`Python files`

| **Install.py**    | file to install “requirement.txt”                            |
| ----------------- | ------------------------------------------------------------ |
| **Characters.py** | Mother class Character  + Children classes : MacGyver and Guardian |
| **Constant.py**   | Constant necessaries in the game                             |
| **Controller.py** | Import of all the classes to structure the global game       |
| **Item.py**       | Class item (name, position and collect)                      |
| **Labyrinthe.py** | Class Labyrinthe to analyse "laby.txt" and create all the method necessary to run the maze structure |
| **View.py**       | Loading of the images and initiate the texts necessaries in the game |
| **Run_game.py**   | File to start the game                                       |

`Text files`

| Laby.txt        | structure of the maze (“M” for McGyver, “G” for Guardian, “O” for walls and “.” for path) |
| --------------- | ------------------------------------------------------------ |
| Requirement.txt |                                                              |

​	



----------------------------------------------------------------------------------------------
[]()**TO CONTRIBUTE:** 

> You need to respect PEP8 !!!  

- Fork it 

- Create your feature branch

-  Commit your changes

- Push to your branch 

- Create a pull request

-----------------------------------------------------------------------------------------------
##### []()**WRITTEN BY:**

> MyBhive 
>

*My most sincere thanks to Geoffrey who helped me a lot to understand the python programming logic.*