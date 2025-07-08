import streamlit as st
import json
from datetime import datetime

st.title("📅 PlanPal - Your Daily AI Scheduler")

# Task input
task = st.text_input("What's your task?")

# Time input
selected_time = st.time_input("Select time", value=datetime.now().time())

# Save Task Button
if st.button("Save Task"):
    new_task = {
        "task": task,
        "time": selected_time.strftime('%I:%M %p')  # clean format
    }
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

    tasks.append(new_task)
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)
    st.success("✅ Task saved successfully!")

# Show My Plan Button
if st.button("Show My Plan"):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        if tasks:
            st.subheader("📋 Your Tasks:")
            for t in tasks:
                st.write(f"🕒 {t['time']} - {t['task']}")
        else:
            st.info("You haven't added any tasks yet.")
    except FileNotFoundError:
        st.warning("⚠️ No tasks found yet.")

import streamlit as st
import speech_recognition as sr

st.title("🎙️ Voice Assistant Enabled - PlanPal")

recognizer = sr.Recognizer()

if st.button("🎤 Speak Your Task"):
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = recognizer.listen(source)
        try:
            task_text = recognizer.recognize_google(audio)
            st.success(f"📝 You said: {task_text}")
        except sr.UnknownValueError:
            st.error("Could not understand audio.")
        except sr.RequestError:
            st.error("Could not request results; check internet.")

    # Now you can auto-fill the task field with task_text

    import streamlit as st
import json
from datetime import datetime
import speech_recognition as sr
import pyttsx3

# Voice engine
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening... Speak your task")
        audio = r.listen(source, timeout=5)
    try:
        query = r.recognize_google(audio)
        st.success(f"🗣️ You said: {query}")
        return query
    except sr.UnknownValueError:
        st.error("❌ Could not understand. Try again.")
        return ""
    except sr.RequestError:
        st.error("❌ Voice service not available.")
        return ""

# App Title
st.title("📅 PlanPal - Your Daily AI Scheduler")

# Input manually or by voice
task = st.text_input("What's your task?")
if st.button("🎤 Speak Task"):
    task = listen()

# Time selection
time = st.time_input("Select time", value=datetime.now().time())

# Save task
if st.button("Save Task"):
    if task.strip() == "":
        st.warning("Please enter or speak a task.")
    else:
        new_task = {"task": task, "time": str(time)}
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
        except FileNotFoundError:
            tasks = []

        tasks.append(new_task)
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=2)
        st.success("✅ Task saved!")
        speak("Your task has been saved!")

# Show saved tasks
if st.button("📋 Show My Plan"):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        if not tasks:
            st.info("📭 No tasks saved.")
        for t in tasks:
            st.write(f"🕒 {t['time']} - {t['task']}")
    except FileNotFoundError:
        st.warning("⚠️ No tasks file found.")

import streamlit as st
import json
from datetime import datetime

st.title("📅 PlanPal - Aapka Daily AI Scheduler")

task = st.text_input("📌 Aapka task kya hai?")
time = st.time_input("⏰ Time select karo")

if st.button("💾 Task Save Karo"):
    new_task = {"task": task, "time": str(time)}
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

    tasks.append(new_task)
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)
    st.success("✅ Task save ho gaya!")

if st.button("📋 Mera Plan Dikhao"):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        for t in tasks:
            st.write(f"🕒 {t['time']} - {t['task']}")
    except FileNotFoundError:
        st.warning("⚠️ Abhi tak koi task save nahi hua.")

import streamlit as st
import speech_recognition as sr
import json
from datetime import datetime

st.title("📅 PlanPal - Aapka Daily AI Scheduler")
st.subheader("🎙️ Voice Assistant Enabled - PlanPal")

task = st.text_input("📌 Aapka task kya hai?")
time = st.time_input("⏰ Time select karo")

# Voice input button
if st.button("🎤 Speak Task"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Boliye... Sun raha hoon")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="hi-IN")
            st.success(f"🗣️ Aapne bola: {text}")
            task = text  # overwrite text input with voice
        except sr.UnknownValueError:
            st.warning("⚠️ Maaf kijiye, samajh nahi aaya.")
        except sr.RequestError:
            st.error("❌ Speech service unavailable.")

# Save task button
if st.button("💾 Task Save Karo"):
    new_task = {"task": task, "time": str(time)}
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

    tasks.append(new_task)
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)
    st.success("✅ Task save ho gaya!")

# Show tasks button
if st.button("📋 Mera Plan Dikhao"):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        for t in tasks:
            st.write(f"🕒 {t['time']} - {t['task']}")
    except FileNotFoundError:
        st.warning("⚠️ Abhi tak koi task save nahi hua.")


import streamlit as st
import json
from datetime import datetime

st.title("📅 PlanPal - Your Daily AI Scheduler")

# Unique keys for inputs
task = st.text_input("What's your task?", key="task_input")
time = st.time_input("Select time", key="time_input")

if st.button("Save Task"):
    new_task = {"task": task, "time": str(time)}
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

    tasks.append(new_task)
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)
    st.success("Task saved!")

if st.button("Show My Plan"):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        for t in tasks:
            st.write(f"🕒 {t['time']} - {t['task']}")
    except FileNotFoundError:
        st.warning("No tasks found yet.")
import streamlit as st
import speech_recognition as sr

def listen_task():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Bolna shuru karo... Listening...")
        audio = r.listen(source, timeout=5)
        try:
            text = r.recognize_google(audio, language="hi-IN")  # Hindi/English mixed
            st.success(f"🗣️ Tumne bola: {text}")
            return text
        except sr.UnknownValueError:
            st.error("❌ Kuch samajh nahi aaya.")
        except sr.RequestError:
            st.error("❌ Voice service se connect nahi ho paaya.")
    return ""
 
 