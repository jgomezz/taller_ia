package pe.edu.jgm._java._21._03._pattern_matching_switch;

sealed interface Classroom permits TeoClassroom, LabClassroom {};

record TeoClassroom (int id, String name, int capacity) implements Classroom{};
record LabClassroom (int id, String name, int capacity, int nroOfComputer) implements Classroom{};

/**
 * Java 21 introduced Pattern Matching for switch, which enhances the power of the switch statement by allowing you
 * to match patterns and destructure objects
 */
public class Application {

    public static void main(String[] args) {

        //
        Classroom lab701 = new LabClassroom(10,"701",20,24 );
        Classroom room1510 = new TeoClassroom(10,"1510",40 );

        //
        processClassroom(lab701);
        processClassroom(room1510);

    }

    /**
     *
     * @param cr
     */
    private static void processClassroom(Classroom cr) {

        String result = switch (cr){
            case TeoClassroom(int id, String name, int capacity) -> "The lab is " + name;
            case LabClassroom(int id, String name, int capacity, int nroOfComputer ) -> "The Teo is " + name;
        };

        System.out.println(result);

    }
}
