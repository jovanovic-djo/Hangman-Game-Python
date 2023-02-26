import random
import tkinter as tk

window = tk.Tk()
window.title("Hangman Game")

wordlist_file = "wordlist.txt"
guesses_allowed = 6
letters_guessed = []

with open(wordlist_file, "r") as f:
    wordlist = [line.strip() for line in f]
    
secret_word = random.choice(wordlist)

# Set up the game board
word_display = tk.Label(window, text=" ".join("_" * len(secret_word)))
word_display.pack()

guesses_remaining = tk.Label(window, text=f"Guesses remaining: {guesses_allowed}")
guesses_remaining.pack()

letters_guessed_display = tk.Label(window, text=f"Letters guessed: {', '.join(letters_guessed)}")
letters_guessed_display.pack()

# Define the function for handling a guess
def handle_guess():
    guess = guess_input.get()
    guess_input.delete(0, tk.END)
    
    if guess not in secret_word or guess in letters_guessed:
        guesses_allowed -= 1
        
    letters_guessed.append(guess)
    
    word_display_text = ""
    for letter in secret_word:
        if letter in letters_guessed:
            word_display_text += letter + " "
        else:
            word_display_text += "_ "
            
    word_display.config(text=word_display_text)
    
    guesses_remaining.config(text=f"Guesses remaining: {guesses_allowed}")
    
    letters_guessed_display.config(text=f"Letters guessed: {', '.join(letters_guessed)}")
    
    if "_" not in word_display_text:
        tk.messagebox.showinfo("Congratulations!", "You won!")
        window.destroy()
        
    if guesses_allowed == 0:
        tk.messagebox.showinfo("Game over", f"The secret word was '{secret_word}'.")
        window.destroy()

# Set up the guess input field and button
guess_input = tk.Entry(window)
guess_input.pack()

guess_button = tk.Button(window, text="Guess", command=handle_guess)
guess_button.pack()

# Start the game
window.mainloop()
