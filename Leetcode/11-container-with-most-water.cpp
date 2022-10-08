class Solution {
    public:
        int maxArea(vector<int>& height) {
            int max_area = INT32_MIN;
            int width;
            for (int left = 0, right = height.size() - 1; left < right;)
            {
                width = right - left;
                max_area = max(max_area, min(height[left], height[right]) * width);
                
                height[left] <= height[right] ? left++ : right--;
            }
            return max_area;   
        }
    };