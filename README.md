# JARVIS-NexusBot 🤖🎙️

A modular, highly customizable AI chatbot and voice assistant built with Python. This project is designed as an open-source starter pack for beginner developers to build their own custom assistant by just changing a single dictionary (`brain`), without rewriting the core logic.

---

## 📂 Project Structure & Versions

### 1️⃣ Version 1.0: Text-Only Skeleton (`NexusBot_Text_v1.0.py`)
- **Zero Dependencies:** Works out of the box on any system without installing external libraries.
- **Clean Logic:** Separated input handling and response dictionary.
- **Echo Fallback:** Guides the user if a command is missing from the brain.

### 2️⃣ Version 1.5: Text-to-Speech Upgrade (`NexusBot_Voice_v1.5.py`)
- **Voice Output:** Integrated `pyttsx4` to make the assistant respond in a clear, real-time voice.
- **Customizable Voices:** Easy configuration to switch between Male `[0]` and Female `[1]` voices via code comments.
- **Maintained Simplicity:** Kept the same modular flow for effortless customization.

---

## 🛠️ Installation & Setup

1. **Clone this repository:**
   ```bash
   git clone [https://github.com/sarthaksharma823/JARVIS-NexusBot.git](https://github.com/sarthaksharma823/JARVIS-NexusBot.git) 

## Required Libraries
-- Pyttsx4 --

# 🎙️ Jarvis 2.0 - Fast & Smart Voice Assistant

A responsive Python-based Desktop Voice Assistant designed to execute voice commands in real-time. **Jarvis 2.0** features optimized audio calibration, zero-delay speech recognition, and custom logic mapping to provide a seamless voice interaction experience.

---

## 🚀 What's New in v2.0?

* **⚡ Fast Ambient Noise Calibration:** Calibrates room noise once at startup instead of every loop iteration, drastically speeding up response times.
* **🎙️ Robust Speech Recognition:** Uses `SpeechRecognition` (Google Speech API) with fine-tuned parameters (`energy_threshold` and `pause_threshold`) for precise voice capture.
* **🔊 Text-to-Speech (TTS):** Integrated offline voice synthesis via `pyttsx4`.
* **🛡️ Crash-Proof Error Handling:** Multi-layer `try-except` blocks ensure the assistant doesn't freeze or crash during silence or internet drops.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Speech Recognition:** `SpeechRecognition`
* **Speech Synthesis:** `pyttsx4`
* **Audio Handling:** `PyAudio`

---

## ⚙️ How to Install & Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Jarvis-2.0.git](https://github.com/YOUR_USERNAME/Jarvis-2.0.git)
   cd Jarvis-2.0
2. Run 'python NexusBot_Text_v1.0.py' in your terminal.
3. Run 'python NexusBot_Text_v1.5.py' in your terminal.
4. Run 'python NexusBot_Text_v2.0.py' in your terminal.
