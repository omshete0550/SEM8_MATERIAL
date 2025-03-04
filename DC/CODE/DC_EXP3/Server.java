import java.io.*;
import java.net.*;
import java.util.*;

public class Server {
    private static final int PORT = 5000;
    private static final List<ClientHandler> clients = new ArrayList<>();
    private static final List<Long> times = new ArrayList<>();

    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("Clock Server started...");

            while (clients.size() < 3) { 
                Socket clientSocket = serverSocket.accept();
                System.out.println("Client connected: " + clientSocket.getInetAddress());

                ClientHandler clientHandler = new ClientHandler(clientSocket);
                clients.add(clientHandler);
                clientHandler.start();
            }

            synchronizeClocks();

        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            closeAllClients();
        }
    }

    private static void synchronizeClocks() {
        try {
            for (ClientHandler client : clients) {
                client.requestTime();
            }

            long avgTime = times.stream().mapToLong(Long::longValue).sum() / times.size();
            System.out.println("Calculated average time: " + avgTime);

            for (ClientHandler client : clients) {
                client.adjustTime(avgTime);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void closeAllClients() {
        for (ClientHandler client : clients) {
            client.closeConnection();
        }
    }

    static class ClientHandler extends Thread {
        private final Socket socket;
        private PrintWriter output;
        private BufferedReader input;

        public ClientHandler(Socket socket) {
            this.socket = socket;
        }

        public void run() {
            try {
                input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                output = new PrintWriter(socket.getOutputStream(), true);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        public void requestTime() throws IOException {
            output.println("GET_TIME");
            long clientTime = Long.parseLong(input.readLine());
            System.out.println("Received time from client: " + clientTime);
            times.add(clientTime);
        }

        public void adjustTime(long newTime) {
            output.println("SET_TIME " + newTime);
        }

        public void closeConnection() {
            try {
                socket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
