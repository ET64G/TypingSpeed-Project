"""
Test Controller Module
Manages test state, timing, and calculations for the typing speed test.
"""

import time


class TestController:
    """Manages the state and calculations for typing tests"""
    
    def __init__(self):
        self.test_state = "idle"  # idle, running, paused, completed
        self.test_mode = "fixed_time"  # fixed_time or fixed_text
        self.start_time = None
        self.elapsed_time = 0
        self.time_limit = 60  # seconds for fixed_time mode
        
        # Typing metrics
        self.total_chars = 0
        self.correct_chars = 0
        self.incorrect_chars = 0
        self.user_input = ""
        self.sample_text = ""
        self.current_position = 0
        
        # Results
        self.final_wpm = 0
        self.final_accuracy = 0
        self.words_completed = 0
        
    def start_test(self, mode="fixed_time", time_limit=60, sample_text=""):
        """Start a new typing test"""
        self.test_state = "running"
        self.test_mode = mode
        self.time_limit = time_limit
        self.sample_text = sample_text
        self.start_time = time.time()
        self.elapsed_time = 0
        self.total_chars = 0
        self.correct_chars = 0
        self.incorrect_chars = 0
        self.user_input = ""
        self.current_position = 0
        self.final_wpm = 0
        self.final_accuracy = 0
        self.words_completed = 0
        
    def pause_test(self):
        """Pause the current test"""
        if self.test_state == "running":
            self.test_state = "paused"
            # Calculate elapsed time up to pause
            if self.start_time:
                self.elapsed_time = time.time() - self.start_time
                
    def resume_test(self):
        """Resume a paused test"""
        if self.test_state == "paused":
            self.test_state = "running"
            # Adjust start time to account for paused duration
            if self.start_time:
                self.start_time = time.time() - self.elapsed_time
                
    def stop_test(self):
        """Stop the current test"""
        if self.test_state in ["running", "paused"]:
            self.test_state = "completed"
            if self.start_time:
                self.elapsed_time = time.time() - self.start_time
            self.calculate_final_results()
            
    def reset_test(self):
        """Reset the test to initial state"""
        self.test_state = "idle"
        self.start_time = None
        self.elapsed_time = 0
        self.total_chars = 0
        self.correct_chars = 0
        self.incorrect_chars = 0
        self.user_input = ""
        self.current_position = 0
        self.final_wpm = 0
        self.final_accuracy = 0
        self.words_completed = 0
        
    def update_input(self, user_input):
        """Update user input and recalculate metrics"""
        if self.test_state != "running":
            return
            
        self.user_input = user_input
        self.current_position = len(user_input)
        self.total_chars = len(user_input)
        
        # Count correct and incorrect characters
        self.correct_chars = 0
        self.incorrect_chars = 0
        
        for i in range(min(len(user_input), len(self.sample_text))):
            if user_input[i] == self.sample_text[i]:
                self.correct_chars += 1
            else:
                self.incorrect_chars += 1
        
        # Check if test should end (fixed_text mode)
        if self.test_mode == "fixed_text":
            if self.current_position >= len(self.sample_text):
                self.stop_test()
                return True  # Test completed
        
        return False  # Test still running
        
    def update_time(self):
        """Update elapsed time and check if time limit reached"""
        if self.test_state == "running" and self.start_time:
            self.elapsed_time = time.time() - self.start_time
            
            # Check if time limit reached (fixed_time mode)
            if self.test_mode == "fixed_time":
                if self.elapsed_time >= self.time_limit:
                    self.stop_test()
                    return True  # Time limit reached
        
        return False  # Still running
        
    def get_current_wpm(self):
        """Calculate current WPM"""
        if self.elapsed_time > 0:
            # WPM = (characters / 5) / (time in minutes)
            wpm = (self.total_chars / 5) / (self.elapsed_time / 60)
            return max(0, wpm)  # Ensure non-negative
        return 0
        
    def get_current_accuracy(self):
        """Calculate current accuracy percentage"""
        if self.total_chars > 0:
            accuracy = (self.correct_chars / self.total_chars) * 100
            return accuracy
        return 0
        
    def get_progress(self):
        """Get progress percentage (for fixed_text mode)"""
        if self.test_mode == "fixed_text" and len(self.sample_text) > 0:
            progress = (self.current_position / len(self.sample_text)) * 100
            return min(100, progress)
        return 0
        
    def get_words_completed(self):
        """Count words completed"""
        if not self.user_input:
            return 0
        
        # Count words by splitting on whitespace
        words = self.user_input.split()
        return len(words)
        
    def calculate_final_results(self):
        """Calculate final test results"""
        self.final_wpm = self.get_current_wpm()
        self.final_accuracy = self.get_current_accuracy()
        self.words_completed = self.get_words_completed()
        
    def get_results(self):
        """Get final test results as a dictionary"""
        return {
            "wpm": round(self.final_wpm, 1),
            "accuracy": round(self.final_accuracy, 1),
            "time_taken": round(self.elapsed_time, 2),
            "total_chars": self.total_chars,
            "correct_chars": self.correct_chars,
            "incorrect_chars": self.incorrect_chars,
            "words_completed": self.words_completed,
            "test_mode": self.test_mode
        }
        
    def is_running(self):
        """Check if test is currently running"""
        return self.test_state == "running"
        
    def is_completed(self):
        """Check if test is completed"""
        return self.test_state == "completed"

