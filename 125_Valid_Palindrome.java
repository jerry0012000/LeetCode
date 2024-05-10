class Solution {
    public boolean isPalindrome(String s) {
        String result = "";
        for (int i=0;i<s.length();i++) {
            char ch = s.charAt(i);
            if (Character.isLetterOrDigit(ch)) {
                result += ch;
            }
        }
        char[] chars =result.toCharArray();
        String compare = "";
        for (int j=result.length()-1; j>=0;j--) {
            compare += chars[j];
        }
        result = result.toLowerCase();
        compare = compare.toLowerCase();
        System.out.println("result: " + result);
        System.out.println("compare: " + compare);
        if (result.equals(compare)) {
            return true;
        }
        else {
            return false;
        }
    }
}
