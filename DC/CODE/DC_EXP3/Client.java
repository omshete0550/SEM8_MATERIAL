import java.io.*;
import java.net.*;
import java.util.Random;

public class Client {
    public static void main(String[] args) {
        String SERVER_HOST = "127.0.0.1"; // Change if needed
        int SERVER_PORT = 5000;

        try (Socket socket = new Socket(SERVER_HOST, SERVER_PORT);
             BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             PrintWriter output = new PrintWriter(socket.getOutputStream(), true)) {

            long localTime = System.currentTimeMillis() + new Random().nextInt(10000) - 5000; // Simulated time drift
            System.out.println("Client's initial time: " + localTime);

            while (true) {
                String serverMessage = input.readLine();
                if (serverMessage == null) break;

                if (serverMessage.equals("GET_TIME")) {
                    output.println(localTime);
                } else if (serverMessage.startsWith("SET_TIME")) {
                    long newTime = Long.parseLong(serverMessage.split(" ")[1]);
                    localTime = newTime;
                    System.out.println("Client's adjusted time: " + localTime);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
