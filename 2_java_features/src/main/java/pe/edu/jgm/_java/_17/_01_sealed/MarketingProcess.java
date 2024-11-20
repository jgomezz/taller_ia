package pe.edu.jgm._java._17._01_sealed;

public final class MarketingProcess extends Process{

    protected boolean hasPromotion;

    public MarketingProcess(int id, boolean hasPromotion) {
        super(id);
        this.hasPromotion = hasPromotion;
    }
}
