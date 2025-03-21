//java code for thread creation by extending thread class
class MultithreadingDemo extends Thread {
    public void run()
    {
        try{
            //displaying the thread that is running
            System.out.println(
                "Thread " + Thread.currentThread().getId()
                + "is running");
        }
        catch (Exception e) {
            //throwing an exception
            System.out.println("Exception is caught");
        }
        
    }
}

//Main class
public class Multithread {
    public static void main (String[]args)
    {
        int n=8; //Number of threads
        for (int i=0;i<n;i++) {
            MultithreadingDemo object
                =new MultithreadingDemo ();
            object.start();
        }
    }
}