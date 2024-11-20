package pe.edu.jgm._java._21._04._colletion;

import java.util.*;

public class SequencedSetExample {

    public static void main(String[] args) {

        SequencedMap<Integer, String> people = new LinkedHashMap<>();
        people.put(10,"Ingrid");
        people.put(20,"Roberto");
        people.putFirst(0,"Jaime");
        people.putLast(2,"Rocio");
        System.out.println("After add record: " + people);
        System.out.println("Fetching first entry: " + people.firstEntry());
        System.out.println("Fetching last entry: " + people.lastEntry());
        System.out.println("Removing first entry: " + people.pollFirstEntry());
        System.out.println("Removing last entry: " + people.pollLastEntry());
        System.out.println("Reversed: " + people.reversed());

    }
}
