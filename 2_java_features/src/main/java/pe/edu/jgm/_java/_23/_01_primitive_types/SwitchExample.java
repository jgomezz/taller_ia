package pe.edu.jgm._java._23._01_primitive_types;

public class SwitchExample {

    void main() {

        double value = 3.14;
        switch (value) {
            case int i -> System.out.println("value is an integer");
            case double d -> System.out.println("value is a double"); // Not possible before Java 23
        }

        double d = 3.14;
        switch (d) {
            case 3.14 -> System.out.println("Value is PI");
            case 2.71 -> System.out.println("Value is Euler's number");
            default -> System.out.println("Value is not a recognized constant");
        }

        float rating = 0.0f;
        switch (rating) {
            case 0f -> System.out.println("0 stars");
            case 2.5f -> System.out.println("Average");
            case 5f -> System.out.println("Best");
            default -> System.out.println("Invalid rating");
        }
    }

}
