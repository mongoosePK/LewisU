//William Pulkownik
//Assignment 1
//Operating Systems
//screenUpdater.java

import java.util.concurrent.*;

public class ScreenUpdater implements Runnable {
	public void run() {
		for (;;) {
			try {
				Thread.currentThread().sleep(1000 * 60);
			} catch (InterruptedException ie) {}

			System.out.println("updating screen");
		}
	}
}
