public class HelloApp {
    public static void main(String[] args) {

        if (args.length == 0) {
            System.out.println("Hello, World!");
        } else {

            StringBuilder sb = new StringBuilder();

            for (String name : args) {
                sb.append(name).append(", ");
            }

            // remove last comma and space
            sb.setLength(sb.length() - 2);

            System.out.println("Hello, " + sb + "!");
        }
    }
}