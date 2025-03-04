import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) {
        int PORT = 4568;

        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
             System.out.println("Server running on port " + PORT + "... Waiting for client...");

            try (Socket socket = serverSocket.accept();
                 BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                 PrintWriter output = new PrintWriter(socket.getOutputStream(), true)) {

                System.out.println("Client connected: " + socket.getInetAddress());

                // Read two numbers
                int a = Integer.parseInt(input.readLine());
                int b = Integer.parseInt(input.readLine());

                System.out.println("Received numbers: " + a + ", " + b);

                // Send result
                output.println(a + b);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
