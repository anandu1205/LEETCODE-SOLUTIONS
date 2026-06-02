class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        times = []

        # Land -> Water
        for i in range(len(landStartTime)):
            land_finish = landStartTime[i] + landDuration[i]

            for j in range(len(waterStartTime)):
                finish = max(land_finish, waterStartTime[j]) + waterDuration[j]
                times.append(finish)

        # Water -> Land
        for i in range(len(waterStartTime)):
            water_finish = waterStartTime[i] + waterDuration[i]

            for j in range(len(landStartTime)):
                finish = max(water_finish, landStartTime[j]) + landDuration[j]
                times.append(finish)

        return min(times)