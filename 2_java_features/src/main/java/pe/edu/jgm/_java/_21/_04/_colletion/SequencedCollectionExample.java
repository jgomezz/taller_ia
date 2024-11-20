package pe.edu.jgm._java._21._04._colletion;

import java.util.ArrayList;
import java.util.List;

public class SequencedCollectionExample {

    public static void main(String[] args) {

        List<String> people = new ArrayList<String>();
        people.add("Ingrid");
        people.add("Roberto");
        people.addFirst("Jaime");
        people.addLast("Rocio");
        System.out.println("After add record: " + people);

        System.out.println("First: " + people.getFirst());
        System.out.println("Last: " + people.getLast());

        people.removeFirst();
        System.out.println("After removing first: " + people);

        people.removeLast();
        System.out.println("After removing last: " + people);
    }
}
