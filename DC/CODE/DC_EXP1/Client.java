import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        String HOST = "127.0.0.1";
        int PORT = 4568;

        try (Socket socket = new Socket(HOST, PORT);
                PrintWriter output = new PrintWriter(socket.getOutputStream(), true);
                BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                Scanner scanner = new Scanner(System.in)) {

            System.out.println("Connected to server…");

            String userMessage;
            while (true) {
                System.out.print("Enter msg for server: ");
                userMessage = scanner.nextLine();
                output.println(userMessage);

                if (userMessage.equalsIgnoreCase("exit")) {
                    System.out.println("Closing connection...");
                    break;
                }

                System.out.println("Process 1: " + input.readLine());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
