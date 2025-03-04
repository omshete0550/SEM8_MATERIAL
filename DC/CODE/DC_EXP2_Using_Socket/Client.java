import java.io.IOException;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.net.MulticastSocket;

public class Client {
    public static void main(String[] args) {
        String multicastGroup = "230.0.0.0"; // Must match the server group
        int port = 4567;

        try (MulticastSocket socket = new MulticastSocket(port)) {
            InetAddress group = InetAddress.getByName(multicastGroup);
            socket.joinGroup(group);

            byte[] buffer = new byte[1024];
            DatagramPacket packet = new DatagramPacket(buffer, buffer.length);

            System.out.println("Listening for messages...");

            // Receive message
            socket.receive(packet);
            String receivedMessage = new String(packet.getData(), 0, packet.getLength());

            System.out.println("Received: " + receivedMessage);

            socket.leaveGroup(group);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
