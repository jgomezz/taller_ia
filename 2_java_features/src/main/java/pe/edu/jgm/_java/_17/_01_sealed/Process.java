package pe.edu.jgm._java._17._01_sealed;

public sealed class Process permits AccountProcess, LogisticProcess, MarketingProcess {
//public  class Process {

    protected int id;

    public Process(int id) {
        this.id = id;
    }

}
