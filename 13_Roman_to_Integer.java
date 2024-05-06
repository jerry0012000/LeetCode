class Solution {
    public int romanToInt(String s) {
        int result = 0;
        String tempStr = s;
        if (s.contains("IV")) {
            result += 4;
            tempStr = tempStr.replace("IV","");
        }
        if (s.contains("IX")) {
            result += 9;
            tempStr = tempStr.replace("IX","");
        }
        if (s.contains("XL")) {
            result += 40;
            tempStr = tempStr.replace("XL","");
        }
        if (s.contains("XC")) {
            result += 90;
            tempStr = tempStr.replace("XC","");
        }
        if (s.contains("CD")) {
            result += 400;
            tempStr = tempStr.replace("CD","");
        }
        if (s.contains("CM")) {
            result += 900;
            tempStr = tempStr.replace("CM","");
        }
        int[] symbolList = {0,0,0,0,0,0,0};
        String[] list = {"I","V","X","L","C","D","M"};
        // System.out.println(list.length);
        for (int i = 0; i < list.length; i++) {
            int originalLength = tempStr.length();
            System.out.println(originalLength);
            String element = list[i];
            System.out.println("element: " + element);
            //这里忘了tempStr =,导致根本没替换
            tempStr = tempStr.replace(element, "");
            System.out.println(tempStr);
            symbolList[i] += originalLength - tempStr.length();
            // System.out.println(element);
        }
        result += symbolList[0];
        result += 5*symbolList[1];
        result += 10*symbolList[2];
        result += 50*symbolList[3];
        result += 100*symbolList[4];
        result += 500*symbolList[5];
        result += 1000*symbolList[6];
        return result;
    }
}
