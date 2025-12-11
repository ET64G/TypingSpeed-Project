"""
Results Window Module
Displays typing test results in a separate window.
"""

import tkinter as tk
from tkinter import ttk


class ResultsWindow:
    """Window to display typing test results"""
    
    def __init__(self, parent, results):
        """
        Initialize results window
        
        Args:
            parent: Parent window
            results: Dictionary containing test results
        """
        self.parent = parent
        self.results = results
        
        # Create window
        self.window = tk.Toplevel(parent)
        self.window.title("Test Results")
        self.window.geometry("500x400")
        self.window.resizable(False, False)
        
        # Center window on parent
        self.center_window()
        
        # Make window modal
        self.window.transient(parent)
        self.window.grab_set()
        
        self.create_ui()
        
    def center_window(self):
        """Center the window on the parent window"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
        
    def create_ui(self):
        """Create the results window UI"""
        # Main frame
        main_frame = ttk.Frame(self.window, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="Test Results", font=("Arial", 20, "bold"))
        title_label.pack(pady=(0, 20))
        
        # Results frame
        results_frame = ttk.LabelFrame(main_frame, text="Your Performance", padding="15")
        results_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # WPM (main metric)
        wpm_frame = ttk.Frame(results_frame)
        wpm_frame.pack(fill=tk.X, pady=10)
        ttk.Label(wpm_frame, text="Words Per Minute:", font=("Arial", 12)).pack(side=tk.LEFT)
        wpm_value = ttk.Label(wpm_frame, text=f"{self.results['wpm']}", 
                             font=("Arial", 16, "bold"), foreground="blue")
        wpm_value.pack(side=tk.LEFT, padx=10)
        
        # Accuracy
        accuracy_frame = ttk.Frame(results_frame)
        accuracy_frame.pack(fill=tk.X, pady=10)
        ttk.Label(accuracy_frame, text="Accuracy:", font=("Arial", 12)).pack(side=tk.LEFT)
        accuracy_value = ttk.Label(accuracy_frame, text=f"{self.results['accuracy']}%", 
                                   font=("Arial", 14, "bold"))
        accuracy_value.pack(side=tk.LEFT, padx=10)
        
        # Time taken
        time_frame = ttk.Frame(results_frame)
        time_frame.pack(fill=tk.X, pady=10)
        ttk.Label(time_frame, text="Time Taken:", font=("Arial", 12)).pack(side=tk.LEFT)
        ttk.Label(time_frame, text=f"{self.results['time_taken']} seconds", 
                 font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
        
        # Separator
        separator = ttk.Separator(results_frame, orient=tk.HORIZONTAL)
        separator.pack(fill=tk.X, pady=15)
        
        # Detailed stats
        details_label = ttk.Label(results_frame, text="Detailed Statistics", 
                                 font=("Arial", 11, "bold"))
        details_label.pack(pady=(5, 10))
        
        # Characters typed
        chars_frame = ttk.Frame(results_frame)
        chars_frame.pack(fill=tk.X, pady=5)
        ttk.Label(chars_frame, text="Total Characters:", font=("Arial", 10)).pack(side=tk.LEFT)
        ttk.Label(chars_frame, text=str(self.results['total_chars']), 
                 font=("Arial", 10)).pack(side=tk.LEFT, padx=10)
        
        # Correct characters
        correct_frame = ttk.Frame(results_frame)
        correct_frame.pack(fill=tk.X, pady=5)
        ttk.Label(correct_frame, text="Correct Characters:", font=("Arial", 10), 
                 foreground="green").pack(side=tk.LEFT)
        ttk.Label(correct_frame, text=str(self.results['correct_chars']), 
                 font=("Arial", 10), foreground="green").pack(side=tk.LEFT, padx=10)
        
        # Incorrect characters
        incorrect_frame = ttk.Frame(results_frame)
        incorrect_frame.pack(fill=tk.X, pady=5)
        ttk.Label(incorrect_frame, text="Incorrect Characters:", font=("Arial", 10), 
                 foreground="red").pack(side=tk.LEFT)
        ttk.Label(incorrect_frame, text=str(self.results['incorrect_chars']), 
                 font=("Arial", 10), foreground="red").pack(side=tk.LEFT, padx=10)
        
        # Words completed
        words_frame = ttk.Frame(results_frame)
        words_frame.pack(fill=tk.X, pady=5)
        ttk.Label(words_frame, text="Words Completed:", font=("Arial", 10)).pack(side=tk.LEFT)
        ttk.Label(words_frame, text=str(self.results['words_completed']), 
                 font=("Arial", 10)).pack(side=tk.LEFT, padx=10)
        
        # Test mode
        mode_frame = ttk.Frame(results_frame)
        mode_frame.pack(fill=tk.X, pady=5)
        ttk.Label(mode_frame, text="Test Mode:", font=("Arial", 10)).pack(side=tk.LEFT)
        mode_text = "Fixed Time" if self.results['test_mode'] == "fixed_time" else "Fixed Text"
        ttk.Label(mode_frame, text=mode_text, font=("Arial", 10)).pack(side=tk.LEFT, padx=10)
        
        # Close button
        close_button = ttk.Button(main_frame, text="Close", command=self.window.destroy)
        close_button.pack(pady=10)

