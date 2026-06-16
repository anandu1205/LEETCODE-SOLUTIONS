import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda course: course[1])

        total_time = 0
        taken_courses = []

        for duration, last_day in courses:
            total_time += duration
            heapq.heappush(taken_courses, -duration)

            if total_time > last_day:
                longest_duration = -heapq.heappop(taken_courses)
                total_time -= longest_duration

        return len(taken_courses)


        