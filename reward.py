import math

def calculate_midpoint(point1: list[float], point2: list[float]) -> list[float]:
    return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]

def calculate_length(point1: list[float], point2: list[float]) -> float:
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_heading(current_point: list[float], target_point: list[float]) -> float:
    """
    Heading is calculated with respect to the x-axis.
    In simple terms, when heading along the x-axis, the angle is 0 degrees.
    And the angle increases as you rotate counter-clockwise.
    """

    # Third point necessary to form a triangle in order to calculate the angle
    reference_point = [current_point[0] + 1, current_point[1]]

    a = calculate_length(reference_point, target_point)
    b = calculate_length(reference_point, current_point)
    c = calculate_length(current_point, target_point)
    
    # Cosine rule to find an angle
    angle = math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))

    # Upside-down triangle
    if (target_point[1] < current_point[1]):
        return 360 - angle
    
    return angle

def reward_function(params):
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    current_point = [params['x'], params['y']]
    current_heading = params['heading']

    # Attempting to cut corners by calculating the midpoint between the next waypoint and 3 points ahead
    target_point = calculate_midpoint(waypoints[closest_waypoints[1]], waypoints[(closest_waypoints[1] + 3) % len(waypoints)])
    
    # Calculate the heading from the current position to the above calculated target
    target_heading = calculate_heading(current_point, target_point)
    
    # "Normalise" the heading to be between 0 and 360 degrees
    if (current_heading < 0):
        current_heading = 360 + current_heading
    
    # Reward based on how close the heading is to the expected target heading
    heading_diff = abs(target_heading - current_heading)
    # Handle cases where degrees wrap around (e.g. the target heading is 359 degrees and the current heading is 2 degrees)
    heading_diff = min(heading_diff, 360 - heading_diff)
    # Perhaps, the reward should degrade exponentially to help with precision
    return (360 - heading_diff) / 360
