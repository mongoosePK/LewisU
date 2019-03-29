<<<<<<< HEAD
import java.util.concurrent.*;
import java.util.Scanner;

class Producer implements Runnable {
	//Object sync; --remove original thread lock (replaced /w semaphore)
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
				//try {
					Thread.sleep(300);
				//} catch (InterruptedException ie){}
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
		
		Semaphore lock = new Semaphore(1, true);
		Semaphore lock2 = new Semaphore(0, true);

		Thread threadAfter = new Thread(new Consumer(shared_object, lock, lock2));
		Thread threadBefore = new Thread(new Producer(shared_object, lock, lock2));
		
		threadBefore.start();
		threadAfter.start();
		
		try {
			threadAfter.join();
			threadBefore.start();
		} catch (InterruptedException ie) {}
	}
}
=======
import java.util.concurrent.*;
import java.util.Scanner;

class Producer implements Runnable {
	//Object sync; --remove original thread lock (replaced /w semaphore)
	int[] xCount;
	Semaphore lock;
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
	Semaphore lock;
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
		//Integer sync_object = 0; ---remove original lock (replaced by semaphore)
		Semaphore lock = new Semaphore(1, true); //create semaphore /w 1 lock
		
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
>>>>>>> efa3af75da46cf4ec4cb16d96b311a519bdf1810
