import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) throws IOException {
        int PORT = 2004;
        ServerSocket serverSocket = new ServerSocket(PORT);
        System.out.println("Server started on port " + PORT);

        while (true) {
            Socket client = serverSocket.accept();
            System.out.println("Client connected: " + client.getInetAddress());
            new ClientHandler(client).start();
        }
    }
}

class ClientHandler extends Thread {
    private final Socket client;

    public ClientHandler(Socket client) {
        this.client = client;
    }

    public void run() {
        try (BufferedReader input = new BufferedReader(new InputStreamReader(client.getInputStream()));
             PrintWriter output = new PrintWriter(client.getOutputStream(), true)) {

            output.println("Server is working:");
            String message;
            while ((message = input.readLine()) != null) {
                System.out.println("Received: " + message);
                output.println("Server message: " + message);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
