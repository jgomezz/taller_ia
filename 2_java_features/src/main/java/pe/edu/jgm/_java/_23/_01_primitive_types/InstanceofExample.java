package pe.edu.jgm._java._23._01_primitive_types;

// Primitive Types in instanceof:
public class InstanceofExample {

    void main() {
        
        int value = 42;

        // Old way (still works)
        if (value instanceof Integer) {
            System.out.println("value is an Integer");
        }

        // Possible with Java 23
        if (value instanceof int) {
            System.out.println("value is an int");
        }
    }


}
