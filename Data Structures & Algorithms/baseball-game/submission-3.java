class Solution {
    public int calPoints(String[] operations) {
        List<Integer> scores = new ArrayList<>();
        int score = 0;
        for (String op : operations) {
            if (op.equals("+")) {
                Integer val = scores.get(scores.size()-1) + scores.get(scores.size()-2);
                score += val;
                scores.add(val);
            } else if (op.equals("D")) {
                Integer val = scores.get(scores.size()-1)*2;
                score += val;
                scores.add(val);
            } else if (op.equals("C")) {
                Integer val = scores.get(scores.size()-1);
                score -= val;
                scores.remove(scores.size()-1);
            } else {
                Integer val = Integer.valueOf(op);
                score += val;
                scores.add(val);
            }
        }
        return score;
    }
}