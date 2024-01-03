class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        sort_tasks=sorted(tasks)
        maximum=0
        j=3
        for i in sorted(processorTime,reverse=True):
            if j!=len(tasks):
                if maximum < i + sort_tasks[j]:
                    maximum = i + sort_tasks[j]
            j+=4
        return maximum
        
        