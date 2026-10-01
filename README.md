<p align="center">
  <img src="banner.png" alt="IP-Conversion Banner" width="100%">
</p>

# 🌐 IP & Subnet Calculator for Cisco Packet Tracer

A production-ready, modular Python CLI utility designed to automate subnet calculations, IP conversions, and network boundary analysis. This tool was engineered specifically to streamline network design, VLSM mapping, and configuration workflows inside **Cisco Packet Tracer**.

## 🎯 The Core Problem & Solution
* **The Problem:** Configuring routers, switches, and access control lists (ACLs) in **Cisco Packet Tracer** requires constant calculation of subnet boundaries. Manually performing bitwise AND operations, converting masks to binary to find host bits, and calculating exact usable ranges is slow, tedious, and prone to mistakes during lab sessions or CCNA exams.
* **The Solution:** This utility automates the entire subnetting lifecycle. By entering a host IP and a Subnet Mask, the script instantly evaluates the binary structure, isolates the true network address, maps usable host ranges, and logs the results.

---

## 🛠️ Key Features & Capabilities
The application processes raw network data dynamically to output complete diagnostics:
* **Bidirectional Binary Parsing:** Converts standard IPv4 dot-decimal inputs into structured, 8-bit padded binary streams.
* **Automated Host Calculation:** Analyzes subnet mask zeros to compute the maximum number of assignable IP addresses (\(2^n - 2\)).
* **Bitwise AND Logic Matrix:** Performs exact logical multiplication on binary streams to determine the base Network Address.
* **Boundary Mapping:** Instantly calculates the **First Usable IP**, **Last Usable IP**, and the **Broadcast Address**.
* **Persistent History Logging:** Automatically appends every calculation log into an `outputdata.txt` file for easy copying into Cisco IOS device configuration notes.

---

## 📂 Code Architecture

The project follows a clean, modular design separating the core engine, presentation layer, and file I/O operations to maintain the *Single Responsibility Principle*:

```text
IP-Conversion/
├── .gitignore
├── LICENSE
├── README.md
├── main.py
└── App/
    ├── __init__.py
    ├── calculator.py
    ├── logger.py
    └── ui.py
```

---

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/Hades-db/IP-Conversion
   ```
2. Navigate to the project directory:
   ```bash
   cd IP-Conversion
   ```
3. Run the application:
   ```bash
   python main.py
   ```
4. Access your dynamic network log history inside: `outputdata.txt`

---

## 📈 Changelog & Version History

### 🟢 Version 1.0 (Current Stable)
* **Add:** Automated dynamic backup system (Saves all output text analysis to a local text file).
* **Add:** Robust exception handling (Clear visual output showing what caused the runtime error).
* **Fix:** Deep code refactoring (Corrected the appearance, structure, and readability of the code).
* **Fix:** Minor logic bugs fixed.

### 🟡 Version 0.5
* **Add:** Zero-bit analyzer in Subnet Mask binary streams.
* **Add:** Network host pool capacity calculation (\(2^n - 2\)).
* **Add:** Automated calculations for Network Last IP and Broadcast address destinations.
* **Fix:** Restructured mathematical logic inside core functions.
* **Fix:** Improved visual code console output formatting.
