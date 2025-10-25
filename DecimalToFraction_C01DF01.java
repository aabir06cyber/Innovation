import java.util.*;
class DecimalToFraction_C01DF01
{
    public static void main(String[] args)
    {
        Scanner dm=new Scanner(System.in);
        System.out.println("What is the decimal number ?");
        double d=dm.nextDouble();
        //Conversion begins...
        String cd=Double.toString(d);
        String no1="";
        String no2="";
        int num=0;
        int den=0;
        int gcd=1;
        int index=cd.indexOf('.');
        no1=cd.substring(index+1); //No. of characters after '.'
        den=(int) Math.pow(10,no1.length()); //DENOMINATOR
        for(int c=0;c<cd.length();c++)
        {
            if(cd.charAt(c)!='.')
            {
                no2=no2.concat(Character.toString(cd.charAt(c))); //No. without '.'
            }
        }
        num=Integer.parseInt(no2); //NUMERATOR
        
        for(int div=1;div<=(Math.min(num,den));div++)
        {
            if((num%div==0) && (den%div==0))
            {
                gcd=div; //Find Greatest Common Divisor [GCD]
            }
        }
        int fnum=num/gcd;
        int fden=den/gcd;
        if(fnum>fden && fden!=1) //for mixed fraction
        {
            int mxfnum=fnum/fden;
            int mxfnum_u=fnum-(fden*mxfnum);
            System.out.println("Fraction form of '"+d+"' : "+fnum+"/"+fden+" [MF: "+mxfnum+"  "+mxfnum_u+"/"+fden+"]");
        }
        else
        {
            System.out.println("Fraction form of '"+d+"' : "+fnum+"/"+fden);
        }
    }
}