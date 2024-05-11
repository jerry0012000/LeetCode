class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length == 0 || prices.length == 1) {
            return 0;
        }
        else {
            int max = 0;
            int left = 0;
            for (int right = 0;right < prices.length;right++) {
                int diff = prices[right] - prices[left];
                if (prices[left] > prices[right]) {
                    left = right;
                }
                else {
                    if (diff > max) {
                        max = diff;
                    }
                }
            }
            return max;
        }
    }
}
//这样也会超时
// class Solution {
//     public int maxProfit(int[] prices) {
//         if (prices.length == 0 || prices.length == 1) {
//             return 0;
//         }
//         else {
//             int minPrice = 10000;
//             int profit = 0;
//             for (int i=0; i<prices.length-1;i++) {
//                 if (prices[i] < minPrice) {
//                     minPrice = prices[i];
//                 }
//                 for (int j=i+1; j<prices.length;j++) {
//                     int maxPrice = 0;
//                     if (prices[j] > maxPrice) {
//                         maxPrice = prices[j];
//                         profit = Math.max(maxPrice-minPrice,profit);
//                     }
//                 }
//             }
//             return profit;
//         }
//     }
// }
//这样会超时
// class Solution {
//     public int maxProfit(int[] prices) {
//         if (prices.length == 0 || prices.length == 1) {
//             return 0;
//         }
//         else {
//             int minPrice = prices[0];
//             int profit = 0;
//             for (int i=0; i<prices.length;i++) {
//                 for (int j=i+1; j<prices.length;j++) {
//                     if ((prices[j] - prices[i]) > profit) {
//                         profit = prices[j] - prices[i];
//                     }
//                 }
//             }
            
//             return profit;
//         }
//     }
// }
