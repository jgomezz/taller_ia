package pe.edu.jgm._java._21._01._virtual_threads.before;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.IntStream;

public class Application {

    public static void main(String[] args) {

        // Create a fixed thread pool with a limited number of threads
        ExecutorService executor = Executors.newFixedThreadPool(10);

        // Submit tasks to the thread pool
        IntStream.range(0, 50).forEach(i ->
                executor.submit(() -> {
                    System.out.println("Tarea " + i + " ejecutada por " + Thread.currentThread());
                })
        );

        // Shutdown the executor
        executor.shutdown();

        // Optional: Wait until all tasks are finished
        try {
            if (!executor.awaitTermination(1, java.util.concurrent.TimeUnit.MINUTES)) {
                System.err.println("Tasks did not finish in the specified time.");
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.err.println("Interrupted while waiting for executor to terminate.");
        }
    }
}
