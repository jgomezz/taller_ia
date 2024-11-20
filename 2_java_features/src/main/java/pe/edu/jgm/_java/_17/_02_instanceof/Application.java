package pe.edu.jgm._java._17._02_instanceof;

public class Application {

    public static void main(String[] args) {

        Object obj = "Hello world";

        // Before
        if (obj instanceof String) {
            String s = (String) obj;
            System.out.println(s);
        }
        // Now
        if (obj instanceof String s) {
            System.out.println(s);
        }
    }
}
