import java.awt.image.BufferedImage;
import java.util.*;
import java.io.*;
import java.lang.*;
import javax.imageio.ImageIO;
public class Main{
  public static void main(String[] args) throws Exception
  {
    BufferedImage bi = ImageIO.read(new File("music.png"));
    int[] pixel;
    String s = "";
    for (int y = 0; y < bi.getHeight(); y++) {
      for (int x = 0; x < bi.getWidth(); x++) {
        pixel = bi.getRaster().getPixel(x, y, new int[3]);
        //System.out.println(pixel[0] + " - " + pixel[1] + " - " + pixel[2] + " - " + (bi.getWidth() * y + x));
        System.out.print((char)pixel[0]);
        System.out.print((char)pixel[1]);
        System.out.print((char)pixel[2]);
      }
    }
  }
}
