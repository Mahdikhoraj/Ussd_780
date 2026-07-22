# Ussd_780
This is command code version of *780#
📞 USSD Simulator (*780#)
A terminal-based simulation of a mobile operator's USSD menu (e.g. *780#), built with Python — complete with an interactive graphical dialer UI powered by Textual.

The project simulates purchasing internet packages, call charges, and travel tickets (train/bus/plane), as well as checking account balance, all through an interactive text-based menu system.

✨ Features
🎹 Graphical dialer interface: an interactive keypad built with Textual for entering the *780# code
🌐 Internet package purchases: daily, weekly, monthly, and yearly plans with multiple options
💳 Call charge purchases: hourly, daily, and monthly plans
🎫 Travel ticket booking: train, bus, and plane, with randomly generated dates/times for the next 6 days
💰 Account balance display (simulated)
🔐 Transaction confirmation via second password: generates a random one-time password and validates it before every purchase (OTP-style simulation)
📝 Transaction history logging: every choice is timestamped and saved to users.txt
✅ Input validation: phone numbers, card numbers, and menu choices are validated with regex
⏱️ Smart timeouts: password and card number prompts time out automatically (inputimeout)
🗂️ Project Structure
Ussd_main/
├── main.py               # Entry point; drives the main menu flow
├── welcome.py             # Welcome message and the graphical dialer UI (DialerApp)
├── Internets.py           # Internet package definitions and prices
├── charges.py             # Call charge package definitions and prices
├── timer.py               # Generates ticket dates/times/prices
├── option.py              # Purchase logic and balance deduction for each package type
├── get_value.py           # Collects and validates user input (phone, card, password, choice)
├── vallidation.py         # Validation helpers (regex for phone, card, etc.)
├── show.py                # Renders menus in the terminal
├── show_secend_pass.py    # Generates the random second password (OTP)
├── files.py                # Reads/writes users.txt and password.txt
├── style.tcss              # Textual CSS styling for the dialer UI
├── requirements.txt        # Project dependencies
└── .gitignore
users.txt and password.txt are created automatically on first run and are excluded from version control via .gitignore.

⚙️ Requirements
Python 3.11+ (tested with Python 3.14)
pip
🚀 Installation & Usage
1. Clone the repository

git clone https://github.com/<your-username>/ussd-simulator.git
cd ussd-simulator/Ussd_main
2. Create a virtual environment (optional but recommended)

python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate
3. Install dependencies

pip install -r requirements.txt
4. Run the app

python main.py
🎮 How to Use
On launch, a dialer keypad appears; enter *780# and press the 📞 CALL button.

From the main menu, choose one of the following options:

Option	Action
1	Buy an internet package
2	Buy call charge
3	Show balance
4	Book a travel ticket
5	View transaction history
6	Exit
To complete a purchase, enter your phone number, a 16-digit card number, and the second password displayed in the terminal.

The transaction result and updated balance are shown and logged to users.txt.

🛠️ Built With
Python
Textual — terminal UI (TUI) framework
inputimeout — input prompts with a timeout
📌 Notes
This project is built purely for learning and simulation purposes — it is not connected to any real telecom operator or payment gateway. Balances and transactions are randomly generated and stored locally.
Card numbers and passwords are only checked for correct format; no real banking service is involved.
🤝 Contributing
Suggestions and bug reports are welcome — feel free to open an issue or pull request.

👥 Authors
Mahdi Khoraj — github.com/Mahdikhoraj
Marzieh Sarsangy — github.com/Marzieh-82
📄 License
This project is licensed under the MIT License.
