import java.io.*;
import java.net.*;
import java.util.Scanner;

public class GroupChatClient {
    public static void main(String[] args) {
        String HOST = "127.0.0.1";
        int PORT = 4568;

        try (Socket socket = new Socket(HOST, PORT);
                BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter output = new PrintWriter(socket.getOutputStream(), true);
                Scanner scanner = new Scanner(System.in)) {

            System.out.print(input.readLine() + " ");
            String name = scanner.nextLine();
            output.println(name);

            new Thread(() -> {
                try {
                    String serverMessage;
                    while ((serverMessage = input.readLine()) != null) {
                        System.out.println(serverMessage);
                    }
                } catch (IOException e) {
                    System.out.println("Disconnected from chat.");
                }
            }).start();

            while (true) {
                String message = scanner.nextLine();
                if (message.equalsIgnoreCase("exit")) {
                    output.println("exit");
                    System.out.println("You left the chat.");
                    break;
                }
                output.println(message);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
