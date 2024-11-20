package pe.edu.jgm._java._17._04._switch;

public class Application {

    public static void main(String[] args) {
        int num = 2;
        String resultado = switch (num) {
            case 1 -> "One";
            case 2 -> "Two";
            default -> "Another";
        };
        System.out.println(resultado); // Imprime "Dos"
    }
}
