package pe.edu.jgm._java._17._01_sealed;

public final class LogisticProcess extends Process{

    protected double rateOfQuality;

    public LogisticProcess(int id, double rateOfQuality) {
        super(id);
        this.rateOfQuality = rateOfQuality;
    }
}
