import tkinter as tk
from tkinter import ttk, messagebox
from test_controller import TestController
from results_window import ResultsWindow
from text_generator import TextGenerator


class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Retro pastel color scheme
        self.colors = {
            'mint': '#C8E6D5',      # Soft mint green
            'peach': '#FFE5D9',     # Soft peach
            'lavender': '#F0E6FF'   # Soft lavender
        }
        
        # Set root background
        self.root.configure(bg=self.colors['mint'])
        
        # Test state variables
        self.test_mode = tk.StringVar(value="fixed_time")
        self.difficulty = tk.StringVar(value="medium")
        self.test_controller = TestController()
        
        # Text generator
        self.text_generator = TextGenerator()
        self.sample_text = ""
        self.user_input = ""
        
        self.create_ui()
        
    def create_ui(self):
        # Header Frame with peach background
        header_frame = tk.Frame(self.root, bg=self.colors['peach'])
        header_frame.pack(fill=tk.X, padx=10, pady=10)
        
        title_label = tk.Label(header_frame, text="Typing Speed Test", 
                              font=("Arial", 18, "bold"), bg=self.colors['peach'])
        title_label.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Mode and difficulty selector
        controls_frame = tk.Frame(header_frame, bg=self.colors['peach'])
        controls_frame.pack(side=tk.RIGHT)
        
        # Test mode selector
        mode_frame = tk.Frame(controls_frame, bg=self.colors['peach'])
        mode_frame.pack(side=tk.LEFT, padx=10)
        tk.Label(mode_frame, text="Test Mode:", bg=self.colors['peach']).pack(side=tk.LEFT, padx=2)
        ttk.Radiobutton(mode_frame, text="Fixed Time", variable=self.test_mode, 
                       value="fixed_time", command=self.on_mode_change).pack(side=tk.LEFT, padx=2)
        ttk.Radiobutton(mode_frame, text="Fixed Text", variable=self.test_mode, 
                       value="fixed_text", command=self.on_mode_change).pack(side=tk.LEFT, padx=2)
        
        # Difficulty selector
        diff_frame = tk.Frame(controls_frame, bg=self.colors['peach'])
        diff_frame.pack(side=tk.LEFT, padx=10)
        tk.Label(diff_frame, text="Difficulty:", bg=self.colors['peach']).pack(side=tk.LEFT, padx=2)
        diff_combo = ttk.Combobox(diff_frame, textvariable=self.difficulty, 
                                 values=("easy", "medium", "hard"), state="readonly", width=10)
        diff_combo.pack(side=tk.LEFT, padx=2)
        diff_combo.bind("<<ComboboxSelected>>", lambda e: self.load_sample_text())
        
        # New text button
        new_text_button = ttk.Button(controls_frame, text="New Text", command=self.load_sample_text)
        new_text_button.pack(side=tk.LEFT, padx=5)
        
        # Main content area with mint background
        main_frame = tk.Frame(self.root, bg=self.colors['mint'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Text display with lavender background
        text_frame = tk.LabelFrame(main_frame, text="Text to Type",
                                   bg=self.colors['lavender'], fg="#333333",
                                   font=("Arial", 10, "bold"))
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.text_display = tk.Text(text_frame, wrap=tk.WORD, font=("Courier", 12), 
                                   height=15, state=tk.DISABLED, bg="#FFFFFF",
                                   selectbackground=self.colors['mint'])
        self.text_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        text_scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.text_display.yview)
        text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_display.config(yscrollcommand=text_scrollbar.set)
        
        # Bottom frame - Input and controls with peach background
        bottom_frame = tk.Frame(self.root, bg=self.colors['peach'])
        bottom_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(bottom_frame, text="Type here:", bg=self.colors['peach'], 
                font=("Arial", 10, "bold")).pack(anchor=tk.W, padx=10, pady=(10, 5))
        
        self.input_field = tk.Text(bottom_frame, height=3, font=("Courier", 12), 
                                   wrap=tk.WORD, bg="#FFFFFF",
                                   selectbackground=self.colors['mint'])
        self.input_field.pack(fill=tk.X, padx=10, pady=5)
        self.input_field.config(state=tk.DISABLED)
        
        # Control buttons
        button_frame = tk.Frame(bottom_frame, bg=self.colors['peach'])
        button_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.start_button = ttk.Button(button_frame, text="Start", command=self.start_test)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.reset_button = ttk.Button(button_frame, text="Reset", command=self.reset_test, state=tk.DISABLED)
        self.reset_button.pack(side=tk.LEFT, padx=5)
        
        # Load initial text
        self.load_sample_text()
        
    def on_mode_change(self):
        """Handle test mode change"""
        # Reload text when mode changes
        if not self.test_controller.is_running():
            self.load_sample_text()
        
    def load_sample_text(self):
        """Load sample text into the display area"""
        # Don't change text if test is running
        if self.test_controller.is_running():
            messagebox.showwarning("Test Running", "Cannot change text while test is running. Please reset first.")
            return
        
        # Get new text based on difficulty
        self.sample_text = self.text_generator.get_text(difficulty=self.difficulty.get())
        
        # Update display
        self.text_display.config(state=tk.NORMAL)
        self.text_display.delete(1.0, tk.END)
        self.text_display.insert(1.0, self.sample_text)
        self.text_display.config(state=tk.DISABLED)
        
    def start_test(self):
        """Start the typing test"""
        # Validation
        if not self.sample_text or len(self.sample_text.strip()) == 0:
            messagebox.showerror("Error", "No text available. Please load a text first.")
            return
        
        if self.test_controller.is_running():
            return
        
        mode = self.test_mode.get()
        time_limit = 60  # Default 60 seconds for fixed_time mode
        
        try:
            self.test_controller.start_test(mode=mode, time_limit=time_limit, sample_text=self.sample_text)
            self.user_input = ""
            self.input_field.config(state=tk.NORMAL)
            self.input_field.delete(1.0, tk.END)
            self.input_field.focus()
            self.start_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.NORMAL)
            
            # Bind input events
            self.input_field.bind('<KeyPress>', self.on_key_press)
            self.input_field.bind('<KeyRelease>', self.on_key_release)
            
            # Start timer update
            self.update_timer()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start test: {str(e)}")
            
    def reset_test(self):
        """Reset the typing test"""
        self.test_controller.reset_test()
        self.user_input = ""
        self.input_field.config(state=tk.DISABLED)
        self.input_field.delete(1.0, tk.END)
        self.input_field.unbind('<KeyPress>')
        self.input_field.unbind('<KeyRelease>')
        self.start_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)
        
    def on_key_press(self, event):
        """Handle key press events"""
        # Prevent typing if test is not running
        if not self.test_controller.is_running():
            return "break"
        
        # Allow special keys for navigation
        if event.keysym in ['BackSpace', 'Delete', 'Left', 'Right', 'Up', 'Down', 'Home', 'End']:
            return
        
        # Prevent certain key combinations that might interfere
        if event.state & 0x4:  # Control key
            if event.keysym in ['c', 'v', 'x', 'a']:  # Copy, Paste, Cut, Select All
                return "break"  # Prevent clipboard operations during test
        
    def on_key_release(self, event):
        """Handle key release events - update controller after input changes"""
        if not self.test_controller.is_running():
            return
        
        # Get current input text
        current_input = self.input_field.get(1.0, tk.END).rstrip('\n')
        
        # Update user input
        self.user_input = current_input
        
        # Update controller and check if test completed
        test_completed = self.test_controller.update_input(self.user_input)
        
        # End test if completed
        if test_completed:
            self.end_test()
    
    def end_test(self):
        """End the typing test"""
        self.test_controller.stop_test()
        self.input_field.config(state=tk.DISABLED)
        self.input_field.unbind('<KeyPress>')
        self.input_field.unbind('<KeyRelease>')
        self.start_button.config(state=tk.NORMAL)
        
        # Show results window
        self.show_results()
        
    def update_timer(self):
        """Update the timer and check if test should end"""
        if self.test_controller.is_running():
            # Update time in controller
            time_reached = self.test_controller.update_time()
            
            # Check if time limit reached
            if time_reached:
                self.end_test()
                return
            
            self.root.after(100, self.update_timer)
    
    def show_results(self):
        """Show results window"""
        results = self.test_controller.get_results()
        ResultsWindow(self.root, results)


def main():
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

