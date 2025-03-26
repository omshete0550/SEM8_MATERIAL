import java.util.Scanner;

public class BankersAlgorithm {
    private int processes, resources;
    private int[][] max, alloc, need;
    private int[] available;

    public BankersAlgorithm(int processes, int resources) {
        this.processes = processes;
        this.resources = resources;
        max = new int[processes][resources];
        alloc = new int[processes][resources];
        need = new int[processes][resources];
        available = new int[resources];
    }

    public void input(Scanner scanner) {
        System.out.println("Enter the available resources:");
        for (int i = 0; i < resources; i++) {
            System.out.print("Resource R" + i + ": ");
            available[i] = scanner.nextInt();
        }

        System.out.println("Enter the Max resources for each process:");
        for (int i = 0; i < processes; i++) {
            System.out.print("P" + i + ": ");
            for (int j = 0; j < resources; j++) {
                max[i][j] = scanner.nextInt();
            }
        }

        System.out.println("Enter the Allocated resources for each process:");
        for (int i = 0; i < processes; i++) {
            System.out.print("P" + i + ": ");
            for (int j = 0; j < resources; j++) {
                alloc[i][j] = scanner.nextInt();
                need[i][j] = max[i][j] - alloc[i][j];
                available[j] -= alloc[i][j];
            }
        }
    }

    public boolean isSafeState() {
        boolean[] finished = new boolean[processes];
        int[] work = available.clone();
        int count = 0;

        while (count < processes) {
            boolean found = false;
            for (int i = 0; i < processes; i++) {
                if (!finished[i]) {
                    boolean canExecute = true;
                    for (int j = 0; j < resources; j++) {
                        if (need[i][j] > work[j]) {
                            canExecute = false;
                            break;
                        }
                    }
                    if (canExecute) {
                        for (int j = 0; j < resources; j++) {
                            work[j] += alloc[i][j];
                        }
                        finished[i] = true;
                        found = true;
                        count++;
                    }
                }
            }
            if (!found)
                break;
        }

        for (boolean f : finished) {
            if (!f)
                return false;
        }
        return true;
    }

    public void displayNeedMatrix() {
        System.out.println("Need Matrix:");
        for (int i = 0; i < processes; i++) {
            System.out.print("P" + i + ": ");
            for (int j = 0; j < resources; j++) {
                System.out.print(need[i][j] + " ");
            }
            System.out.println();
        }
    }

    public void displayAvailableResources() {
        System.out.print("Resources Remaining: ");
        for (int i = 0; i < resources; i++) {
            System.out.print(available[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of processes: ");
        int processes = scanner.nextInt();
        System.out.print("Enter the number of resources: ");
        int resources = scanner.nextInt();

        BankersAlgorithm bankers = new BankersAlgorithm(processes, resources);
        bankers.input(scanner);

        bankers.displayNeedMatrix();
        bankers.displayAvailableResources();

        if (bankers.isSafeState()) {
            System.out.println("System is in a SAFE state.");
        } else {
            System.out.println("System is UNSAFE. Deadlock possible!");
        }
    }
}
