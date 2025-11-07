import java.util.*;

public class zeroneknapsack {

    public static int knapSack(int W, int wt[], int val[], int n) {
        int[][] K = new int[n + 1][W + 1];

        // Build table K[][] in bottom-up manner
        for (int i = 0; i <= n; i++) {
            for (int w = 0; w <= W; w++) {
                if (i == 0 || w == 0)
                    K[i][w] = 0;
                else if (wt[i - 1] <= w)
                    K[i][w] = Math.max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]);
                else
                    K[i][w] = K[i - 1][w];
            }
        }

        return K[n][W];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of items: ");
        int n = sc.nextInt();

        int[] val = new int[n];
        int[] wt = new int[n];

        for (int i = 0; i < n; i++) {
            System.out.print("Enter value and weight of item " + (i + 1) + ": ");
            val[i] = sc.nextInt();
            wt[i] = sc.nextInt();
        }

        System.out.print("Enter capacity of knapsack: ");
        int W = sc.nextInt();

        System.out.println("\nMaximum value that can be put in knapsack = " + knapSack(W, wt, val, n));
        sc.close();
    }
}
