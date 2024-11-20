package pe.edu.jgm._java._17._01_sealed;

public class _Application {

    public static void main(String[] args) {

        AccountProcess accountProcess = new AccountProcess(100,5);
        LogisticProcess logisticProcess = new LogisticProcess(101,0.80);
        MarketingProcess marketingProcess = new MarketingProcess(102, true);

        inspectProcess(accountProcess);
        inspectProcess(logisticProcess);
        inspectProcess(marketingProcess);

    }

    private static void inspectProcess(Process process) {
        switch (process) {
            case AccountProcess accountProcess -> System.out.println("Check Account process with " + accountProcess.nroOffice + " offices.");
            case LogisticProcess logisticProcess -> System.out.println("Check Logistic process with " + logisticProcess.rateOfQuality  + " rate of quality.");
            case MarketingProcess marketingProcess -> System.out.println("Check Marketing process " +(marketingProcess.hasPromotion ? "with" : "without") + " promotion.");
            default -> System.out.print("Do nothing");
        }
    }
}
