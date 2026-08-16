# 🔐 Password Strength Checker

A simple Python-based **Password Strength Checker** developed as part of **DecodeLabs Cyber Security Project 1**.

This project evaluates a password based on multiple security criteria and classifies it as **Weak, Medium, or Strong**.

## 🎯 Project Objective

The main objective of this project is to understand basic cybersecurity concepts such as:

* String handling
* Conditional logic
* Password validation
* Security criteria
* Basic risk evaluation

The program checks whether a password meets important security requirements before determining its overall strength.

## 🚀 Features

The Password Strength Checker evaluates:

* ✅ Password length
* ✅ Uppercase letters
* ✅ Numbers
* ✅ Special characters
* ✅ Overall password strength
* ✅ Feedback for missing security requirements

## 📊 Strength Levels

| Score | Strength  |
| ----- | --------- |
| 0–1   | 🔴 Weak   |
| 2–3   | 🟡 Medium |
| 4     | 🟢 Strong |

## 🛠️ Technologies Used

* **Python 3**
* **Regular Expressions (`re`)**
* Conditional Statements
* Functions
* String Handling

## 📁 Project Structure

```text
Password-strength-checker-/
│
├── password_strength_checker.py
└── README.md
```

## 💻 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/GhulamMurtaza-cyber/Password-strength-checker-.git
```

### 2. Open the project folder

```bash
cd Password-strength-checker-
```

### 3. Run the program

```bash
python password_strength_checker.py
```

## 🧪 Example

```text
========================================
     PASSWORD STRENGTH CHECKER
========================================

Enter your password: Decode@123

Password Strength: Strong
Great! Your password is strong.
```

### Weak Password Example

```text
Enter your password: 123

Password Strength: Weak

Suggestions:
- Use at least 8 characters.
- Add at least one uppercase letter.
- Add at least one special character.
```

### Medium Password Example

```text
Enter your password: Abcdefgh1

Password Strength: Medium

Suggestions:
- Add at least one special character.
```

## 🔒 Security Logic

The program assigns points according to the following criteria:

```text
Length >= 8 characters       → +1
Uppercase letter             → +1
Number                       → +1
Special character            → +1
```

The final score determines the password strength:

```text
Score 4       → Strong
Score 2–3     → Medium
Score 0–1     → Weak
```

## 📚 Learning Outcomes

Through this project, I practiced:

* Python functions
* Regular expressions
* String validation
* Conditional statements
* User input handling
* Basic cybersecurity logic
* Building a practical security-focused application

## 🎓 Project Information

**Program:** Cyber Security Industrial Training
**Project:** Project 1 — Password Strength Checker
**Batch:** 2026
**Organization:** DecodeLabs

The project brief describes this as the foundational project for evaluating security risk through string handling and conditional logic.

## 📌 Future Improvements

Possible improvements include:

* Checking passwords against commonly leaked passwords
* Adding more character variety requirements
* Adding a graphical user interface
* Adding a password generator
* Adding a password entropy calculation
* Improving password security recommendations

## 👨‍💻 Author

**Ghulam Murtaza**

Cyber Security Student | Python Learner | Cybersecurity Enthusiast

---

⭐ If you find this project useful, consider giving the repository a star!

**Building today, securing tomorrow. 🔐**
