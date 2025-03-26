import java.util.*;

public class LoadBalancer {
    private Map<Integer, Integer> nodes;
    private int nextNodeId;

    public LoadBalancer() {
        nodes = new HashMap<>();
        nextNodeId = 0;
    }

    public void addNode() {
        nodes.put(nextNodeId++, 0);
        System.out.println("Added Node " + (nextNodeId - 1));
    }

    public void removeNode(int nodeId) {
        if (!nodes.containsKey(nodeId)) {
            System.out.println("Node " + nodeId + " does not exist.");
            return;
        }
        int loadToRedistribute = nodes.get(nodeId);
        nodes.remove(nodeId);
        System.out.println("Removed Node " + nodeId + ". Redistributing " + loadToRedistribute + " processes.");

        for (int i = 0; i < loadToRedistribute; i++) {
            addProcess();
        }
    }

    public void addProcess() {
        if (nodes.isEmpty()) {
            System.out.println("No nodes available to assign process.");
            return;
        }
        int minLoadNode = Collections.min(nodes.entrySet(), Map.Entry.comparingByValue()).getKey();
        nodes.put(minLoadNode, nodes.get(minLoadNode) + 1);
        System.out.println("Assigned process to Node " + minLoadNode);
    }

    public void removeProcess(int nodeId) {
        if (!nodes.containsKey(nodeId) || nodes.get(nodeId) == 0) {
            System.out.println("No process to remove from Node " + nodeId);
            return;
        }
        nodes.put(nodeId, nodes.get(nodeId) - 1);
        System.out.println("Removed process from Node " + nodeId);
    }

    public void displayNodes() {
        System.out.println("Current Load Distribution: " + nodes);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        LoadBalancer lb = new LoadBalancer();

        while (true) {
            System.out.println("\n1. Add Process");
            System.out.println("2. Remove Process");
            System.out.println("3. Add Node");
            System.out.println("4. Remove Node");
            System.out.println("5. Exit");
            System.out.print("Enter choice: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    lb.addProcess();
                    break;
                case 2:
                    System.out.print("Enter Node ID to remove process from: ");
                    int nodeId = scanner.nextInt();
                    lb.removeProcess(nodeId);
                    break;
                case 3:
                    lb.addNode();
                    break;
                case 4:
                    System.out.print("Enter Node ID to remove: ");
                    int removeNodeId = scanner.nextInt();
                    lb.removeNode(removeNodeId);
                    break;
                case 5:
                    System.out.println("Exiting...");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice. Try again.");
            }
            lb.displayNodes();
        }
    }
}