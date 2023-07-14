"""
You are given an array A of length N and Q queries given by the 2D array B of size Q×2.
Each query consists of two integers B[i][0] and B[i][1].
For every query, your task is to find the count of even numbers in the range from A[B[i][0]] to A[B[i][1]].
"""
class Solution:
    @staticmethod
    def prefix(array):
        psum=[0]*len(array)
        if array[0]%2==0:
            psum[0]=1
        for i in range(1,len(array)):
            psum[i]=psum[i-1]+ (1 if array[i]%2==0 else 0)
        return psum
    def even_numbers(self,psum,l,r):
        if l==0:
            return psum[r]
        return psum[r]-psum[l-1]

if __name__ == '__main__':
    ob = Solution()
    array=list(map(int,input().split()))
    q=int(input())
    queries=[]
    for i in range(q):
        l,r=map(int,input().split())
        queries.append([l,r])
    #find prefix sum first
    psum=ob.prefix(array)
    for i in range(q):
        l,r=queries[i]
        print(ob.even_numbers(psum,l,r),end=" ")
