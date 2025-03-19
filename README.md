# **Tic-Tac-Toe – A Simple Python Game Using Tkinter**  

## **Overview**  
This is a **Tic-Tac-Toe** game built using **Python and Tkinter** (Python's built-in GUI library). It allows two players to play alternately and determines the winner based on classic Tic-Tac-Toe rules. The game includes a **restart button**, a **turn indicator**, and an **automatic win/tie detection system**.  

## **Features**  
✅ **Two-Player Mode** – Play alternately as 'X' and 'O'.  
✅ **Graphical Interface** – Built with **Tkinter** for an interactive experience.  
✅ **Turn Indicator** – Displays whose turn it is.  
✅ **Win/Tie Detection** – Highlights the winning sequence and declares a tie if applicable.  
✅ **Restart Button** – Allows resetting the game at any point.  
✅ **Compact & Responsive UI** – Automatically centers on the screen.  

---

## **Gameplay**  
🎯 **Objective:** Get three marks in a row, column, or diagonal before your opponent.  
🎮 **Controls:**  
- Click on an empty box to place your mark ('X' or 'O').  
- **The game automatically checks for a winner or a tie**.  
- Press **"Restart"** to start a new game.  

---
## **Code Structure**  
📂 **Project Structure:**  
```
/tic-tac-toe
│── tic tac toe.py     # Main game script
```

### **Key Components in `tic tac toe.py`**
📌 **GUI Setup (Tkinter Window & Buttons):**  
- The game board is created using a **3x3 grid of buttons**.  
- A **label** at the top displays the **current player's turn**.  
- A **restart button** resets the game state.  

📌 **Game Logic:**  
- **Player Turn Handling:** Alternates turns between ‘X’ and ‘O’.  
- **Win Checking:** Scans rows, columns, and diagonals to determine a winner.  
- **Tie Detection:** If all 9 spaces are filled and there’s no winner, the game declares a tie.  
- **Color Highlighting:** The winning combination is highlighted.  

📌 **Restart Mechanism:**  
- Resets the board while keeping player ‘X’ as the starting player.  

---

## **Future Improvements (Ideas for Contributions)**
🚀 **Enhancements:**  
✅ Add **AI Mode** (Single-player with computer opponent).  
✅ Implement a **score tracker** to keep track of wins/losses.  
✅ Improve the UI with better styling and animations.  
✅ Add **a difficulty setting** (Easy, Medium, Hard).  

---

## **Contributing**  
Feel free to **fork the repo**, suggest improvements, or fix bugs. PRs are welcome! 🤝  
