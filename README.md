# 🎙️ AI Voice Assistant (Speech-to-Speech)

A real-time **AI-powered voice assistant** built using Python that listens to user speech, processes it using an LLM, and responds back with natural AI-generated voice.

---

## 🚀 Features

* 🎤 Speech-to-Text (STT) using microphone input
* 🧠 AI-powered responses using OpenAI GPT
* 🔊 Natural Text-to-Speech (TTS) voice output
* ⚡ Fast response with local command handling
* 🔁 Continuous listening loop (real-time interaction)

---

## 🧩 Tech Stack

| Component          | Technology Used                |
| ------------------ | ------------------------------ |
| Speech Recognition | `speech_recognition`           |
| AI Model           | OpenAI GPT (`gpt-4o-mini`)     |
| Text-to-Speech     | OpenAI TTS (`gpt-4o-mini-tts`) |
| Audio Playback     | `pygame`                       |
| Language           | Python                         |

---

## 🧠 System Architecture

```
User Speech 🎤
     ↓
Speech Recognition (STT)
     ↓
Text Command
     ↓
Local Logic Layer ⚡ (time, exit, etc.)
     ↓
OpenAI GPT (LLM)
     ↓
Response Text
     ↓
AI Text-to-Speech (TTS)
     ↓
Voice Output 🔊
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd <your-folder>
```

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install openai speechrecognition pygame pyaudio
```

> ⚠️ If `pyaudio` fails on Windows, install using:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## 🔑 Setup API Key

### Option 1 (Recommended)

Set environment variable:

```bash
setx OPENAI_API_KEY "your_api_key_here"
```

Restart terminal after this.

---

### Option 2 (Quick)

Add directly in code:

```python
client = OpenAI(api_key="your_api_key_here")
```

---

## ▶️ Usage

Run the assistant:

```bash
python ai_voice_assistant.py
```

---

## 🗣️ Example Interaction

```
Bot: AI assistant started
Listening...

You: What’s the time right now?
Bot: The time is 10:45

You: Tell me a joke
Bot: Why don’t programmers like nature? Too many bugs!
```

---

## ⚡ Key Functionalities

### 🎤 Speech Input

* Captures audio using microphone
* Handles ambient noise adjustment
* Uses timeout to prevent freezing

---

### 🧠 AI Processing

* Sends user query to GPT model
* Generates short, conversational responses

---

### 🔊 Voice Output

* Converts response into natural AI-generated voice
* Plays audio using pygame

---

### ⚡ Local Optimization

* Handles simple queries like:

  * Time
  * Exit command
* Reduces API calls and latency

---

## 🧪 Challenges & Fixes

| Problem               | Solution                      |
| --------------------- | ----------------------------- |
| Mic blocking/freezing | Added timeout & phrase limits |
| TTS not working       | Switched to OpenAI neural TTS |
| API key errors        | Used environment variables    |
| Long response delay   | Limited GPT response length   |

---

## 📈 Future Improvements

* Wake word detection (“Hey Assistant”)
* Interrupt speech mid-response
* Conversation memory (context-aware replies)
* GUI interface
* Emotion-based voice responses

---

## 📌 Summary

This project demonstrates a **complete speech-to-speech AI pipeline**, combining:

* Real-time voice input
* Intelligent r

