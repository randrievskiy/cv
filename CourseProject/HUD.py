import cv2


def draw_battery_icon(frame, battery_level, position, size=(50, 20), color=(255, 0, 255), thickness=2):
    # Calculate the battery outline rectangle
    top_left = position
    bottom_right = (position[0] + size[0], position[1] + size[1])

    # Draw battery outline
    cv2.rectangle(frame, top_left, bottom_right, color, thickness)

    # Draw battery level
    level_width = int(size[0] * (battery_level / 100.0))
    level_bottom_right = (top_left[0] + level_width, bottom_right[1])
    cv2.rectangle(frame, top_left, level_bottom_right, color, -1)

    # Draw the battery's positive terminal
    terminal_top_left = (bottom_right[0], position[1] + size[1] // 4)
    terminal_bottom_right = (bottom_right[0] + 5, position[1] + 3 * size[1] // 4)
    cv2.rectangle(frame, terminal_top_left, terminal_bottom_right, color, thickness)


def draw_battery_percentage(frame, battery_level, frame_width):
    cv2.putText(frame, str(battery_level) + "%", (frame_width - 50, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255),2)
