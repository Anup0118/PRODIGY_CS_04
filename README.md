This Python script is a simple keylogger that captures and logs all keystrokes on a keyboard. It uses the pynput library to listen for key press and release events, logging each keystroke to a specified text file.

Features:

  Captures all alphanumeric key presses and special keys.
  Logs key events to a file named key_log.txt.
  Stops logging when the Esc key is pressed.

How It Works

The script defines two callback functions, on_press and on_release, which are triggered on key press and release events, respectively. The Listener class from the pynput.keyboard module is used to monitor these events.

   on_press(key): This function logs the character representation of the key if it is an alphanumeric key. For special keys (like Space, Enter, etc.), it logs the string representation of the key wrapped in square brackets (e.g., [Key.space]).
   
   on_release(key): This function checks if the Esc key is released and stops the listener if it is.
