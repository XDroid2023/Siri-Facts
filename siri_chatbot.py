import random
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import os
import subprocess
import threading
from wave_animation import WaveAnimation

# Set appearance mode and default color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Apple facts database
apple_facts = [
    "Apple was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne.",
    "The company was initially founded to sell the Apple I personal computer kit.",
    "Apple's first logo featured Isaac Newton sitting under an apple tree.",
    "The famous Apple logo was designed in 1977 by Rob Janoff.",
    "The first Macintosh was introduced in 1984 with its iconic '1984' Super Bowl commercial.",
    "Steve Jobs was forced out of Apple in 1985, only to return in 1997.",
    "The iPod was introduced in 2001, revolutionizing the music industry.",
    "The iPhone was first introduced by Steve Jobs in 2007.",
    "Apple became the first U.S. company to reach a $1 trillion market cap in 2018.",
    "The App Store was launched in 2008 with just 500 apps.",
    "Apple's headquarters, Apple Park, opened in 2017 in Cupertino, California.",
    "The Apple Watch was introduced in 2014 and released in 2015.",
    "iOS was originally called iPhone OS until 2010.",
    "Apple acquired Beats Electronics in 2014 for $3 billion.",
    "The first iPad was released in 2010.",
    "Apple's first retail store opened in 2001 in Virginia.",
    "The MacBook Air was introduced in 2008.",
    "Siri was introduced with the iPhone 4S in 2011.",
    "Apple TV was first released in 2007.",
    "The company changed its name from Apple Computer, Inc. to Apple Inc. in 2007.",
    "The first iMac was introduced in 1998.",
    "Apple's Swift programming language was introduced in 2014.",
    "The iTunes Store was launched in 2003.",
    "FaceTime was introduced with the iPhone 4 in 2010.",
    "Apple Maps was launched in 2012.",
    "The Apple Pencil was introduced in 2015.",
    "AirPods were first released in 2016.",
    "Apple Music was launched in 2015.",
    "The Mac Pro was first introduced in 2006.",
    "iCloud was launched in 2011.",
    "Apple Pay was introduced in 2014.",
    "The Apple Watch Series 1 was released in 2016.",
    "Apple's A4 chip was their first custom-designed processor.",
    "The MacBook Pro was first introduced in 2006.",
    "Apple acquired NeXT in 1997 for $429 million.",
    "The first Apple Store outside the US opened in Japan in 2003.",
    "Safari web browser was released in 2003.",
    "The Apple II was introduced in 1977.",
    "Apple's first laptop was the Macintosh Portable in 1989.",
    "The iPod Mini was introduced in 2004.",
    "Apple's first mouse was introduced with the Lisa computer in 1983.",
    "The iTunes Music Store sold its billionth song in 2006.",
    "Apple's first tablet attempt was the Newton MessagePad in 1993.",
    "The iPhone App Store reached 1 million apps in 2013.",
    "Apple introduced the Lightning connector in 2012.",
    "The first iPod could store 1,000 songs.",
    "Apple's first smartphone attempt was the ROKR E1 with Motorola in 2005.",
    "The MacBook was introduced in 2006.",
    "Apple TV+ streaming service launched in 2019.",
    "The first Apple Watch Edition was made with 18-karat gold.",
    "Apple Card was introduced in 2019.",
    "The first iBook was released in 1999.",
    "Apple Arcade was launched in 2019.",
    "The iPod Touch was introduced in 2007.",
    "Apple's first wireless mouse was the Apple Pro Mouse in 2000.",
    "The iPhone 5 was the first iPhone with a Lightning connector.",
    "Apple's first wireless earbuds were the AirPods.",
    "The iPad Mini was introduced in 2012.",
    "Apple's first smartwatch was announced in 2014.",
    "The first Retina Display appeared on the iPhone 4.",
    "Apple's first bluetooth headset was released in 2007.",
    "The MacBook Air was advertised as the world's thinnest notebook.",
    "Apple's first wireless keyboard was released in 2003.",
    "The first iPhone had a 3.5-inch display.",
    "Apple's first touchscreen device was the iPhone.",
    "The iPod Nano was introduced in 2005.",
    "Apple's first webcam was the iSight in 2003.",
    "The Mac mini was introduced in 2005.",
    "Apple's first wireless router was the AirPort in 1999.",
    "The PowerBook was introduced in 1991.",
    "Apple's first color display was the Apple Color Display in 1984.",
    "The first iMac with Intel processor was released in 2006.",
    "Apple's first USB mouse was the Apple USB Mouse in 1998.",
    "The iPod Shuffle was introduced in 2005.",
    "Apple's first LCD display was the Studio Display in 1998.",
    "The first MacBook Pro with Retina display was released in 2012.",
    "Apple's first wireless trackpad was the Magic Trackpad in 2010.",
    "The first iPhone with Face ID was the iPhone X.",
    "Apple's first 64-bit processor was the A7 chip.",
    "The first Apple Watch with cellular was Series 3.",
    "Apple's first noise-cancelling headphones were AirPods Pro.",
    "The first iPad Pro was released in 2015.",
    "Apple's first ARM-based Mac was released in 2020.",
    "The first iMac Pro was released in 2017.",
    "Apple's first 5G iPhone was the iPhone 12 series.",
    "The first MacBook with Touch Bar was released in 2016.",
    "Apple's first wireless charging case was for AirPods.",
    "The first iPhone with wireless charging was iPhone 8.",
    "Apple's first tablet with Face ID was iPad Pro 2018.",
    "The first Mac with Touch ID was the MacBook Pro 2016.",
    "Apple's first over-ear headphones were AirPods Max.",
    "The first iPhone with 5G was iPhone 12.",
    "Apple's first M1 chip was released in 2020.",
    "The first iPad with Apple Pencil support was iPad Pro 2015.",
    "Apple's first device with ProMotion was iPad Pro 2017.",
    "The first iPhone with ProRAW was iPhone 12 Pro.",
    "Apple's first device with LiDAR was iPad Pro 2020.",
    "The first MacBook with Force Touch was in 2015.",
    "Apple's first device with MagSafe charging was iPhone 12.",
    "The first Apple silicon Mac was MacBook Air 2020.",
    "Apple's first spatial audio device was AirPods Pro.",
    "The first iPhone with Always-On display was iPhone 14 Pro.",
    "Apple's first foldable device is yet to be announced.",
    "The first Mac Pro with Apple silicon was released in 2023."
]

class SiriGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Siri - Apple Facts")
        self.root.geometry("800x900")
        self.root.configure(bg='#000000')
        
        # Voice settings
        self.voice_enabled = tk.BooleanVar(value=True)
        self.speaking = False

        # Main frame
        self.main_frame = ctk.CTkFrame(root, fg_color='#000000')
        self.main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Wave animation
        self.wave_canvas = WaveAnimation(self.main_frame, width=760, height=100)
        self.wave_canvas.pack(pady=(0, 20))

        # Title with modern font
        title_frame = ctk.CTkFrame(self.main_frame, fg_color='transparent')
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = ctk.CTkLabel(
            title_frame,
            text="Siri",
            font=("SF Pro Display", 40, "bold"),
            text_color="#FFFFFF"
        )
        title_label.pack()
        
        subtitle_label = ctk.CTkLabel(
            title_frame,
            text="Your Apple Facts Assistant",
            font=("SF Pro Display", 16),
            text_color="#666666"
        )
        subtitle_label.pack()

        # Chat display with modern styling
        self.chat_display = ctk.CTkTextbox(
            self.main_frame,
            width=700,
            height=500,
            font=("SF Pro Text", 14),
            fg_color='#1C1C1E',
            text_color="#FFFFFF",
            wrap="word"
        )
        self.chat_display.pack(pady=(0, 20), fill=tk.BOTH, expand=True)

        # Buttons frame
        button_frame = ctk.CTkFrame(self.main_frame, fg_color='transparent')
        button_frame.pack(fill=tk.X, pady=(0, 20))

        # Modern buttons with hover effects
        self.fact_button = ctk.CTkButton(
            button_frame,
            text="Get Fact",
            command=self.show_fact,
            font=("SF Pro Display", 14, "bold"),
            fg_color="#007AFF",
            hover_color="#0051D5",
            corner_radius=20
        )
        self.fact_button.pack(side=tk.LEFT, padx=5, expand=True)

        self.clear_button = ctk.CTkButton(
            button_frame,
            text="Clear",
            command=self.clear_display,
            font=("SF Pro Display", 14, "bold"),
            fg_color="#333333",
            hover_color="#404040",
            corner_radius=20
        )
        self.clear_button.pack(side=tk.LEFT, padx=5, expand=True)

        self.exit_button = ctk.CTkButton(
            button_frame,
            text="Exit",
            command=self.quit_app,
            font=("SF Pro Display", 14, "bold"),
            fg_color="#FF3B30",
            hover_color="#D70015",
            corner_radius=20
        )
        self.exit_button.pack(side=tk.LEFT, padx=5, expand=True)

        # Voice toggle with modern switch
        self.voice_toggle = ctk.CTkSwitch(
            self.main_frame,
            text="Enable Voice",
            variable=self.voice_enabled,
            font=("SF Pro Display", 12),
            progress_color="#34C759",
            button_color="#FFFFFF",
            button_hover_color="#CCCCCC"
        )
        self.voice_toggle.pack(pady=(0, 10))

        # Welcome message
        self.display_welcome()

    def display_welcome(self):
        welcome_msg = "Welcome to Siri - Your Apple Facts Chatbot!"
        self.display_message(welcome_msg)
        self.speak(welcome_msg)
        
        instructions = "Click 'Get Fact' to learn interesting facts about Apple Inc."
        self.display_message(instructions)
        self.speak(instructions)

    def speak(self, text):
        if self.voice_enabled.get() and not self.speaking:
            self.speaking = True
            def run_speech():
                subprocess.run(['say', '-v', 'Samantha', text])
                self.speaking = False
            threading.Thread(target=run_speech, daemon=True).start()

    def display_message(self, message):
        self.chat_display.configure(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"\n{message}\n")
        self.chat_display.see(tk.END)
        self.chat_display.configure(state=tk.DISABLED)

    def show_fact(self):
        fact = random.choice(apple_facts)
        self.display_message(" " + fact)
        self.speak(fact)

    def clear_display(self):
        self.chat_display.configure(state=tk.NORMAL)
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.configure(state=tk.DISABLED)
        self.display_welcome()

    def quit_app(self):
        self.speak("Goodbye! Have a great day!")
        self.root.after(1000, self.root.quit)

def main():
    root = ctk.CTk()
    app = SiriGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
