import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        String HOST = "127.0.0.1";
        int PORT = 4568;

        try  (Socket socket = new Socket(HOST, PORT);
             PrintWriter output = new PrintWriter(socket.getOutputStream(), true);
             BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             Scanner scanner = new Scanner(System.in)) {

            System.out.print("Enter two numbers: ");
            output.println(scanner.nextInt());
            output.println(scanner.nextInt());

            System.out.println("Sum received from server: " + input.readLine());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

        