# Not acccepted.
def topKFrequent(nums, k):
        most = {}
        for i in nums:
            if i <= 0:
                break
            if i in most:
                most[i] += 1
            else:
                most[i] = 1
        
        m_frequent = sorted(most.items(), key=lambda x:x[1])

        result = []
        if len(m_frequent) < 0 :
            return [-1]
        for j in range(k):
            result.append(m_frequent[j][1])

        return result
        

if __name__ == "__main__" :
    # test = Solution()
    # print(topKFrequent([1,1,1,2,2,3], 2))
    print(topKFrequent([-1,-1], 1))