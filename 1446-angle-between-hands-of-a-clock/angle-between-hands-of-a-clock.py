class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_hand = (minutes / 60) * 360

        hour_position = (hour % 12) * (360 / 12)
        minute_movement = (minutes / 60) * (360 / 12)

        hour_hand = hour_position + minute_movement

        angle = abs(hour_hand - minute_hand)

        return min(angle, 360 - angle)
        