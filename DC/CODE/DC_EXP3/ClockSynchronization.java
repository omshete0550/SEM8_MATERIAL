import java.util.Scanner;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

class Process implements Runnable {
    private String name;
    private int clock;
    private BlockingQueue<String> commandQueue = new LinkedBlockingQueue<>();
    private Process otherProcess;

    public Process(String name, int initialTime) {
        this.name = name;
        this.clock = initialTime;
    }

    public void setOtherProcess(Process otherProcess) {
        this.otherProcess = otherProcess;
    }

    public void sendPacket() {
        clock++;
        System.out.println(name + " sent a packet at time " + clock);
        otherProcess.receivePacket(clock);
    }

    public void receivePacket(int senderClock) {
        clock = Math.max(clock + 1, senderClock + 1);
        System.out.println(name + " received a packet at time " + clock);
    }

    public void enqueueCommand(String command) {
        commandQueue.offer(command);
    }

    @Override
    public void run() {
        System.out.println(name + " initial time: " + clock);
        try {
            while (true) {
                String command = commandQueue.take(); // blocks until command is received
                if (command.equalsIgnoreCase("send")) {
                    sendPacket();
                } else if (command.equalsIgnoreCase("exit")) {
                    System.out.println(name + " is exiting...");
                    break;
                }
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}

public class ClockSynchronization {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Process process1 = new Process("Process 1", 0);
        Process process2 = new Process("Process 2", 5);

        process1.setOtherProcess(process2);
        process2.setOtherProcess(process1);

        Thread t1 = new Thread(process1);
        Thread t2 = new Thread(process2);

        t1.start();
        t2.start();

        while (true) {
            System.out.print("Enter command (e.g., '1 send', '2 send', '1 exit', '2 exit'): ");
            String input = scanner.nextLine().trim().toLowerCase();

            if (input.startsWith("1 ")) {
                process1.enqueueCommand(input.substring(2));
                if (input.endsWith("exit"))
                    break;
            } else if (input.startsWith("2 ")) {
                process2.enqueueCommand(input.substring(2));
                if (input.endsWith("exit"))
                    break;
            } else {
                System.out.println("Invalid input. Use '1 send', '2 send', '1 exit', or '2 exit'.");
            }
        }

        scanner.close();
    }
}
