package pe.edu.tecsup.ia.services;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service
public class ChatGptService {

    @Value("${openai.api-key}")
    private String openaiApiKey;

    private   ChatClient chatClient;

    public ChatGptService(ChatClient.Builder chatClientBuilder) {
        this.chatClient = chatClientBuilder.build();
    }


    public String generateQuestions(String prompt) {

        String response = chatClient
                .prompt()
                .user(prompt)
                .call()
                .content();

        return response;
    }
}
