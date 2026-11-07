class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = []

        time = 0

        for j, task in enumerate(tasks):
            time = max(time, j)

            # Release servers that have completed their tasks
            while busy and busy[0][0] <= time:
                free_time, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            # If no server is free, move time forward
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    free_time, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            # Assign task to the best available server
            weight, index = heapq.heappop(available)

            ans.append(index)

            # Update server's next available time
            heapq.heappush(busy, (time + task, weight, index))

        return ans
