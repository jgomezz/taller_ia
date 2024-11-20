package pe.edu.jgm._java._21._01._virtual_threads.now;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.IntStream;

public class Application {

    public static void main(String[] args) {

        ExecutorService executor = Executors.newVirtualThreadPerTaskExecutor();

        IntStream.range(0, 50).forEach(i ->
                executor.submit(() -> {
                    System.out.println("Tarea " + i + " ejecutada por " + Thread.currentThread());
                })
        );

        executor.shutdown(); // Clean up

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
