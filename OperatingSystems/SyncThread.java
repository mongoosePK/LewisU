// SyncThread.java -- assignment 2 for OS35000
//By: William Pulkownik
// It passes some thread synchronization locks around
import java.util.concurrent.*;

class Producer implements Runnable {
	int[] xCount;
	Semaphore lock, lock2;
	public Producer(int[] x, Semaphore lock, Semaphore lock2) {
		this.lock = lock;
        this.lock2 = lock2;
		this.xCount = x;
	}
	public void run() {
		while(true){
			try{
				lock.acquire();
				xCount[0]++;
				Thread.sleep(300);
			} catch (InterruptedException ie) {}
			lock2.release();
		}
	}
}	

class Consumer implements Runnable {
	Semaphore lock, lock2;
	int[] xPrint;
	public Consumer(int[] x, Semaphore lock, Semaphore lock2) {
		this.lock = lock;
        this.lock2 = lock2;
		this.xPrint = x;
	}

	public void run() {
		while(true) {
			try {
				lock2.acquire();
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
		
		Semaphore lock = new Semaphore(0, true);
		Semaphore lock2 = new Semaphore(1, true);

		Thread threadWriter = new Thread(new Consumer(shared_object, lock, lock2));
		Thread threadEater = new Thread(new Producer(shared_object, lock, lock2));
		Thread threadWriter2 = new Thread(new Consumer(shared_object, lock, lock2));
		Thread threadEater2 = new Thread(new Producer(shared_object, lock, lock2));

		threadEater.start();
		threadWriter.start();
		
		threadEater2.start();
		threadWriter2.start();

		try {
			threadWriter.join();
			threadEater.join();

			threadEater2.join();
			threadWriter2.join();

		} catch (InterruptedException ie) {}
	}
}
