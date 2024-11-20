package pe.edu.jgm._java._17._03_record.before;

public class Application {

    public static void main(String[] args) {
        Product product = new Product(101, "Teclado", 29.99);

        // Acceder a los campos
        System.out.println("id: " + product.getId());
        System.out.println("Name: " + product.getName());
        System.out.println("Price: $" + product.getPrice());

        // Uso de toString()
        System.out.println(product); // Producto[id=101, nombre=Teclado, precio=29.99]

        // Comparación de productos
        Product otroProducto = new Product(101, "Keyword", 29.99);
        System.out.println(product.equals(otroProducto)); // true


    }

}
