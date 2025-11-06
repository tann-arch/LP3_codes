import java.util.*;

public  class fibo{
    static int iterativestep =0;
    static int recursivestep =0;


    public static int iterativeFibo(int n){
        if(n <= 1){ 
        iterativestep++;
            return n;
        }
        int a =0, b =1, c =0;
        System.out.print(a + " " + b + " ");
        for(int i =2 ; i<=n; i++){
            iterativestep++; 
            c = a+b;
            a = b;
            b = c;
            System.out.print(c + " ");
        }
        return b;

    }

    
    public static int recursivefibo(int n){
        recursivestep++;
        if(n <= 1){
            return n;
        }
        else {
            return recursivefibo(n-1) + recursivefibo(n-2);
        }
    }

    public static void main(String[] args){
        Scanner sc = new Scanner (System.in);
        System.out.println("Enter the value for n:");
        int n = sc.nextInt();
        System.out.println("using iterrative approach:"+ iterativeFibo(n));
        System.out.println("\nNumber of steps in Iterative approach: " + iterativestep);
        System.out.println("using recursive approach:"+ recursivefibo(n));
        System.out.println("Number of steps in Recursive approach: " + recursivestep);  

        sc.close();
    }
    
}