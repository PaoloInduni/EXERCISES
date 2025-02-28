public class ej3 {

    public static void main(String[] args) {
        int[] prices = {7,1,5,3,6,4};

        System.out.println(maxProfit(prices));
    }

    public static int maxProfit(int[] prices) {

        int profit = 0;

        for (int sellingDay = (prices.length-1); sellingDay>0; sellingDay--) {

            System.out.println("Día de venta: "+(sellingDay+1)+" Precio: " + prices[sellingDay]);

            for (int buyingDay = 0; buyingDay<sellingDay; buyingDay++){

                System.out.println("Día de compra: "+(buyingDay+1)+" Precio: " + prices[buyingDay]);

                System.out.println("Profit: "+profit);

                if(prices[sellingDay] - prices[buyingDay] > profit){

                    System.out.println("Se guardó el profit como el más alto");

                    profit = prices[sellingDay] - prices[buyingDay];
                }
            }
        }

        return profit;
    }
}
