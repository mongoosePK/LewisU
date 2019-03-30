import java.util.concurrent.*;
import java.util.Scanner;

class Producer implements Runnable {
	//Object sync; --remove original thread lock (replaced /w semaphore)
	int[] xCount;
	Semaphore lock,;
	public Producer(int[] x, Semaphore lock) {
		this.lock = lock;
		this.xCount = x;
	}
	public void run() {
		while(true){
			try{
				lock.acquire();
				xCount[0]++;
				//try {
					Thread.sleep(300);
				//} catch (InterruptedException ie){}
			} catch (InterruptedException ie) {}
			lock.release();
		}
	}
}	

class Consumer implements Runnable {
	Semaphore lock,;
	int[] xPrint;
	public Consumer(int[] x, Semaphore lock) {
		this.lock = lock;
		this.xPrint = x;
	}

	public void run() {
		while(true) {
			try {
				lock.acquire();
				System.out.println(xPrint[0]);
			} catch (InterruptedException ie){}
			lock.release();
		}
	}
}
public class SyncThread {
	public static void main(String[] args) {
		int shared_object[] = new int[1];
		shared_object[0] = 0;
		
		Semaphore lock = new Semaphore(1);

		Thread threadAfter = new Thread(new Consumer(shared_object, lock));
		Thread threadBefore = new Thread(new Producer(shared_object, lock));
		
		threadBefore.start();
		threadAfter.start();
		
		try {
			threadAfter.join();
			threadBefore.start();
		} catch (InterruptedException ie) {}
	}
}