import java.util.HashMap;

class RomanToInt{
    public int solution(String s){
        int num = 0;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);

        int len = s.length();
        for (int i = 0; i < len; i++){
            if (i + 1 < len && map.get(s.charAt(i)) < map.get(s.charAt(i+1))){
                num -= map.get(s.charAt(i));
            }else {
                num += map.get(s.charAt(i));
            }
        }
        return num;
    }
}