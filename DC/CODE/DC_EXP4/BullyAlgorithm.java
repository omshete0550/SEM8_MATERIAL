import java.util.*;

public class BullyAlgorithm {
    static int n;
    static int co;
    static int status[] = new int[100];
    static int process[] = new int[100];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of processes:");

        n = sc.nextInt();
        int i, c, cl = 1;
        for (i = 0; i < n; i++) {
            status[i] = 1;
            process[i] = i;
        }

        boolean choice = true;
        int ch;
        do {
            System.out.println("\nChoose an option:");
            System.out.println("1. Crash Process");
            System.out.println("2. Recover Process");
            System.out.println("3. Exit");
            System.out.println(">");
            ch = sc.nextInt();
            switch (ch) {
                case 1:
                    System.out.println("Enter the process to crash:");
                    c = sc.nextInt();
                    status[c - 1] = 0;
                    cl = 1;
                    break;
                case 2:
                    System.out.println("Enter the process to recover:");
                    c = sc.nextInt();
                    status[c - 1] = 1;
                    break;
                case 3:
                    choice = false;
                    cl = 0;
                    break;
                default:
                    System.out.println("Invalid option. Please try again.");
            }
            if (cl == 1) {
                System.out.println("Which process will initiate election: ");
                int ele = sc.nextInt();
                elect(ele);
            }
            System.out.println("Final Co-ordinator is " + co);
            // sc.close();
        } while (choice);

    }

    static void elect(int ele) {
        ele = ele - 1;
        co = ele + 1;

        for (int i = 0; i < n; i++) {
            if (process[ele] < process[i]) {
                System.out.println("Election message is sent from " + (ele + 1) + " to " + (i + 1));
                if (status[i] == 1)
                    System.out.println("Ok message is sent from " + (i + 1) + " to " + (ele + 1));
                if (status[i] == 1)
                    elect(i + 1);
            }
        }
    }
}
