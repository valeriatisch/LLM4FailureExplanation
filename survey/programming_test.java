public class FindTop {
 
  	private int[] numbers;

  	public FindTop(int[] numbersArg){
       	this.numbers = numbersArg;
  	}
 
  	public int findHighest(int lowIndex, int highIndex){
       	int top = this.numbers[lowIndex];
       	for(int i = lowIndex; i <= highIndex; i++){
             	if (top < this.numbers[i])
                   	top = this.numbers[i];
       	}
       	return top;
  	}
 
  	public static void main(String[] args) {
       	int myNumbers[] = {10, 5, 2, 4, 8};
       	FindTop numbers = new FindTop(myNumbers);
       	System.out.println( numbers.findHighest(1, 4));
  	}
}


