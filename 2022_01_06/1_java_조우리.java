class Solution {
    public int solution(int[] nums) {
		int sum;
		int cnt = 0;
		for(int i=0; i<nums.length; i++) {
			int num1 = nums[i];
			sum = 0;
			for(int j=i+1; j<nums.length; j++) {
				int num2 = nums[j];
				for(int k=j+1; k<nums.length; k++) {
					int num3 = nums[k];
					sum = num1 + num2 + num3;
					if(checkNum(sum) == false)	cnt++;
				}
			}
		}
		
		return cnt;
	}
	
	static boolean checkNum(int sum) {
		boolean check = false;
		for(int i=2; i<sum; i++) {
			if(sum%i == 0) {
				check = true;
				break;
			}
		}
		
		return check;
	}
}