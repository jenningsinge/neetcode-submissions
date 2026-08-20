class Solution {
    public boolean isValid(String s) {
        List<Character> parens = new ArrayList<>();

        char[] chars = s.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == '(' || chars[i] == '{' || chars[i] == '[') {
                parens.add(chars[i]);
            } else if (parens.size() > 0) {
                if (matchingParens(parens.get(parens.size()-1), chars[i])) {
                    parens.remove(parens.size()-1);
                } else return false;
            } else return false;
        }
        return parens.size() == 0;
    }

    public boolean matchingParens(Character open, Character close) {
        System.out.println(open.toString() + close);
        if (open == '(' && close == ')') return true;
        if (open == '{' && close == '}') return true;
        if (open == '[' && close == ']') return true;
        return false;
    }
}
