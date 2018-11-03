import java.lang.*;
import java.util.*;
import java.io.*;

public class Zebra{
  static int belltoll;
  public static boolean done(char[] test) {
    boolean b = true;
    for(int i = 0; i < test.length; i++)
    {
      if(test[i] == 'O')
      {
        b = false;
        break;
      }
    }
    return b;
  }
  public static char[] ringBell(char[] init)
  {
    int index = init.length - 1;
    for(int i = init.length - 1; i >= 0; i--)
    {
      if(init[i] == 'O')
      {
        index = i;
        init[i] = 'Z';
        break;
      }
    }
    for(int i = index + 1; i < init.length; i++)
    {
      if(init[i] == 'Z')
      {
        init[i] = 'O';
      }
    }
    return init;
  }
  public static void main(String[] args)
  {
    Scanner in = new Scanner(System.in);
    int size = in.nextInt();
    char[] arr = new char[size];
    int index = 0;
    while(size > 0)
    {
      String s = in.next();
      arr[index] = s.charAt(0);
      index++;
      size--;
    }
    belltoll = 0;
    while(!done(arr))
    {
      arr = ringBell(arr);
      belltoll++;
    }
    System.out.println(belltoll);
  }
}
