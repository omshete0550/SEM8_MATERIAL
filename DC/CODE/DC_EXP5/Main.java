import java.util.*;

class Node {
    int nodeId;
    int parentNode;
    boolean hasToken;
    Queue<Integer> requestQueue;

    public Node(int nodeId, int parentNode, boolean hasToken) {
        this.nodeId = nodeId;
        this.parentNode = parentNode;
        this.hasToken = hasToken;
        this.requestQueue = new LinkedList<>();
    }

    public void requestToken(int requesterId, Map<Integer, Node> nodes) {
        System.out.println("Process " + requesterId + " sending Request to parent Process " + parentNode);
        System.out.println("Request Queue: " + requestQueue);

        if (hasToken) {
            System.out.println("Parent process " + nodeId + " has the token and sends the token to the request process "
                    + requesterId);
            hasToken = false;
            nodes.get(requesterId).receiveToken();
        } else {
            requestQueue.add(requesterId);
            nodes.get(parentNode).requestToken(requesterId, nodes);
        }
    }

    public void receiveToken() {
        hasToken = true;
        int process = nodeId;
        System.out.println("Process " + process + " enters the Critical Section");
        System.out.println("Request Queue: " + requestQueue);
        if (!requestQueue.isEmpty()) {
            int nextNode = requestQueue.poll();
            System.out.println("Node " + nodeId + " sends token to Node " + nextNode);
            hasToken = false;
            requestQueue.clear();
            System.out
                    .println("Request queue of process " + process + " is empty. Therefore, Release Critical Section");
            System.out.println("Holder: " + nextNode);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of nodes: ");
        int n = sc.nextInt();
        Map<Integer, Node> nodes = new HashMap<>();
        int rootNode = -1;
        for (int i = 0; i < n; i++) {
            System.out.print("Enter Node ID for node " + (i + 1) + ": ");
            int nodeId = sc.nextInt();
            System.out.print("Enter Parent Node ID for Node " + nodeId + ": ");
            int parentNode = sc.nextInt();
            System.out.print("Does this node have the token initially? (true/false): ");
            boolean hasToken = sc.nextBoolean();
            nodes.put(nodeId, new Node(nodeId, parentNode, hasToken));
            if (hasToken)
                rootNode = nodeId;
        }

        System.out.print("Enter Process ID that requests the token: ");
        int requestingNode = sc.nextInt();
        nodes.get(requestingNode).requestToken(requestingNode, nodes);
    }
}
