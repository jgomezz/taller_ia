package pe.edu.tecsup.ia.webs;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import pe.edu.tecsup.ia.services.ChatGptService;

import java.util.Map;

@RestController
@RequestMapping("/api/chatgpt")
public class ChatGptController {

    @Autowired
    private ChatGptService chatGptService;

    @PostMapping("/generate-questions")
    public ResponseEntity<String> generateQuestions(@RequestBody Map<String, Object> payload) {
        String prompt = (String) payload.get("prompt");
        String response = chatGptService.generateQuestions(prompt);
        return ResponseEntity.ok(response);
    }
}