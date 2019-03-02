import java.util.Scanner;
import java.util.concurrent.*;

//define the class
public class DoubleHandler implements Runnable {
	public void run(){
		double num2;
		Scanner d = new Scanner(System.in);
		
		while(true) {
			//this section gets the double input and prints
			System.out.println(Thread.currentThread().getName() + ": or enter a double:");
			num2 = d.nextDouble();
			System.out.println(Thread.currentThread().getName() + ": " + num2); 
		}
	}
	
}
