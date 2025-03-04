import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) throws IOException {
        String HOST = "127.0.0.1";
        int PORT = 2004;

        Socket socket = new Socket(HOST, PORT);
        BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        PrintWriter output = new PrintWriter(socket.getOutputStream(), true);
        Scanner scanner = new Scanner(System.in);

        System.out.println(input.readLine()); // Server welcome message

        while (true) {
            System.out.print("Enter message: ");
            String message = scanner.nextLine();
            output.println(message);
            System.out.println(input.readLine()); // Server response
        }
    }
}
