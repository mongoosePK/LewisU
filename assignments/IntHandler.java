import java.util.Scanner;
import java.util.concurrent.*;


public class IntHandler implements Runnable {
	public void run(){
		int num;
		Scanner i = new Scanner(System.in);

		while (true) {
			//this section gets Integer input with scanner
			System.out.println(Thread.currentThread().getName() + ": enter an integer: ");
			num = i.nextInt();			
			System.out.println(Thread.currentThread().getName() + ": " + num);
			
		}
	}
}
