import java.util.Scanner;

public class Main {

 public static void main(String[] args){

 	int num_pol = 0;
 	int num_untr = 0;

 	Scanner scanner = new Scanner(System.in);
 	int n = scanner.nextInt();
 	for (int i = 0; i < n; i++){
 		int event = scanner.nextInt();
 		if (event != -1)
 			num_pol += event;
 		else if(num_pol > 0)
 			num_pol -= 1;
 		else
 			num_untr += 1;
 	}
 	System.out.println(num_untr);
 }

}
