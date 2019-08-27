//Bobby Reich
import java.util.concurrent.Semaphore;

class Consumer implements Runnable {
    int x[];
    Semaphore s;
    Semaphore s1;
    public Consumer(int [] xIn, Integer synchIn, Semaphore sIn, Semaphore s1In) {
        x = xIn;
        s = sIn;
        s1 = s1In;
    }
    public void run() {
        while (true) {
            try {
                s.acquire();
                System.out.println(x[0]);    
            } catch (InterruptedException ie) {}
            s1.release();
        } 
    }   
}
class Producer implements Runnable {
    int x[];
    Semaphore s;
    Semaphore s1;
    public Producer(int [] xIn, Integer synchIn, Semaphore sIn, Semaphore s1In) {
        x = xIn;
        s = sIn;
        s1 = s1In;
    }
    public void run() {
        while (true) {
            try {
                s1.acquire();
                synchronized(synch) {
                    x[0]++;
                }
            } catch (InterruptedException ie) {}
            try {
                Thread.sleep(300);
            } catch (InterruptedException ie) {}
            s.release();
        }
    }
}
public class synchOs {
    public static void main(String[] args) {
        int x[] = new int[1];
        x[0] = 0;
        Semaphore s = new Semaphore(1, true);
        Semaphore s1 = new Semaphore(0, true);

        Thread myProducer = new Thread(new Producer(x, s, s1));
        Thread myConsumer = new Thread(new Consumer(x, s, s1));

        Thread myProducerTwo = new Thread(new Producer(x, s, s1));
        Thread myConsumerTwo = new Thread(new Consumer(x, s, s1));

        Thread myProducerThree = new Thread(new Producer(x, s, s1));
        Thread myConsumerThree = new Thread(new Consumer(x, s, s1));

        myProducer.start();
        myConsumer.start();

        myProducerTwo.start();
        myConsumerTwo.start();

        myProducerThree.start();
        myConsumerThree.start();
        try {
            myProducer.join();
            myConsumer.join();

            myProducerTwo.join();
            myConsumerTwo.join();

            myProducerThree.join();
            myConsumerThree.join();
        } catch (InterruptedException ie) {}
    }
}