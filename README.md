PRINCE OF PERSIA: THE TWO THRONES - TRAINER

📌 ABOUT  
This is a game trainer for Prince of Persia: The Two Thrones, created using Python and Cheat Engine.  
It allows players to modify in-game memory to enable cheats such as:  
- Infinite Health  
- Unlimited Sand  
- One-Hit Kills  
- Speed Boost  
- Freeze Timer  

This project showcases how to find and manipulate game memory using Cheat Engine, Python, and pointers.  

----------------------------------------------------

🛠️ HOW I HACKED THE TRAINER  

1️⃣ FINDING MEMORY ADDRESSES  
Using Cheat Engine, I searched for values that represent in-game stats (e.g., health, sand, etc.):  
- Open the game and launch Cheat Engine.  
- Attach Cheat Engine to the game’s process.  
- Search for the in-game value (e.g., health) and apply filters (e.g., taking damage to narrow down addresses).  
- Find the correct memory address holding the value.  

2️⃣ USING POINTERS TO FIND DYNAMIC ADDRESSES  
Since game memory changes each time it loads, I used pointer scanning:  
- Found the health address and checked which instruction modifies it.  
- Used Cheat Engine’s Pointer Scanner to find static base pointers.  
- Repeated the process across multiple game sessions to locate the reliable pointer.  

3️⃣ WRITING THE PYTHON TRAINER  
Once I found the correct memory locations and pointers, I used Python with the pymem library to modify values in real time.  

----------------------------------------------------

🔥 FEATURES  
✅ Infinite Health - Never die in combat.  
✅ Unlimited Sand - Use time powers endlessly.  

----------------------------------------------------

📌 HOW TO USE  
1. Open *Prince of Persia: The Two Thrones*.  
2. Run the trainer script.  
3. Activate cheats using hotkeys (F1/F2)

----------------------------------------------------

📝 NOTES  
- This trainer was created for educational purposes only.  
- Works only on the specific version of Prince of Persia: The Two Thrones (Steam/Ubisoft).  
- Use at your own risk!  

----------------------------------------------------

🎯 FUTURE IMPROVEMENTS  
🔹 Add a user-friendly GUI using PyQt or Tkinter.  
🔹 Improve memory scanning to auto-detect values.  
🔹 Extend support for other Prince of Persia games.  

----------------------------------------------------

💡 CREDITS  
- **Cheat Engine** - For memory scanning & debugging.  
- **Python (pymem)** - For memory manipulation.  
- **Ubisoft** - Developers of Prince of Persia: The Two Thrones.  

Enjoy hacking the sands of time! 😎🔥  
