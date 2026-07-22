# 📞 USSD 780 Simulator

A terminal-based simulation of the \*780# USSD service, built with Python.  
The project includes an interactive graphical dialer powered by Textual and simulates common telecom services such as purchasing internet packages, buying call charges, booking travel tickets, and checking account balance.

> Note: This project is for educational purposes only and is not connected to any real telecom operator or payment gateway.

---

## ✨ Features

- 📱 Interactive graphical dialer built with Textual
- 🌐 Purchase internet packages (daily, weekly, monthly, yearly)
- 📞 Purchase call charge packages (hourly, daily, monthly)
- 🎫 Book travel tickets (train, bus, and plane)
- 📅 Randomly generated travel dates and departure times (within the next 6 days)
- 💰 Simulated account balance
- 🔐 OTP-style transaction confirmation using a randomly generated second password
- 📝 Transaction history with timestamps saved to users.txt
- ✅ Input validation using regular expressions
- ⏱️ Input timeout for card number and password using inputimeout

---

## 📂 Project Structure

text
Ussd_main/
│
├── main.py                # Entry point
├── welcome.py             # Welcome screen and Textual dialer
├── Internets.py           # Internet packages
├── charges.py             # Call charge packages
├── timer.py               # Ticket date/time generator
├── option.py              # Purchase logic
├── get_value.py           # User input collection
├── vallidation.py         # Regex validation helpers
├── show.py                # Menu rendering
├── show_secend_pass.py    # OTP generator
├── files.py               # Read/write local files
├── style.tcss             # Textual styles
├── requirements.txt       # Project dependencies
└── .gitignore


users.txt and password.txt are created automatically on the first run and are ignored by Git.

---

## ⚙️ Requirements

- Python 3.11 or later (tested with Python 3.14)
- pip

---

## 🚀 Installation

### 1. Clone the repository

bash
git clone https://github.com/<your-username>/ussd-simulator.git
cd ussd-simulator/Ussd_main


### 2. Create a virtual environment (optional)

Windows

bash
python -m venv .venv
.venv\Scripts\activate


Linux / macOS

bash
python -m venv .venv
source .venv/bin/activate


### 3. Install dependencies

bash
pip install -r requirements.txt


### 4. Run the application

bash
python main.py


---

## 🎮 Usage

1. Launch the application.
2. Enter ***780#** using the graphical dialer.
3. Press the 📞 CALL button.
4. Select one of the available services:

| Option | Action |
|:------:|--------|
| 1 | Buy an internet package |
| 2 | Buy call charge |
| 3 | Check account balance |
| 4 | Book a travel ticket |
| 5 | View transaction history |
| 6 | Exit |

To complete a purchase, provide:

- Phone number
- 16-digit bank card number
- Generated OTP (second password)

After each successful transaction:

- The account balance is updated.
- The transaction is saved to users.txt.

---

## 🛠️ Built With

- Python
- Textual
- inputimeout
- Regular Expressions (Regex)

---

## 📌 Disclaimer

This application is a learning project.

- It is not connected to any real telecom operator.
- It does not communicate with any real banking or payment system.
- All balances, transactions, and OTPs are simulated and stored locally.

---

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

Feel free to open an Issue or submit a Pull Request.

---

## 👥 Authors

- Mahdi Khoraj — https://github.com/Mahdikhoraj
- Marzieh Sarsangy — https://github.com/Marzieh-82

---

## 📄 License

This project is licensed under the MIT License.