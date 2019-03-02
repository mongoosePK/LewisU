import java.util.Scanner;
import java.util.concurrent.*;
import java.util.InputMismatchException;


public class IntHandler implements Runnable {
	public void run(){
		Scanner i = new Scanner(System.in);

		while (true) {
			try{
				//this section gets Integer input with scanner
				System.out.println(Thread.currentThread().getName() + ": enter an integer: ");
				int num = i.nextInt();			
				System.out.println(Thread.currentThread().getName() + ": " + num);
			}catch (InputMismatchException e) {
				i.nextLine();
			}
		}
	}
}
