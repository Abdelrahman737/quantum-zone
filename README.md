# Quantum Zone

**AI-Powered E-commerce Order Automation System**

An intelligent e-commerce platform specializing in premium brand electronics, smartphones, laptops, peripherals, and more. Orders are automatically processed and validated through AI-driven workflows.

---

## Features

- **Product Catalog**: Browse high-end electronics with multiple variants (colors, sizes, specs)
- **Customer Accounts**: Registration, login, and saved address management
- **Smart Ordering**: Place orders with automated processing via n8n workflows
- **AI Validation**: AI-powered order validation and fraud detection
- **Order Tracking**: Real-time status updates with full order history
- **Invoice Generation**: Automatic invoice creation upon order confirmation
- **Admin Dashboard**: Manage products, inventory, orders, and view analytics

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Python, FastAPI, Uvicorn |
| **Database** | MySQL (XAMPP) |
| **Automation** | n8n (workflow engine) |
| **AI** | AI-assisted order validation |

---

## Project Structure

```
Quantum-Zone/
├── Backend/
│   ├── main.py                   # FastAPI entry point
│   ├── config.py                 # Environment configuration
│   ├── database.py               # MySQL connection pool
│   ├── auth.py                   # JWT & password utilities
│   └── routes/                   # API route modules
├── Frontend/
│   ├── index.html                # Landing / home page
│   ├── css/                      # Stylesheets
│   ├── js/                       # JavaScript modules
│   └── assets/                   # Images, icons, fonts
├── .gitignore
└── README.md
```

---

## Getting Started

### Prerequisites
- Python 3.10+
- XAMPP (MySQL)

### Backend Setup
1. Start XAMPP and ensure MySQL is running
2. Set up the database via phpMyAdmin
3. Run the backend:
```bash
cd Backend
pip install -r requirements.txt
uvicorn main:app --reload
```
API documentation: `http://localhost:8000/docs`

---

## License

This project is part of a Final Year Project (FYP) at Multimedia University (MMU).
