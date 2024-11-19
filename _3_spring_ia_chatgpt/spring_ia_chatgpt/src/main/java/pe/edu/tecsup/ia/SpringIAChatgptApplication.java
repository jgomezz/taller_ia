package pe.edu.tecsup.ia;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication(scanBasePackages = "pe.edu.tecsup.ia")
public class SpringIAChatgptApplication {

    public static void main(String[] args) {
        SpringApplication.run(SpringIAChatgptApplication.class, args);
    }

}
