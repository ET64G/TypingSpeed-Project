# Typing Speed Test Application - Pseudocode

## Main Application Flow

```
PROGRAM TypingSpeedTest

    INITIALIZE Application
        CREATE main window
        SET window title: "Eions Typing Speed Test"
        SET window size: 800x600
        SET color scheme (mint, peach, lavender)
        
        INITIALIZE test_mode = "fixed_time"
        INITIALIZE difficulty = "medium"
        CREATE TestController instance
        CREATE TextGenerator instance
        INITIALIZE sample_text = ""
        INITIALIZE user_input = ""
        
        CALL create_ui()
        CALL load_sample_text()
    END INITIALIZE

    FUNCTION create_ui()
        CREATE header frame with title
        CREATE mode selector (Fixed Time / Fixed Text)
        CREATE difficulty selector (Easy / Medium / Hard)
        CREATE "New Text" button
        CREATE text display area (read-only)
        CREATE input field (initially disabled)
        CREATE "Start" button
        CREATE "Reset" button
    END FUNCTION

    FUNCTION load_sample_text()
        IF test is running THEN
            SHOW warning message
            RETURN
        END IF
        
        GET text from TextGenerator based on difficulty
        SET sample_text = generated text
        UPDATE text display with sample_text
    END FUNCTION

    FUNCTION start_test()
        IF sample_text is empty THEN
            SHOW error message
            RETURN
        END IF
        
        IF test is already running THEN
            RETURN
        END IF
        
        GET test mode (fixed_time or fixed_text)
        SET time_limit = 60 seconds (for fixed_time mode)
        
        CALL test_controller.start_test(mode, time_limit, sample_text)
        CLEAR input field
        ENABLE input field
        FOCUS input field
        DISABLE "Start" button
        ENABLE "Reset" button
        
        BIND keyboard events (KeyPress, KeyRelease)
        CALL update_timer()
    END FUNCTION

    FUNCTION reset_test()
        CALL test_controller.reset_test()
        CLEAR user_input
        DISABLE input field
        CLEAR input field
        UNBIND keyboard events
        ENABLE "Start" button
        DISABLE "Reset" button
    END FUNCTION

    FUNCTION on_key_press(event)
        IF test is not running THEN
            RETURN "break" (prevent input)
        END IF
        
        IF key is navigation key (BackSpace, Delete, arrows, etc.) THEN
            ALLOW key (return normally)
        END IF
        
        IF key is Control+C, Control+V, Control+X, Control+A THEN
            RETURN "break" (prevent clipboard operations)
        END IF
    END FUNCTION

    FUNCTION on_key_release(event)
        IF test is not running THEN
            RETURN
        END IF
        
        GET current input from input field
        SET user_input = current input
        
        CALL test_controller.update_input(user_input)
        GET test_completed flag
        
        IF test_completed THEN
            CALL end_test()
        END IF
    END FUNCTION

    FUNCTION end_test()
        CALL test_controller.stop_test()
        DISABLE input field
        UNBIND keyboard events
        ENABLE "Start" button
        CALL show_results()
    END FUNCTION

    FUNCTION update_timer()
        IF test is running THEN
            CALL test_controller.update_time()
            GET time_reached flag
            
            IF time_reached THEN
                CALL end_test()
                RETURN
            END IF
            
            SCHEDULE update_timer() after 100ms
        END IF
    END FUNCTION

    FUNCTION show_results()
        GET results from test_controller
        CREATE ResultsWindow with results
    END FUNCTION

END PROGRAM
```

## Test Controller Flow

```
CLASS TestController

    INITIALIZE
        SET test_state = "idle"
        SET test_mode = "fixed_time"
        SET start_time = None
        SET elapsed_time = 0
        SET time_limit = 60
        SET total_chars = 0
        SET correct_chars = 0
        SET incorrect_chars = 0
        SET user_input = ""
        SET sample_text = ""
        SET current_position = 0
        SET final_wpm = 0
        SET final_accuracy = 0
        SET words_completed = 0
    END INITIALIZE

    FUNCTION start_test(mode, time_limit, sample_text)
        SET test_state = "running"
        SET test_mode = mode
        SET time_limit = time_limit
        SET sample_text = sample_text
        SET start_time = current time
        RESET all metrics to zero
    END FUNCTION

    FUNCTION update_input(user_input)
        IF test_state != "running" THEN
            RETURN False
        END IF
        
        SET user_input = user_input
        SET current_position = length of user_input
        SET total_chars = length of user_input
        
        RESET correct_chars = 0
        RESET incorrect_chars = 0
        
        FOR each character position i from 0 to min(length of user_input, length of sample_text)
            IF user_input[i] == sample_text[i] THEN
                INCREMENT correct_chars
            ELSE
                INCREMENT incorrect_chars
            END IF
        END FOR
        
        IF test_mode == "fixed_text" THEN
            IF current_position >= length of sample_text THEN
                CALL stop_test()
                RETURN True  // Test completed
            END IF
        END IF
        
        RETURN False  // Test still running
    END FUNCTION

    FUNCTION update_time()
        IF test_state == "running" AND start_time exists THEN
            SET elapsed_time = current time - start_time
            
            IF test_mode == "fixed_time" THEN
                IF elapsed_time >= time_limit THEN
                    CALL stop_test()
                    RETURN True  // Time limit reached
                END IF
            END IF
        END IF
        
        RETURN False  // Still running
    END FUNCTION

    FUNCTION stop_test()
        SET test_state = "completed"
        IF start_time exists THEN
            SET elapsed_time = current time - start_time
        END IF
        CALL calculate_final_results()
    END FUNCTION

    FUNCTION calculate_final_results()
        SET final_wpm = CALL get_current_wpm()
        SET final_accuracy = CALL get_current_accuracy()
        SET words_completed = CALL get_words_completed()
    END FUNCTION

    FUNCTION get_current_wpm()
        IF elapsed_time > 0 THEN
            wpm = (total_chars / 5) / (elapsed_time / 60)
            RETURN max(0, wpm)
        END IF
        RETURN 0
    END FUNCTION

    FUNCTION get_current_accuracy()
        IF total_chars > 0 THEN
            accuracy = (correct_chars / total_chars) * 100
            RETURN accuracy
        END IF
        RETURN 0
    END FUNCTION

    FUNCTION get_words_completed()
        IF user_input is empty THEN
            RETURN 0
        END IF
        
        SPLIT user_input by whitespace into words
        RETURN count of words
    END FUNCTION

    FUNCTION get_results()
        RETURN dictionary containing:
            - wpm (rounded to 1 decimal)
            - accuracy (rounded to 1 decimal)
            - time_taken (rounded to 2 decimals)
            - total_chars
            - correct_chars
            - incorrect_chars
            - words_completed
            - test_mode
    END FUNCTION

END CLASS
```

## Text Generator Flow

```
CLASS TextGenerator

    STATIC VARIABLES:
        EASY_TEXTS = array of simple, short texts
        MEDIUM_TEXTS = array of medium complexity texts
        HARD_TEXTS = array of complex, technical texts

    FUNCTION get_text(difficulty, random_selection)
        IF difficulty == "easy" THEN
            SET texts = EASY_TEXTS
        ELSE IF difficulty == "hard" THEN
            SET texts = HARD_TEXTS
        ELSE
            SET texts = MEDIUM_TEXTS
        END IF
        
        IF random_selection == True THEN
            RETURN random text from texts array
        ELSE
            RETURN first text from texts array
        END IF
    END FUNCTION

END CLASS
```

## Results Window Flow

```
CLASS ResultsWindow

    FUNCTION __init__(parent, results)
        CREATE new window (Toplevel)
        SET window title: "Test Results"
        SET window size: 500x400
        CENTER window on parent
        MAKE window modal
        CALL create_ui()
    END FUNCTION

    FUNCTION create_ui()
        CREATE title label: "Test Results"
        CREATE results frame with label: "Your Performance"
        
        DISPLAY WPM (main metric, large and bold)
        DISPLAY Accuracy percentage
        DISPLAY Time taken
        CREATE separator line
        DISPLAY "Detailed Statistics" label
        DISPLAY Total characters
        DISPLAY Correct characters (green)
        DISPLAY Incorrect characters (red)
        DISPLAY Words completed
        DISPLAY Test mode
        
        CREATE "Close" button
    END FUNCTION

END CLASS
```

## Main Program Entry Point

```
FUNCTION main()
    CREATE Tkinter root window
    CREATE TypingTestApp instance with root
    START main event loop (root.mainloop())
END FUNCTION

PROGRAM START
    CALL main()
END PROGRAM
```

