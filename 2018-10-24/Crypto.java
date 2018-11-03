import java.lang.*;
import java.util.*;

class Main {
  static int curBeginIndex;
  static int curEndIndex;
  static int[] shiftBlock;
  static char[] cipherText;
  static char[] knownPlainText;
  public static void printRemainder(char[] c,char[] k) {
    curEndIndex = c.length - 1;
    char[] plainText = new char[curEndIndex - curBeginIndex + 1];
    int tempIndex = curBeginIndex;
    for(int i = 0; i < plainText.length; i++)
    {
      shiftBlock[i] = (int)k[i] - 65;
    }
    for(int i = 0; i < plainText.length; i++)
    {
      int temp = (int)c[tempIndex + i] - 65 - shiftBlock[i];
      if(temp < 0)
      {
        temp = (26 + temp);
      }
      System.out.print((char)(temp + 65));
      plainText[i] = (char)(temp + 65);
    }
  }
  public static char[] printPlainText(char[] c, char[] k) {
    char[] plainText = new char[k.length];
    int tempIndex = curBeginIndex;
    for(int i = 0; i < shiftBlock.length; i++)
    {
      shiftBlock[i] = (int)k[i] - 65;
    }
    for(int i = 0; i < plainText.length; i++)
    {
      int temp = (int)c[tempIndex + i] - 65 - shiftBlock[i];
      if(temp < 0)
      {
        temp = (26 + temp);
      }
      System.out.print((char)(temp + 65));
      plainText[i] = (char)(temp + 65);
    }
    return plainText;
  }
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    cipherText = in.nextLine().toCharArray();
    knownPlainText = in.nextLine().toCharArray();
    in.close();
    shiftBlock = new int[knownPlainText.length];
    curBeginIndex = 0;
    curEndIndex = knownPlainText.length - 1;
    while(curEndIndex <= cipherText.length - 1)
    {
      knownPlainText = printPlainText(cipherText, knownPlainText);
      curBeginIndex = curEndIndex + 1;
      curEndIndex = curEndIndex + knownPlainText.length;
    }
    if(curEndIndex != cipherText.length - 1) {
      printRemainder(cipherText, knownPlainText);
    }
  }
}
