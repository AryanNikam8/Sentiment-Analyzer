import tkinter as tk
from tkinter import messagebox
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    sentiment_scores = sia.polarity_scores(text)
    if sentiment_scores['compound'] > 0.05:
        sentiment = "Positive"
    elif sentiment_scores['compound'] < -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment, sentiment_scores

def get_sentiment():
    user_input = user_input_entry.get()
    
    if user_input.lower() == 'exit':
        root.quit()
    else:
        sentiment, sentiment_scores = analyze_sentiment(user_input)
        
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Sentiment: {sentiment}\n")
        output_text.insert(tk.END, f"Scores: {sentiment_scores}\n")

root = tk.Tk()
root.title("Sentiment Analysis Chatbot")

root.geometry("400x400")
root.config(bg="#0afcb4")

frame = tk.Frame(root, bg="#0afcb4")
frame.pack(padx=20, pady=20, expand=True)

welcome_label = tk.Label(frame, text="Sentiment Analysis Chatbot", font=("Freestyle Script", 24, 'bold'), bg="#0afcb4")
welcome_label.pack(pady=10)

user_input_label = tk.Label(frame, text="Enter your text:", font=("Comic Sans MS", 12), bg="#0afcb4")
user_input_label.pack(pady=5)

user_input_entry = tk.Entry(frame, width=40, font=("MV Boli", 12))
user_input_entry.pack(pady=5)

analyze_button = tk.Button(frame, text="Analyze Sentiment", command=get_sentiment, font=("Comic Sans MS", 12), bg="#c80afc", fg="white")
analyze_button.pack(pady=15)

output_label = tk.Label(frame, text="Sentiment Analysis Output:", font=("Comic Sans MS", 12), bg="#0afcb4")
output_label.pack(pady=5)

output_text = tk.Text(frame, height=10, width=40, font=("MV Boli", 12), wrap=tk.WORD, bg="#f0f8ff", bd=2)
output_text.pack(pady=10)

root.mainloop()
