class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.tW =defaultdict()
        self.times = times                
        vote_count = defaultdict(int)
        cur_max, cur_win = 0, -1
        for p, t in zip(persons, times):
            vote_count[p] += 1
            if vote_count[p] >= cur_max: 
                cur_max, cur_win = vote_count[p], p
            self.tW[t] = cur_win
            
        
        

    def q(self, t: int) -> int:
        return self.tW[self.times[bisect_right(self.times, t)-1]]