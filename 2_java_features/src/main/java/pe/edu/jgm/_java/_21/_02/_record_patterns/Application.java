package pe.edu.jgm._java._21._02._record_patterns;

import java.util.List;

/**
 *  With Record Patterns in Java 21, you can destructure and match objects easily
 */
public class Application {

    public static void main(String[] args) {

        List<Product> products = List.of(
            new Product(100, "Keyword", 60.8),
            new Product(101, "Mouse", 30.5),
            new Product(102, "CPU", 800.5)
        );

        products.stream()
                .filter(item -> item instanceof Product(int id, String name, double price ) && price > 100)
                .forEach(System.out::println);

    }
}
