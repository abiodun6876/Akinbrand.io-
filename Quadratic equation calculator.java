import java.util.Scanner;

class MyClass {

  public static void main(String[] args) {

    int a,b,c;

    double d, x1, x2;

    Scanner myObj = new Scanner(System.in);

    

    System.out.println("QUADRATIC EQUATION SOLVER");

    System.out.println("ax^2 + bx + c = 0");

    

    System.out.print("Enter the value of a: ");

    a = myObj.nextInt();

    System.out.print("Enter the value of b: ");

    b = myObj.nextInt();

    

    System.out.print("Enter the value of c: ");

    c = myObj.nextInt();

    

    d = Math.sqrt(b*b - 4*a*c);

    x1 = (-b + d) / (2*a);

    x2 = (-b - d) / (2*a);

    

    System.out.println("\nThe solutions are:");

    System.out.println("x1 = " + x1);

    System.out.println("x2 = " + x2);

  }

}

