import java.util.LinkedList;  // Correct import

public class AddElements {
    public static void main(String[] args) {
        // Creating a LinkedList of Strings
        LinkedList<String> list = new LinkedList<String>();

        // Adding elements to the LinkedList using add() method
        list.add("ein");
        list.add("zwei");
        list.add("drei");
        list.add("viel");
        list.add("funf");

        // Print the LinkedList
        System.out.println(list);
    }
}
