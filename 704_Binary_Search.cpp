class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = nums[0];
        int right = nums.back();
        if (target < left || target > right) {
            return -1;
        }
        int leftidx = 0;
        int rightidx = nums.size()-1;
        // cout << left << "\n";
        // cout << leftidx << "\n";
        // cout << right << "\n";
        // cout << rightidx << "\n";
        cout << leftidx << "," << rightidx << "\n";
        if (left == target) {
            return leftidx;
        }
        else if (right == target) {
            return rightidx;
        }
        else {
            int mididx = (leftidx + rightidx) / 2;
            int mid = nums[mididx];
            // cout << mid << "\n";
            // cout << mididx << "\n";
            cout << leftidx << "," << mididx << "," << rightidx << "\n";
            while (leftidx < rightidx) {
                if (leftidx == rightidx-1) {
                    if (target == nums[rightidx]) {
                        return rightidx;
                    }
                    else {
                        return -1;
                    }
                }
                if (target == mid) {
                    return mididx;
                }
                else if (target < mid) {
                    right = mid;
                    rightidx = mididx;
                }
                else {//(target > mid)
                    left = mid;
                    leftidx = mididx;
                }
                if (mididx == 0 || mididx == nums.size()-1) {
                    break;
                }
                cout << leftidx << "," << mididx << "," << rightidx << "\n";
                mididx = (leftidx + rightidx) / 2;
                mid = nums[mididx];
            }
        }
        return -1;
    }
};
