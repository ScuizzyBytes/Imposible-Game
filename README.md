# 🐍 Impossible Game

A brutal, minimal, grid-based Snake implementation built with Python and Pygame.

---

### 💬 About The Project

Let's be real: this is definitely not the most advanced or feature-complete Snake game out there. It has its flaws, limitations, and room for improvement. 

However, I built this from scratch to master Pygame, modular code design, event loops, and array manipulation for snake mechanics. I spent time getting everything to work, so I'm pushing it here as part of my coding journey! 🚀

---

### 🛠 Tech & Architecture

- **Modular Design:** Clean separation of concerns with standalone scripts (`cubes.py`, `create_snake.py`, and `main.py`).
- **Grid System:** Custom coordinate mapping on a $20 \times 20$ grid ($25\text{px}$ cells).
- **Movement Engine:** Efficient head-insertion and tail-popping list manipulation (`snake_body.insert(0, new_head)` & `snake_body.pop()`).

---

### 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Impossible-Game.git](https://github.com/YOUR_USERNAME/Impossible-Game.git)
