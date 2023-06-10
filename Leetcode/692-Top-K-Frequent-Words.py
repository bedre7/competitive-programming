class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordFreq = defaultdict(int)
        for word in words:
            wordFreq[word] += 1
        
        freqs = defaultdict(list)
        for word, freq in wordFreq.items():
            freqs[freq].append(word)
        
        topk = []
        maxHeap = list(set([-freq for freq in wordFreq.values()]))
        heapq.heapify(maxHeap)
        print(maxHeap)
        for _ in range(k):
            if len(topk) == k: break
            currFreq = -heapq.heappop(maxHeap)
            for word in sorted(freqs[currFreq]):
                if len(topk) == k: break
                topk.append(word)
        
        return topk