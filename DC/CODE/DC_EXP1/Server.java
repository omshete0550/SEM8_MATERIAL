import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) {
        int PORT = 4568;

        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("Server is running… Waiting for client...");

            try (Socket socket = serverSocket.accept();
                    BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                    PrintWriter output = new PrintWriter(socket.getOutputStream(), true)) {

                System.out.println("Client connected: " + socket.getInetAddress());

                String clientMessage;
                while ((clientMessage = input.readLine()) != null) {
                    System.out.println("Client: " + clientMessage);

                    if (clientMessage.equalsIgnoreCase("exit")) {
                        System.out.println("Client disconnected.");
                        break;
                    }
                    output.println("Server: " + clientMessage + " good morning");
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
