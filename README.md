&#x20;**Snake Game 🐍**



A classic Snake game built with Python's Turtle module, featuring modern enhancements like levels, color-changing snakes, and progressive difficulty.



About

This is an enhanced version of the classic Snake game where you control a snake that grows longer as it consumes food. The game features a leveling system, dynamic snake colors, increasing difficulty, and sound effects for an engaging gaming experience.



\## ✨ Features



\- \*\*Classic Gameplay\*\*: Traditional snake game mechanics

\- \*\*Level System\*\*: Progress through levels as you score points

\- \*\*Dynamic Colors\*\*: Snake changes color based on the food consumed

\- \*\*Progressive Difficulty\*\*: Speed increases with each level

\- \*\*High Score Tracking\*\*: Compete with your best score

\- \*\*Pause Functionality\*\*: Pause and resume gameplay anytime

\- \*\*Sound Effects\*\*: Audio feedback for eating food and game over

\- \*\*Safe Boundaries\*\*: Clearly defined play area with border collision

\- \*\*Smooth Controls\*\*: Responsive arrow key controls



📸 Screenshots

&#x20;Gameplay (Paused)



!\[Paused Game](screenshots/paused.png)



\### Game Over

!\[Game Over](screenshots/gameover.png)



\## 📥 Installation



1\. \*\*Clone or download the repository:\*\*

&#x20;  ```bash

&#x20;  git clone <repository-url>

&#x20;  cd snake-game

&#x20;  ```



2\. \*\*Ensure you have Python 3.6+ installed:\*\*

&#x20;  ```bash

&#x20;  python --version

&#x20;  ```



3\. \*\*No additional installation required!\*\* 

&#x20;  The game uses Python's built-in `turtle` module.



&#x20;  > \*\*Note:\*\* Sound effects require Windows OS (uses `winsound` module). On macOS/Linux, the game will work but without sound.



\## 🚀 Usage



Run the game using Python:



```bash

python snake\_game.py

```



The game window will open with a 500x500 pixel playing area.



\## 🎹 Controls



| Key | Action |

|-----|--------|

| ⬆️ \*\*Up Arrow\*\* | Move Up |

| ⬇️ \*\*Down Arrow\*\* | Move Down |

| ⬅️ \*\*Left Arrow\*\* | Move Left |

| ➡️ \*\*Right Arrow\*\* | Move Right |

| \*\*Spacebar\*\* | Pause/Resume Game |

| \*\*R\*\* | Restart Game |



\## ⚙️ Game Mechanics



\### Scoring System

\- \*\*Each Food\*\*: +10 points

\- \*\*High Score\*\*: Automatically saved during gameplay



\### Level System

\- \*\*Level 1\*\*: Starting level (speed: 120ms)

\- \*\*Level 2\*\*: Unlocks at 50 points

\- \*\*Level 3\*\*: Unlocks at 100 points

\- \*\*Formula\*\*: `Level = (Score // 50) + 1`



\### Speed Progression

\- Speed increases as you level up

\- Minimum delay: 40ms

\- Speed reduction: `delay -= level` after each food



\### Color System

\- \*\*Snake Head\*\*: Always Yellow

\- \*\*Snake Body\*\*: Changes to match the color of food eaten

\- \*\*Food Colors\*\*: Red, Blue, Yellow, Purple, Cyan (random)



\### Game Over Conditions

\- Collision with border walls

\- Collision with snake's own body



\## 📁 Project Structure



```

snake-game/

│

├── snake\_game.py          # Main game file

├── screenshots/           # Game screenshots

│   ├── gameplay.png

│   ├── paused.png

│   └── gameover.png

└── README.md             # This file

```



\## 📦 Requirements



\- \*\*Python\*\*: 3.6 or higher

\- \*\*Operating System\*\*: 

&#x20; - Windows (full features with sound)

&#x20; - macOS/Linux (game works without sound)



\### Built-in Modules Used

\- `turtle` - Graphics and game rendering

\- `random` - Random food spawning and colors

\- `winsound` - Sound effects (Windows only)



\##  Game Specifications



\- \*\*Screen Size\*\*: 500x500 pixels

\- \*\*Grid Cell Size\*\*: 20x20 pixels

\- \*\*Safe Play Area\*\*: 480x480 pixels (with margins)

\- \*\*Initial Snake Length\*\*: 3 segments

\- \*\*Starting Direction\*\*: Up

\- \*\*Initial Speed\*\*: 120ms delay



\## 🛠️ Code Architecture



\### Key Functions

\- `draw\_border()` - Renders the game boundary

\- `spawn\_food()` - Places food at random locations

\- `move()` - Main game loop and snake movement

\- `update\_score()` - Updates score display

\- `game\_over()` - Handles game over state

\- `toggle\_pause()` - Pause/resume functionality

\- `reset\_game()` - Restarts the game



\### Global Variables

\- `score` - Current score

\- `high\_score` - Best score

\- `level` - Current level

\- `d` - Movement delay (speed)

\- `saap` - Snake body segments list

\- `kata` - Current direction



\## 👨‍ Credits


\*\*Game Title\*\*: Snake Game 🐍


\## 📄 License

This project is open source and available for educational purposes.

\*\*Enjoy the game! 🎮\*\*

\*Press R to start playing!\*



