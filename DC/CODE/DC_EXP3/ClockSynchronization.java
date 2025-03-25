import java.util.Scanner;

class Process {
    private String name;
    private int clock;
    private Scanner scanner;
    private Process otherProcess;
    private static final Object inputLock = new Object(); 

    public Process(String name, int initialTime) {
        this.name = name;
        this.clock = initialTime;
        this.scanner = new Scanner(System.in);
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

    public void startProcess() {
        System.out.println(name + " initial time: " + clock);

        while (true) {
            synchronized (inputLock) { 
                System.out.print(name + ": Enter 'send' to send packet, 'exit' to quit: ");
                String input = scanner.nextLine().trim().toLowerCase();

                if (input.equals("exit")) {
                    System.out.println(name + " is exiting...");
                    break;
                } else if (input.equals("send")) {
                    sendPacket();
                } else {
                    System.out.println("Invalid command. Please enter 'send' or 'exit'.");
                }
            }
        }
    }
}

public class ClockSynchronization {
    public static void main(String[] args) {
        Process process1 = new Process("Process 1", 0);
        Process process2 = new Process("Process 2", 5);

        process1.setOtherProcess(process2);
        process2.setOtherProcess(process1);

        Thread t1 = new Thread(process1::startProcess);
        Thread t2 = new Thread(process2::startProcess);

        t1.start(); 

        try {
            Thread.sleep(100); 
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        t2.start(); 
    }
}