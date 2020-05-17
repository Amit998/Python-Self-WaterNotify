import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title="Please Drink Water",
        message="Water do eyes, nose, or mouth gets dry? Keeping your body hydrated helps it retain optimum levels of moisture in these sensitive areas, as well as in the blood, bones, an.",
        # app_icon="glass-512.jpg",
        timeout=5
    )
    time.sleep(10)