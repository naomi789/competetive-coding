import java.util.*;
import java.io.*;
import java.lang.*;
public class Cictro{
  final static byte[][] IV = {{(byte)31, (byte)56, (byte)156, (byte)167}, {(byte)38, (byte)240, (byte)174, (byte)248}};
  static byte[][] w;
  /******CODE TAKEN FROM https://stackoverflow.com/questions/19181411/circular-rotate-issue-with-rotate-left***/
  static final byte BYTE_BITS = (byte)8;
  public static byte rotateRight(byte bits, int shift)
  {
     return (byte)(((bits & 0xff)  >>> shift) | ((bits & 0xff) << (8 - shift)));
  }
  public static byte rotateLeft(byte bits, int shift)
  {
    return (byte)(((bits & 0xff) << shift) | ((bits & 0xff) >>> (8 - shift)));
  }
  /***********************************************************************************/
  public static void alpha() {
    byte a = w[0][0];
    byte b = w[0][1];
    byte c = w[0][2];
    byte d = w[0][3];
    w[0][0] = w[1][0];
    w[0][1] = w[1][1];
    w[0][2] = w[1][2];
    w[0][3] = w[1][3];
    w[1][0] = a;
    w[1][1] = b;
    w[1][2] = c;
    w[1][3] = d;
  }
  public static void beta() //Current implementation: a xor= b: a = a ^ b
  {
    w[0][0] = (byte)(w[0][0] ^ w[1][3]);
    w[0][1] = (byte)(w[0][1] ^ w[1][2]);
    w[0][2] = (byte)(w[0][2] ^ w[1][1]);
    w[0][3] = (byte)(w[0][3] ^ w[1][0]);
  }
  public static void gamma() { //Pretty bad permutation function imo
    byte a = w[0][0];
    byte b = w[0][1];
    byte c = w[0][2];
    byte d = w[0][3];
    byte e = w[1][0];
    byte f = w[1][1];
    byte g = w[1][2];
    byte h = w[1][3];
    w[0][3] = a;
    w[1][2] = b;
    w[1][3] = c;
    w[1][1] = d;
    w[0][1] = e;
    w[1][0] = f;
    w[0][2] = g;
    w[0][0] = h;
  }
  public static void delta() {
    w[0][0] = rotateLeft(w[0][0], 1);
    w[1][0] = rotateLeft(w[1][0], 1);
    w[0][2] = rotateLeft(w[0][2], 1);
    w[1][2] = rotateLeft(w[1][2], 1);
    w[0][1] = rotateRight(w[0][1], 1);
    w[1][1] = rotateRight(w[1][1], 1);
    w[0][3] = rotateRight(w[0][3], 1);
    w[1][3] = rotateRight(w[1][3], 1);
  }
  public static void hashFunction() {
    int count = 0;
    while (count < 50)
    {
      alpha();
      beta();
      gamma();
      delta();
      count++;
    }
  }
  public static void sponge(byte[] blockInput) {
    w[0][0] = (byte)(w[0][0] ^ blockInput[0]);
    w[0][1] = (byte)(w[0][1] ^ blockInput[1]);
    w[0][2] = (byte)(w[0][2] ^ blockInput[2]);
    w[0][3] = (byte)(w[0][3] ^ blockInput[3]);
    hashFunction();
  }
  public static String CictroHash(String value) {
    char[] ascii= value.toCharArray();
    w = new byte[2][4];
    w[0][0] = IV[0][0];
    w[0][1] = IV[0][1];
    w[0][2] = IV[0][2];
    w[0][3] = IV[0][3];
    w[1][0] = IV[1][0];
    w[1][1] = IV[1][1];
    w[1][2] = IV[1][2];
    w[1][3] = IV[1][3];

    while(ascii.length % 4 != 0)
    {
      ascii = new char[ascii.length + 1];
      int i= 0;
      for(; i < value.length(); i++)
      {
        ascii[i] = value.charAt(i);
      }
      ascii[ascii.length - 1] = (char)0;
    }
    int blockstart = 0;
    byte[] curblock = new byte[4];
    while(blockstart != ascii.length)
    {
      curblock[0] = (byte)ascii[blockstart];
      curblock[1] = (byte)ascii[blockstart + 1];
      curblock[2] = (byte)ascii[blockstart + 2];
      curblock[3] = (byte)ascii[blockstart + 3];
      sponge(curblock);
      blockstart += 4;
    }
    String result = "";
    StringBuilder sb = new StringBuilder();
    sb.append(String.format("%02X", w[0][0]));
    sb.append(String.format("%02X", w[0][1]));
    sb.append(String.format("%02X", w[0][2]));
    sb.append(String.format("%02X", w[0][3]));
    /*return (Integer.toHexString(w[0][0]) + Integer.toHexString(w[0][1]) + Integer.toHexString(w[0][2]) + Integer.toHexString(w[0][3]));*/
    return sb.toString();
  }
  //code from https://stackoverflow.com/questions/20536566/creating-a-random-string-with-a-z-and-0-9-in-java
  public static String getSaltString() {
        int length = (int)(Math.random() * 25);
        String SALTCHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@~`#$%^&*()_+-={}[]|:;<,>.?/abcdefghijklmnopqrstuvwxyz";
        StringBuilder salt = new StringBuilder();
        Random rnd = new Random();
        while (salt.length() < length) { // length of the random string.
            int index = (int) (rnd.nextFloat() * SALTCHARS.length());
            salt.append(SALTCHARS.charAt(index));
        }
        String saltStr = salt.toString();
        return saltStr;

  }
  public static void main(String[] args)
  { //Does the birthday attack!
    int max = 126;
    int min = 32;
    String a = getSaltString();
    String b = getSaltString();
    while(!(CictroHash(a).equals(CictroHash(b)) && !a.equals(b)))
    {
      b = getSaltString();
      a = getSaltString();
    }
    System.out.println("DONE");
    System.out.println("String a is:" + a + "!");
    System.out.println("String b is:" + b + "!");
    
  }
}
