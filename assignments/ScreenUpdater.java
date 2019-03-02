import java.util.concurrent.*;

public class ScreenUpdater implements Runnable {
	public void run() {
		for (;;) {
			try {
				Thread.currentThread().sleep(1000 * 6);
			} catch (InterruptedException ie) {}

			System.out.println(Thread.currentThread().getName() + ": updating screen");
		}
	}
}
