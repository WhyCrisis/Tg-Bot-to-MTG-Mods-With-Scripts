# MTG MODS — Telegram Bot for Script Automation

A simple, clean, and efficient Telegram bot designed to distribute automation scripts, libraries, and comprehensive configuration guides. Built with Python and modern asynchronous frameworks.

---

## 📜 Project Lore (How it Started)

### Background & Pitch
While looking for real-world production concepts to expand my portfolio, I discovered a series of highly useful automation scripts created by the author behind the [MTGMODS](https://github.com/MTGMODS) ecosystem (Bohdan). However, they lacked a centralized, user-friendly interface for seamless sharing and deployment through mobile platforms. 

I reached out to Bohdan with a polite and transparent proposal to wrap his public scripts into an intuitive Telegram bot layout — offering full credit attribution, transparent bot statistics, and potentially API features.

### The Outcome & The Decision
Bohdan didn't reply. Instead of letting a great development opportunity fade due to absolute silence, I learned a vital software engineering lesson: **Sometimes you don't need permission to learn, adapt, and build.** 

The original scripts remain publicly accessible, and this project does not claim ownership over them. This bot serves as a custom interface wrapper to maximize utility and ease of use. If any script author explicitly requests the removal of their work, it will be complied with immediately. Until then: **I build, I learn, and I publish.**

---

## 🚀 Key Features

* **File Distribution**: Clean interface for downloading configuration scripts and binaries directly through Telegram.
* **Modular Codebase**: Split architecture separates UI components (`keyboards`), text engines (`texts`), and operational routers.
* **User-Friendly Navigation**: Dynamically rendered inline menus and call-to-action buttons for smooth user journeys.

---

## 🛠️ Tech Stack & Architecture

* **Language**: Python 3.11+
* **Framework**: `aiogram` (Modern Asynchronous Telegram Bot API framework)
* **Environment Management**: `python-dotenv` for isolating secure API tokens
* **Current Status**: Pure working MVP with asset-based navigation. No database dependency for instant deployment and fast response times.

---


## 📄 License & Attributions

* **Core Interface & Bot Architecture**: Developed independently by **WhyCrisis**.
* **Automation Content & Original Scripts**: All credits for the foundational scripts, configurations, and core logic belong entirely to the original creator and the [MTGMODS](https://github.com/MTGMODS) repository ecosystem.

## 💻 Installation & Local Deployment

1. **Clone the repository:**
```bash
   git clone [https://github.com/WhyCrisis/Tg-Bot-to-MTG-Mods-With-Scripts.git](https://github.com/WhyCrisis/Tg-Bot-to-MTG-Mods-With-Scripts.git)
   cd Tg-Bot-to-MTG-Mods-With-Scripts
