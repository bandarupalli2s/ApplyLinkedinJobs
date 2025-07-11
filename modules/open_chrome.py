from modules.helpers import make_directories
from config.settings import run_in_background, stealth_mode, disable_extensions, safe_mode, file_name, failed_file_name, logs_folder_path, generated_resume_path
from config.questions import default_resume_path
if stealth_mode:
    import undetected_chromedriver as uc
else: 
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    # from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from modules.helpers import find_default_profile_directory, critical_error_log, print_lg
import atexit
import signal
import os

def cleanup_processes():
    """Cleanup function to terminate all related processes when Chrome is closed"""
    try:
        import psutil
        current_pid = os.getpid()
        current_process = psutil.Process(current_pid)
        
        # Kill all child processes
        for child in current_process.children(recursive=True):
            try:
                child.terminate()
                child.wait(timeout=5)
            except:
                try:
                    child.kill()
                except:
                    pass
    except:
        pass

# Register cleanup function
atexit.register(cleanup_processes)

def signal_handler(signum, frame):
    """Handle termination signals"""
    cleanup_processes()
    exit(0)

# Register signal handlers
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

try:
    make_directories([file_name,failed_file_name,logs_folder_path+"/screenshots",default_resume_path,generated_resume_path+"/temp"])

    # Set up WebDriver with Chrome Profile
    options = uc.ChromeOptions() if stealth_mode else Options()
    if run_in_background:   options.add_argument("--headless")
    if disable_extensions:  options.add_argument("--disable-extensions")

    print_lg("IF YOU HAVE MORE THAN 10 TABS OPENED, PLEASE CLOSE OR BOOKMARK THEM! Or it's highly likely that application will just open browser and not do anything!")
    
    # Try to connect to existing Chrome instance first
    print_lg("Attempting to connect to existing Chrome browser...")
    
    # Add options to connect to existing Chrome
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    
    try:
        if stealth_mode:
            driver = uc.Chrome(options=options)
        else:
            driver = webdriver.Chrome(options=options)
        print_lg("Successfully connected to existing Chrome browser!")
    except Exception as e:
        print_lg("Could not connect to existing Chrome. Opening new Chrome instance...")
        print_lg("To use existing Chrome, please start Chrome with: --remote-debugging-port=9222")
        
        # Remove the debugger address option and try normal connection
        options = uc.ChromeOptions() if stealth_mode else Options()
        if run_in_background:   options.add_argument("--headless")
        if disable_extensions:  options.add_argument("--disable-extensions")
        
        if safe_mode: 
            print_lg("SAFE MODE: Will login with a guest profile, browsing history will not be saved in the browser!")
        else:
            profile_dir = find_default_profile_directory()
            if profile_dir: 
                options.add_argument(f"--user-data-dir={profile_dir}")
                print_lg(f"Using Chrome profile directory: {profile_dir}")
            else: 
                print_lg("Default profile directory not found. Logging in with a guest profile, Web history will not be saved!")
        
        # Add options to ensure process termination
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_experimental_option("detach", False)
        
        if stealth_mode:
            print_lg("Downloading Chrome Driver... This may take some time. Undetected mode requires download every run!")
            driver = uc.Chrome(options=options)
        else: 
            driver = webdriver.Chrome(options=options)
    
    driver.maximize_window()
    wait = WebDriverWait(driver, 5)
    actions = ActionChains(driver)
    
    # Set up process monitoring
    def on_driver_quit():
        cleanup_processes()
    
    # Override the quit method to ensure cleanup
    original_quit = driver.quit
    def quit_with_cleanup():
        cleanup_processes()
        original_quit()
    
    driver.quit = quit_with_cleanup
    
except Exception as e:
    msg = 'Seems like either... \n\n1. Chrome is already running. \nA. Close all Chrome windows and try again. \n\n2. Google Chrome or Chromedriver is out dated. \nA. Update browser and Chromedriver (You can run "windows-setup.bat" in /setup folder for Windows PC to update Chromedriver)! \n\n3. If error occurred when using "stealth_mode", try reinstalling undetected-chromedriver. \nA. Open a terminal and use commands "pip uninstall undetected-chromedriver" and "pip install undetected-chromedriver". \n\n\nIf issue persists, try Safe Mode. Set, safe_mode = True in config.py \n\nPlease check GitHub discussions/support for solutions https://github.com/ \n                                   OR \nReach out in discord ( https://discord.gg/fFp7uUzWCY )'
    if isinstance(e,TimeoutError): msg = "Couldn't download Chrome-driver. Set stealth_mode = False in config!"
    print_lg(msg)
    critical_error_log("In Opening Chrome", e)
    from pyautogui import alert
    alert(msg, "Error in opening chrome")
    try: driver.quit()
    except NameError: exit()
    
