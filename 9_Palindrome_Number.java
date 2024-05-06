class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int num = x;
        int digitCount = 0;
        List<Integer> list = new ArrayList<>();
        List<Integer> reverseList = new ArrayList<>();
        while (num != 0) {
            reverseList.add(num % 10);
            num /= 10;
            digitCount++;
        }
        for (int i = digitCount; i > 0; i--) {
            System.out.println(i);
            System.out.println((int) Math.floor(x / (Math.pow(10,i-1))) % 10);
            list.add((int) Math.floor(x / (Math.pow(10,i-1))) % 10);
        }
        if (list.equals(reverseList)) {
            return true;
        }
        else {
            System.out.println(list);
            System.out.println(reverseList);
            return false;
        }
    }
}
