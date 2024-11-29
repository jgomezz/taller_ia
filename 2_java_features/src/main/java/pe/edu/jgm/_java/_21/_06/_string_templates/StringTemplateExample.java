package pe.edu.jgm._java._21._06._string_templates;

public class StringTemplateExample {

    void main() {

        // Status Quo of Java String Concatenation
        int a = 10;
        int b = 21;

        String concatenated = a + " times " + b + " = " + a * b;
        System.out.println(concatenated);

        String format       = String.format("%d times %d = %d", a, b, a * b);
        System.out.println(format);

        String formatted    = "%d times %d = %d".formatted(a, b, a * b);
        System.out.println(formatted);

        // String Interpolation With String Templates
        int x = 5;

        String mensaje = STR."El valor de x es \{x}";
        System.out.println(mensaje); // Imprime "El valor de x es 5"
    }
}
