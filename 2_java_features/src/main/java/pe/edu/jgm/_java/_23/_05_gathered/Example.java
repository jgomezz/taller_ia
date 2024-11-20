package pe.edu.jgm._java._23._05_gathered;

import module java.base;
import static java.io.IO.*;

public class Example{

    void main(){
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6);
        List result = numbers.stream()
                .filter(number -> number % 2 == 0)
                .toList();
        println(result);
        // result: { 2, 4, 6 }

        long numberOfWords =
                Stream.of("the", "", "fox", "jumps", "over", "the", "", "dog")  // (1)
                        .filter(Predicate.not(String::isEmpty))                   // (2)
                        .collect(Collectors.counting());                          // (3)
        println(numberOfWords);



        /* // IDEAL
        result = Stream.of("foo", "bar", "baz", "quux")
                .distinctBy(String::length)      // Hypothetical
                .toList();

        // result ==> [foo, quux]
        */
         result = Stream.of("foo", "bar", "baz", "quux")
                .map(DistinctByLength::new)
                .distinct()
                .map(DistinctByLength::str)
                .toList();

        // result ==> [foo, quux]
        println(result);

         /* // IDEAL
        result = Stream.iterate(0, i -> i + 1)
                .windowFixed(3)                  // Hypothetical
                .limit(2)
                .toList();

        // result ==> [[0, 1, 2], [3, 4, 5]]
         */

        result
                = Stream.iterate(0, i -> i + 1)
                .limit(3 * 2)
                .collect(Collector.of(
                        () -> new ArrayList<ArrayList<Integer>>(),
                        (groups, element) -> {
                            if (groups.isEmpty() || groups.getLast().size() == 3) {
                                var current = new ArrayList<Integer>();
                                current.add(element);
                                groups.addLast(current);
                            } else {
                                groups.getLast().add(element);
                            }
                        },
                        (left, right) -> {
                            throw new UnsupportedOperationException("Cannot be parallelized");
                        }
                ));

        println(result);

        // windowFixed
        result = Stream.iterate(0, i -> i + 1)
                .gather(Gatherers.windowFixed(2))
                .limit(5)
                .collect(Collectors.toList());
        println(result);

        // windowSliding
        result = Stream.iterate(0, i -> i + 1)
                .gather(Gatherers.windowSliding(2))
                .limit(5)
                .collect(Collectors.toList());
        println(result);

        // fold > Gatherers.fold is like a refined version of the Stream.reduce
        String res = Stream.of("hello","world","how","are","you?")
                .gather(Gatherers.fold(() -> "",(acc, element) -> acc.isEmpty() ? element : acc + "," + element))
                .findFirst()
                .get();

        println(res);

        res = Stream.of("hello", "world","how", "are", "you?")
                .reduce("", (acc, element) -> acc.isEmpty() ? element.trim() : acc + "," + element);
        println(res);

        var res2 = Stream.of(1,"hello", true).gather(Gatherers.fold(() -> 0, (acc, el) -> acc + 1));
        println(res2.findFirst().get());

        // Gatherers.scan
        var res3 = Stream.of(1,2,3,4,5,6,7,8,9)
                .gather(Gatherers.scan(() -> "", (string, number) -> string + number))
                .toList();
        println(res3);

        // Gatherers.mapConcurrent >  limits the concurrency to four threads
        var res4 = Stream.of(1,2,3,4,5)
                .gather(Gatherers.mapConcurrent(4, x -> x * x))
                .collect(Collectors.toList());
        println(res4);

        System.out.println("Type of res4: " + ((Object) res4).getClass().getName());

    }

}

record DistinctByLength(String str) {

    @Override public boolean equals(Object obj) {
        return obj instanceof DistinctByLength(String other)
                && str.length() == other.length();
    }

    @Override public int hashCode() {
        return str == null ? 0 : Integer.hashCode(str.length());
    }

}