import javax.swing.JOptionPane; //pct java extesion e subpacote swing, dentro do subpacote tem a class JOptionPane
public class HelloWorld{                          //class para escrever o método main
    public static void main(String [] args) {   //mét main, delimitado por {} c/ tipo de retorno void, com o paramêtro vetor de strings
        //System.out.println("Hello, World");     //Classe de funcionalidade de exbição textual na linha de comando, println(pula uma linha)
        JOptionPane.showMessageDialog(null, "Hello, World"); //JOptPane - op de acesso a membro(.) - mét -> showMesDia ->Membro da class JOptPane 
    }
}
// HelloWorld, String e System são 3 classes diferentes
