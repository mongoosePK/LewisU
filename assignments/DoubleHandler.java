import java.util.Scanner;
import java.util.concurrent.*;
import java.util.InputMismatchException;
//define the class
public class DoubleHandler implements Runnable {
	public void run(){
		Scanner d = new Scanner(System.in);
		
		while(true) {
			try{
			//this section gets the double input and prints
			System.out.println(Thread.currentThread().getName() + ": or enter a double:");
			double num2 = d.nextDouble();
			System.out.println(Thread.currentThread().getName() + ": " + num2); 
		}catch (InputMismatchException e) {
				d.nextLine();
			}
		}
	}
	
}
