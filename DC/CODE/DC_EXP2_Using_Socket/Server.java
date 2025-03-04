import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class Server {
    public static void main(String[] args) {
        String multicastGroup = "230.0.0.0"; // Multicast Group IP
        int port = 4567;

        try (DatagramSocket socket = new DatagramSocket()) {
            InetAddress group = InetAddress.getByName(multicastGroup);
            String message = "Hello, Clients! Welcome to Group Communication.";

            DatagramPacket packet = new DatagramPacket(
                message.getBytes(), message.length(), group, port
            );

            socket.send(packet);
            System.out.println("Message sent to group: " + message);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
