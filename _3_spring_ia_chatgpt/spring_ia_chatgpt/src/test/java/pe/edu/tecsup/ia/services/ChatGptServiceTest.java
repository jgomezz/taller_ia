package pe.edu.tecsup.ia.services;

import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import static org.junit.jupiter.api.Assertions.*;

@Slf4j
@SpringBootTest
public class ChatGptServiceTest {

    @Autowired
    ChatGptService chatGptService;

    @Test
    void generateQuestions() {

        log.info("Start test");

        String question = "Give an joke";

        String response = this.chatGptService.generateQuestions(question);

        log.info(response);
    }
}