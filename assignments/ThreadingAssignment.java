import java.util.concurrent.*;

public class ThreadingAssignment {
	public static void main(String[] args) {
		System.out.println("I am thread: " + Thread.currentThread().getName());

		Thread screenUpdater = new Thread(new ScreenUpdater());
		Thread intHandler = new Thread(new IntHandler());
		Thread doubleHandler = new Thread(new DoubleHandler());
		try {
			intHandler.start();
			doubleHandler.start();
			screenUpdater.start();
			
			intHandler.join();
			doubleHandler.join();
			screenUpdater.join();
		} catch (InterruptedException ie) {}
	}
}
