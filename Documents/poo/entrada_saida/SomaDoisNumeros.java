import javax.swing.JOptionPane; 

public class SomaDoisNumeros{  
    static public void main(String [] abc){ 
        //declaracao de variaveis - fase 1
        double a , b, result;
     
        //entrada de dados -fase 2
       a = Double.parseDouble(JOptionPane.showInputDialog("Digite o primeiro valor")); 
       b = Double.parseDouble(JOptionPane.showInputDialog("Digite o segundo valor")); 

        //processamente - fase 3
        result = a + b;

        //saida de dados - fase 4
        JOptionPane.showMessageDialog(null, result);
    }
}