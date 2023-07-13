import psutil
import time

# Collect network traffic statistics
def get_network_stats():
    network_stats = psutil.net_io_counters(pernic=True)
    return network_stats

# Continuously collect network stats
while True:
    stats = get_network_stats()
    # Store stats data or send to a backend server for visualization
    time.sleep(5)

