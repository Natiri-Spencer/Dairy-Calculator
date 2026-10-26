# KIAMBU DAIRY CO-OP CALCULATOR

**Version:** v1.0

A simple command-line application for calculating payments owed to dairy farmers based on milk supplied and the current buying price.

## Features

- Enter farmer name
- Enter litres supplied
- Automatically reads current buying price from `price.txt`
- Calculates total payment due
- Includes input validation
- Uses a fallback default price if `price.txt` is missing

---

## Requirements

- Python 3.8+

Verify installation:

```bash
python --version
```

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Natiri-Spencer/dairy-payment-calculator.git
cd dairy-payment-calculator
```

### 2. Create the price file

Create a file named:

```text
price.txt
```

Example contents:

```text
60
```

This means the current buying price is:

```text
KES 60 per litre
```

### 3. Run the application

```bash
python dairy_calculator.py
```

---

## Example Output

```text
Kiambu Dairy Co-op Payment Calculator
-------------------------------------
Current buying price: KES 58.00 per litre

Farmer name: John Kamau
Litres supplied today: 125

Payment Summary
----------------
Farmer : John Kamau
Litres : 125.00
Price  : KES 58.00/litre
Total  : KES 7,250.00
```

---

## Default Behavior

If `price.txt` is missing or contains invalid data, the system uses:

```text
KES 55.00 per litre
```

as the default buying price.

---

## Version

### v1.0

- Farmer payment calculation
- Buying price loaded from file
- Input validation
- Graceful fallback price
- Command-line interface
