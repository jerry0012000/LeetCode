class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        if (text1.contains(text2)) {
            return text2.length();
        }
        else if (text2.contains(text1)) {
            return text1.length();
        }
        else {
            int longestLength = 0;
            int maxIndex = 0;
            if (text1.length() > text2.length()) {  
                boolean[] exist = new boolean[text2.length()];
                for (int i=0;i<text2.length();i++) { 
                    // if (i > 0 && exist[i-1] == false) {
                    //     maxIndex = 0;
                    //     if (longestLength < calculateTrues(exist)) {
                    //         longestLength = calculateTrues(exist);
                    //     }
                    //     for (int l=0;l<exist.length;l++) {
                    //     // 重置列表
                    //         exist[l] = false;
                    //     }
                    // }  
                    for (int j=maxIndex;j<text1.length();j++) {
                        if (text2.charAt(i) == text1.charAt(j)) {
                            maxIndex = j+1;
                            exist[i] = true;
                            break;
                        }
                    }
                    // if (i > 0 && exist[i-1] == true && exist[i] == false) {
                    //     for (int l=0;l<exist.length;l++) {
                    //         // 重置列表
                    //         exist[l] = false;
                    //     }
                    //     for (int j=0;j<text1.length();j++) {
                    //         //看看这一位是不是起始位
                    //         if (text2.charAt(i) == text1.charAt(j)) {
                    //             maxIndex = j;
                    //             exist[i] = true;
                    //         }
                    //     }
                    // } 
                    System.out.println(text1.charAt(i));
                    System.out.println(exist[i]);
                    System.out.println(Arrays.toString(exist));
                    if (longestLength < calculateTrues(exist)) {
                        longestLength = calculateTrues(exist);
                    }
                }
                for (int i=0;i<text2.length();i++) { 
                    if (i > 0 && exist[i-1] == false) {
                        maxIndex = 0;
                        if (longestLength < calculateTrues(exist)) {
                            longestLength = calculateTrues(exist);
                        }
                        for (int l=0;l<exist.length;l++) {
                        // 重置列表
                            exist[l] = false;
                        }
                    }  
                    for (int j=maxIndex;j<text1.length();j++) {
                        if (text2.charAt(i) == text1.charAt(j)) {
                            maxIndex = j+1;
                            exist[i] = true;
                        }
                    }
                    if (i > 0 && exist[i-1] == true && exist[i] == false) {
                        for (int l=0;l<exist.length;l++) {
                            // 重置列表
                            exist[l] = false;
                        }
                        for (int j=0;j<text1.length();j++) {
                            //看看这一位是不是起始位
                            if (text2.charAt(i) == text1.charAt(j)) {
                                maxIndex = j+1;
                                exist[i] = true;
                                break;
                            }
                        }
                    } 
                    System.out.println(text1.charAt(i));
                    System.out.println(exist[i]);
                    System.out.println(Arrays.toString(exist));
                    if (longestLength < calculateTrues(exist)) {
                        longestLength = calculateTrues(exist);
                    }
                }     
                return longestLength;
            }
            else if (text1.length() <= text2.length()) {
                boolean[] exist = new boolean[text1.length()];
                for (int i=0;i<text1.length();i++) {
                    // if (i > 0 && exist[i-1] == false) {
                    //     maxIndex = 0;
                    //     if (longestLength < calculateTrues(exist)) {
                    //         longestLength = calculateTrues(exist);
                    //     }
                    //     for (int l=0;l<exist.length;l++) {
                    //         // 重置列表
                    //         exist[l] = false;
                    //     }
                    // } 
                    for (int j=maxIndex;j<text2.length();j++) {
                        if (text1.charAt(i) == text2.charAt(j)) {
                            maxIndex = j+1;
                            exist[i] = true;
                            break;
                        }
                    }
                    // if (i > 0 && exist[i-1] == true && exist[i] == false) {
                    //     for (int l=0;l<exist.length;l++) {
                    //         // 重置列表
                    //         exist[l] = false;
                    //     }
                    //     for (int j=0;j<text2.length();j++) {
                    //         //看看这一位是不是起始位
                    //         if (text1.charAt(i) == text2.charAt(j)) {
                    //             maxIndex = j;
                    //             exist[i] = true;
                    //         }
                    //     }
                    // } 
                    System.out.println(text1.charAt(i));
                    System.out.println(exist[i]);
                    System.out.println(Arrays.toString(exist));
                    if (longestLength < calculateTrues(exist)) {
                        longestLength = calculateTrues(exist);
                    }
                }
                for (int i=0;i<text1.length();i++) {
                    if (i > 0 && exist[i-1] == false) {
                        maxIndex = 0;
                        if (longestLength < calculateTrues(exist)) {
                            longestLength = calculateTrues(exist);
                        }
                        for (int l=0;l<exist.length;l++) {
                            // 重置列表
                            exist[l] = false;
                        }
                    } 
                    for (int j=maxIndex;j<text2.length();j++) {
                        if (text1.charAt(i) == text2.charAt(j)) {
                            maxIndex = j+1;
                            exist[i] = true;
                            break;
                        }
                    }
                    if (i > 0 && exist[i-1] == true && exist[i] == false) {
                        for (int l=0;l<exist.length;l++) {
                            // 重置列表
                            exist[l] = false;
                        }
                        for (int j=0;j<text2.length();j++) {
                            //看看这一位是不是起始位
                            if (text1.charAt(i) == text2.charAt(j)) {
                                maxIndex = j+1;
                                exist[i] = true;
                                break;
                            }
                        }
                    } 
                    System.out.println(text1.charAt(i));
                    System.out.println(exist[i]);
                    System.out.println(Arrays.toString(exist));
                    if (longestLength < calculateTrues(exist)) {
                        longestLength = calculateTrues(exist);
                    }
                }
                return longestLength;
            }
        return 0;
        }
    }
    public int calculateTrues(boolean[] a) {
        int trues = 0;
        for (int k=0;k<a.length;k++) {
            if (a[k]) {
                trues += 1;
            }
        }
        return trues;
    }
}
