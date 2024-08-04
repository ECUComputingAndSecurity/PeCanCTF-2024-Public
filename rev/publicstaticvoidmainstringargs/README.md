# Flag

Flag is `pecan{kr3w ver tAErg}`.

The challenge protects against brute forcing using a boolean condition in the code which basically forces the competitors to use their rev-eng knowledge rather than trying different inputs and checking if it contains 'pecan' and finding the result.

Requires Java 22 and ability to decompile, edit, and recompile the code. Since Java 22 is quite new and probably not added to some stable repos, some competitors may need to spend more time and skill installing Java 22 to get it to work.
Some may just use an online Java decompiler and work from there.

Users can run the program using `java PublicStaticVoidMainStringArgs.class`.
Users are only given the class file, not the source code, even though they decompile to very similar looking code (just without useful names).

For example, Fernflower decompiles it as follows:
```java
import java.io.PrintStream;

public class PublicStaticVoidMainStringArgs {
   final double random = Math.random() * 1024.0D;
   boolean toggle = true;

   public static void main(String[] var0) {
      new PublicStaticVoidMainStringArgs(var0);
   }

   public PublicStaticVoidMainStringArgs(String[] var1) {
      System.out.println(this.a(var1));
   }

   private String a(String[] var1) {
      if (var1.length == 1) {
         if (var1[0].length() != 1) {
            return this.c(this.b(0), 5);
         } else if (var1[0].equals("%")) {
            byte var8 = -6;
            return this.c(this.b(1), var8 * 1 + 1);
         } else if (var1[0].charAt(0) < '\\') {
            PrintStream var10000 = System.out;
            double var10001 = Math.random();
            var10000.println("your number is " + (int)(var10001 * 100.0D));
            if (this.random == 1.23D) {
               this.toggle = false;
            }

            System.out.println(this.toggle);
            return this.c(this.b(2), 14);
         } else if (var1[0].charAt(0) == '\\') {
            System.out.println("h3ll0_w0rld!");
            return this.c(this.b(1), 4);
         } else {
            return this.c(this.b(-23), 3);
         }
      } else {
         int[] var2 = new int[]{79, 102, 121, 117, 33, 85, 106, 110, 102};
         String var3 = "";
         int[] var4 = var2;
         int var5 = var2.length;

         for(int var6 = 0; var6 < var5; ++var6) {
            int var7 = var4[var6];
            var3 = var3 + (var7 - 1) + " ";
         }

         return this.c(var3, 0);
      }
   }

   private String b(int var1) {
      switch(var1) {
      case -23:
         return "th3-fl4g-hunt3rs";
      case 0:
         return "gniog peek";
      case 1:
         return "kr3w ver ";
      case 2:
         return "P r o b z G o t I t ?";
      case 78:
         return "3xc3ll3nt" + this.random;
      default:
         throw new IllegalArgumentException("Unexpected arg " + var1);
      }
   }

   private String c(String var1, int var2) {
      char[] var3 = "pecan{".toCharArray();
      byte var4 = 125;
      var2 += 5;

      for(int var5 = 0; var5 < var3.length; ++var5) {
         var3[var5] = (char)(var3[var5] + var2);
      }

      char var11 = (char)(var4 + var2);
      String var10000 = new String(var3);
      String var12 = var10000 + var1;
      if (var2 == 0) {
         if (!this.toggle) {
            var12 = var12 + "tAErg";
         } else {
            var12 = var12 + ".kmnA";
         }
      } else if (var2 == 1) {
         var12 = var12 + "xOMyP";
      } else {
         var12 = var12 + "A6sOw";
         if (this.toggle) {
            System.out.print("Nic");
            System.out.println("e");
            return "{" + var12.substring(1, 4) + "}";
         }
      }

      var12 = var12 + var11;
      String var6 = "";
      char[] var7 = var12.toCharArray();
      int var8 = var7.length;

      for(int var9 = 0; var9 < var8; ++var9) {
         char var10 = var7[var9];
         if (var10 > '~') {
            var10 = '_';
         }

         var6 = var6 + var10;
      }

      return var6;
   }
}
```