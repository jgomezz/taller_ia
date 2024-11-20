package pe.edu.jgm._java._17._01_sealed;

public final class AccountProcess extends Process{

    protected int nroOffice;

    public AccountProcess(int id, int nroOffice) {
        super(id);
        this.nroOffice = nroOffice;
    }
}
