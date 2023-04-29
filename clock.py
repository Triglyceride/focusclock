import time

def concentration_timer(minutes):
    """A concentration timer that runs for the specified number of minutes"""

    # Convert the minutes to seconds
    seconds = minutes * 60

    # Display a message to the user
    print("The concentration timer has started for {} minutes!".format(minutes))

    # Start the countdown loop
    while seconds > 0:
        # Display the remaining time to the user
        print("Remaining time: {} seconds".format(seconds))

        # Sleep for one second
        time.sleep(1)

        # Decrement the remaining time
        seconds -= 1

    # Display the completion message
    print("Congratulations! You have completed the concentration timer for {} minutes!".format(minutes))

# Run the concentration timer for 25 minutes
concentration_timer(25)
