import java.lang.Math;
import java.lang.System;

public class PublicStaticVoidMainStringArgs {

    final double random = Math.random() * 1024f;
    boolean toggle = true;

    public static void main(
        final String[] args
    ) {
        new PublicStaticVoidMainStringArgs(args);
    }

    public PublicStaticVoidMainStringArgs(
        final String[] args
    ) {
        System.out.println(a(args));
    }

    private String a(
        final String[] args
    ) {
        if(args.length != 1) {
            int[] ints = new int[]{79, 102, 121, 117, 33, 85, 106, 110, 102};
            String str = "";
            for (int i : ints) {
                str += (i - 1) + " ";
            }
            return c(str, 0);
        }

        if(args[0].length() != 1) {
            return c(b(0), 5);
        }

        if(args[0].equals("%")) {
            int x = (-7 + (int) 1);
            return c(b(1), (x * 1) + 1);
        }

        if((int) args[0].charAt(0) < (int) '\\') {
            System.out.println("your number is " + (int) (Math.random() * 100));
            if(random == 1.23) {
                toggle = false;
            }
            System.out.println(toggle);
            return c(b(2), (int) 14.0);
        }

        if((int) args[0].charAt(0) == (char) 92) {
            System.out.println("h3ll0_w0rld!");
            return c(b(1), 4);
        }

        return c(b(-23), (6 / 2));
    }

    private String b(
        final int i
    ) {
        switch(i) {
            case -23:
                return "th3-fl4g-hunt3rs";
            case 0:
                return "gniog peek";
            case 1:
                return "kr3w ver ";
            case 2:
                return "P r o b z G o t I t ?";
            case 78:
                return "3xc3ll3nt" + random;
            default:
                throw new IllegalArgumentException("Unexpected arg " + i);
        }
    }

    private String c(
        final String s,
        int d
    ) {
        char[] prefix = "pecan{".toCharArray();
        char suffix = '}';

        d += 5;

        for(int i = 0; i < prefix.length; i++) {
            prefix[i] += d;
        }

        suffix += d;

        String n = new String(prefix) + s;

        if(d == 0) {
            if(!toggle) {
                n += "tAErg";
            } else {
                n += ".kmnA";
            }
        } else if(d == 1) {
            n += "xOMyP";
        } else {
            n += "A6sOw";
            if(toggle) {
                System.out.print("N" + "i" + "c");
                System.out.println("e");
                return "{" + n.substring(1, 4) + "}";
            }
        }

        n += suffix;

        String nn = "";
        for(char c : n.toCharArray()) {
            if((int) c > 0x7e) {
                c = '_';
            }

            nn += c;
        }

        return nn;
    }

}
