import java.util.*;

class Item {
    double value, weight;
    Item(double v, double w) {
        value = v;
        weight = w;
    }
}

public class Knapsack {

    public static double getMaxValue(Item[] items, double capacity) {
        // Step 1: Sort by value/weight ratio (descending)
        Arrays.sort(items, (a, b) -> Double.compare(b.value / b.weight, a.value / a.weight));

        double totalValue = 0.0; // Total profit
        double currentWeight = 0.0;

        // Step 2: Take items greedily
        for (Item item : items) {
            if (currentWeight + item.weight <= capacity) {
                // Take full item
                currentWeight += item.weight;
                totalValue += item.value;
            } else {
                // Take fraction
                double remain = capacity - currentWeight;
                totalValue += item.value * (remain / item.weight);
                break; // knapsack full
            }
        }
        return totalValue;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of items: ");
        int n = sc.nextInt();

        Item[] items = new Item[n];
        for (int i = 0; i < n; i++) {
            System.out.print("Enter value and weight of item " + (i + 1) + ": ");
            double value = sc.nextDouble();
            double weight = sc.nextDouble();
            items[i] = new Item(value, weight);
        }

        System.out.print("Enter capacity of knapsack: ");
        double capacity = sc.nextDouble();

        double maxValue = getMaxValue(items, capacity);
        System.out.println("\nMaximum value in Knapsack = " + maxValue);

        sc.close();
    }
}

