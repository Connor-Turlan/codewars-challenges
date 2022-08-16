public class Greed{
	public static int greedy(int[] dice){
	  int[] counts = {0, 0, 0, 0, 0, 0};
	  int score = 0;
  
	  // count all the rolls.
	  for (int roll : dice) { counts[roll-1]++; }
  
	  // determine the scores.
	  int n = 1;
	  for (int count : counts) {
		  // check for 3 of n.
		  if (count >= 3) {
			  score += n == 1 ? 1000 : n * 100;
			  count -= 3;
		  }
  
		  // check for any additional count.
		  if (n == 1) { score += 100 * count; }
		  if (n == 5) { score += 50 * count; }
  
		  n++;
	  }
  
	  return score;
	}
}