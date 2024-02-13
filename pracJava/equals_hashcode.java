public class equals_hashcode {
    public static void main(String[] args) {
        Solution();
    }
    
    private static void Solution(){
        String a = "abc";
        String b = "abc";
        a += "d";
        b += "d";

        System.out.println(a);
        System.out.println(b);

        System.out.println(a == b);
        System.out.println(a.equals(b));
        int hashA = a.hashCode();
        int hashB = b.hashCode();
        System.out.println(hashA == hashB);
        System.out.println(hashA);
        System.out.println(hashB);

    }
}

