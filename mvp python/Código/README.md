**# Running Duelo Binario**

## Requirements:

- Python 3.10 or higher  
- Tkinter  

---

### **1. Create and activate a virtual environment:**

```bash
python -m venv env
```

```bash
. env/bin/activate
```

---

### **2. Install Tkinter:**

#### **On Linux:**

```bash
sudo apt install python3-tk
```

The command may vary depending on your operating system. Check your system documentation for details.  

---

### **3. Run the game:**

In the `src` folder, execute the following command:  

```bash
python3 main.py <mode>
```

- Replace `<mode>` with either `1` or `2`.  
- **Mode 1**: Both players use the same machine locally.  
- **Mode 2**: Uses the DOG server (unstable and not recommended for smooth gameplay).  

**Note:**  
This program is tested and works well on Linux and Windows systems.  
We do not recommend its use on macOS, as its functionality there is unstable.  

---

## **Game Instructions**

1. **Choose the game mode:**  
   - **Mode 1 (Local Play):** Both players alternate turns on the same device.  
   - **Mode 2 (DOG Server):** Connects to the DOG server for remote play (connection issues and delays may occur).

2. **Starting the Game:**  
   Once the game is launched:  
   - For **Mode 1**, simply follow the on-screen prompts to take turns.  
 -  For **Mode 2**, ensure both players are connected. One player must click on "Iniciar partida" in the menu and wait for the server to establish the match between both players connected to the server. 

3. **Gameplay:**  
   - Insert a binary digit (`0` or `1`) into any empty white cell.
   - Send move clicking in "Enviar jogada"
   - The goal is to surround a black cell with four binary digits.  
   - When all four surrounding white cells of a black cell are filled, the player who placed the last digit scores the points corresponding to the binary value formed.  

4. **End of the Game:**  
   - The game ends when all possible cells are filled.  
   - The player with the highest score wins.  

---

**Important Notes on DOG Server:**  
Mode 2 uses a server connection that can experience delays and instability, potentially impacting gameplay. For the best experience, use Mode 1.  
