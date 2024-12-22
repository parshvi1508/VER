import streamlit as st
import time
import random

# Custom CSS for room themes and styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(45deg, #1a0f0f, #2c1810);
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff4b1f, #ff9068);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(255, 75, 31, 0.3);
    }
    
    /* Room Theme Styles */
    .quantum-lab {
        background: linear-gradient(45deg, #2E1437, #480048);
        padding: 2rem;
        border-radius: 10px;
        border: 1px solid rgba(255, 0, 255, 0.2);
        position: relative;
        overflow: hidden;
    }
    .cyber-hub {
        background: linear-gradient(45deg, #1A2980, #26D0CE);
        padding: 2rem;
        border-radius: 10px;
        border: 1px solid rgba(38, 208, 206, 0.2);
    }
    .neural-nexus {
        background: linear-gradient(45deg, #FF4B1F, #FF9068);
        padding: 2rem;
        border-radius: 10px;
        border: 1px solid rgba(255, 75, 31, 0.2);
    }
    .binary-vault {
        background: linear-gradient(45deg, #8E2DE2, #4A00E0);
        padding: 2rem;
        border-radius: 10px;
        border: 1px solid rgba(142, 45, 226, 0.2);
    }
    .ai-sanctum {
        background: linear-gradient(45deg, #20002c, #cbb4d4);
        padding: 2rem;
        border-radius: 10px;
        border: 1px solid rgba(32, 0, 44, 0.2);
    }
    
    /* Room Decorations */
    .room-decor {
        position: absolute;
        top: 0;
        right: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        opacity: 0.1;
        background-size: 20px 20px;
        background-image: 
            linear-gradient(to right, rgba(255,255,255,0.1) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(255,255,255,0.1) 1px, transparent 1px);
    }
    
    /* Door Animation */
    .door-effect {
        position: relative;
        padding: 20px;
        border: 2px solid rgba(255, 144, 104, 0.3);
        border-radius: 5px;
        margin: 10px 0;
        transition: all 0.3s ease;
    }
    .door-effect:before {
        content: '🚪';
        position: absolute;
        right: 10px;
        top: 50%;
        transform: translateY(-50%);
        font-size: 24px;
    }
    
    /* Success/Error Messages */
    .success-msg {
        color: #00ff00;
        font-weight: bold;
        padding: 1rem;
        border-radius: 5px;
        background: rgba(0, 255, 0, 0.1);
        animation: glow 1.5s ease-in-out infinite alternate;
    }
    .error-msg {
        color: #ff4b1f;
        font-weight: bold;
        padding: 1rem;
        border-radius: 5px;
        background: rgba(255, 75, 31, 0.1);
    }
    
    /* Progress Bar */
    .progress-container {
        width: 100%;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        margin: 1rem 0;
    }
    .progress-bar {
        background: linear-gradient(45deg, #ff4b1f, #ff9068);
        height: 10px;
        border-radius: 10px;
        transition: width 0.5s ease-in-out;
    }
    
    /* Room Title */
    .room-title {
        color: white;
        font-size: 1.8rem;
        text-align: center;
        text-shadow: 0 0 10px rgba(255,255,255,0.5);
        margin-bottom: 1rem;
    }
     .css-18e3th9 {
        text-align: center;
        border: 3px solid #FF6600;  /* Neon Orange Border */
        padding: 10px;
        border-radius: 10px;
    }

    /* Style for the Streamlit markdown with neon orange border and centered */
    .css-1v0mbdj {
        text-align: center;
        border: 3px solid #FF6600;  /* Neon Orange Border */
        padding: 10px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Define rooms with themed questions
rooms = [
    {
        "name": "Quantum Computing Lab",
        "theme_class": "quantum-lab",
        "description": "Where quantum bits dance in superposition",
        "question": "🌌 In this realm of quantum possibility, I exist in multiple states until observed. What am I?",
        "answer": "qubit",
        "hints": [
            "I can be both 0 and 1",
            "I power quantum computers",
            "Schrödinger's cat would understand me"
        ],
        "difficulty": "🌟🌟",
        "points": 20
    },
    {
        "name": "Cybersecurity Hub",
        "theme_class": "cyber-hub",
        "description": "Fortress of digital defense",
        "question": "🔐 I am the guardian of secrets, unbreakable yet transparent. What am I?",
        "answer": "encryption",
        "hints": [
            "I protect data",
            "I use complex mathematics",
            "I am essential for secure communication"
        ],
        "difficulty": "🌟🌟🌟",
        "points": 30
    },
    # Add more rooms following the same pattern...
    {
        "name": "Neural Network Nexus",
        "theme_class": "neural-nexus",
        "description": "Where artificial neurons spark intelligence",
        "question": "🧠 I learn from patterns, evolve with data, yet I'm not alive. What am I?",
        "answer": "ai",
        "hints": [
            "I mimic human intelligence",
            "I use neural networks",
            "I can recognize patterns"
        ],
        "difficulty": "🌟🌟🌟",
        "points": 40
    },
    {
        "name": "Binary Vault",
        "theme_class": "binary-vault",
        "description": "The foundation of all digital existence",
        "question": "💻 I speak in only two digits, yet I can express anything. What am I?",
        "answer": "binary",
        "hints": [
            "I am the language of computers",
            "I only use 0s and 1s",
            "I am the foundation of digital logic"
        ],
        "difficulty": "🌟🌟🌟🌟",
        "points": 50
    },
    {
        "name": "AI Sanctum",
        "theme_class": "ai-sanctum",
        "description": "Where machine learning masters meditate",
        "question": "🤖 I predict the future by learning from the past. What am I?",
        "answer": "machine_learning",
        "hints": [
            "I improve with experience",
            "I find patterns in data",
            "I make predictions based on training"
        ],
        "difficulty": "🌟🌟🌟🌟🌟",
        "points": 60
    }
]

# Initialize session state
if 'current_room' not in st.session_state:
    st.session_state.current_room = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'hints_shown' not in st.session_state:
    st.session_state.hints_shown = 0
if 'wrong_attempts' not in st.session_state:
    st.session_state.wrong_attempts = 0

# Title and description
st.title("🌅 Dawn Tech Unplugged")
st.markdown("### Virtual Escape Room Challenge")

# Display current progress
progress = (st.session_state.current_room / len(rooms)) * 100
st.markdown(f"""
    <div class="progress-container">
        <div class="progress-bar" style="width: {progress}%;"></div>
    </div>
    <p style="color: #ff9068;">Escape Progress: {progress:.0f}%</p>
""", unsafe_allow_html=True)

# Display current score
st.markdown(f"""
    <h3 style="color: #ff4b1f;">Score: {st.session_state.score} points</h3>
""", unsafe_allow_html=True)

# Display current room
if st.session_state.current_room < len(rooms):
    current_room = rooms[st.session_state.current_room]
    
    # Room display
    st.markdown(f"""
        <div class="{current_room['theme_class']}">
            <div class="room-decor"></div>
            <h2 class="room-title">{current_room['name']}</h2>
            <p style="color: white; opacity: 0.8;">{current_room['description']}</p>
            <div class="door-effect">
                <p style="color: white; font-size: 1.2rem;">{current_room['question']}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Hint system
    if st.button("🔍 Request Hint"):
        if st.session_state.hints_shown < len(current_room['hints']):
            st.markdown(f"""
                <div style="padding: 1rem; background: rgba(255, 144, 104, 0.1); border-radius: 5px;">
                    <p style="color: #ff9068;">Hint #{st.session_state.hints_shown + 1}: {current_room['hints'][st.session_state.hints_shown]}</p>
                </div>
            """, unsafe_allow_html=True)
            st.session_state.hints_shown += 1
    
    # Answer input
    answer = st.text_input("Enter the code to unlock the door:", key=f"answer_{st.session_state.current_room}")
    
    if st.button("🚪 Unlock Door"):
        if answer.lower().replace(" ", "_") == current_room['answer']:
            # Success animation and message
            st.markdown("""
                <div class="success-msg">
                    🎉 Door Unlocked! Proceeding to next room...
                </div>
            """, unsafe_allow_html=True)
            st.balloons()
            
            # Update score and progress
            st.session_state.score += current_room['points']
            st.session_state.current_room += 1
            st.session_state.hints_shown = 0
            st.session_state.wrong_attempts = 0
            
            time.sleep(2)
            st.rerun()
        else:
            # Error message
            st.session_state.wrong_attempts += 1
            st.markdown(f"""
                <div class="error-msg">
                    🚫 Invalid code! Security level increased. Attempts: {st.session_state.wrong_attempts}
                </div>
            """, unsafe_allow_html=True)
else:
    # Escape completion message
    st.markdown(f"""
        <div style="text-align: center; padding: 2rem;">
            <h1 style="color: #ff4b1f;">🎉 Congratulations!</h1>
            <p style="color: white; font-size: 1.2rem;">You've successfully escaped from Dawn Tech!</p>
            <p style="color: #ff9068; font-size: 1.5rem;">Final Score: {st.session_state.score} points</p>
        </div>
    """, unsafe_allow_html=True)
    st.balloons()