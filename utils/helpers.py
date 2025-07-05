import os
from datetime import datetime

def take_screenshot(driver, filename):
    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join("screenshots", f"{timestamp}_{filename}")
    driver.save_screenshot(filepath)
    return filepath
