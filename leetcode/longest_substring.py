class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_arr = list(s)
        set_list = set(temp_arr)
        result_arr = list()

        if len(set_list) is 0:
            return 0
        if len(set_list) is 1:
            return 1
        for i in range(len(temp_arr)):
            sub = []
            for j in range(i, len(temp_arr)):
                if temp_arr[j] in sub:
                    substring = ''.join(sub)
                    result_arr.append(len(substring))
                    break
                sub.append(temp_arr[j])

                if j == len(temp_arr) - 1:
                    substring = ''.join(sub)
                    result_arr.append(len(substring))
        answer = max(result_arr)
        return answer


